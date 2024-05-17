from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from application.forms.forms import ContactInformationForm, CoverLetterForm, ExperienceFormSet, RecommendationFormSet
from JobHub.models import Job
from application.models import Application, Experience, Recommendation


# Create your views here.
def application_view(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'application/application-info.html', {'job': job})


@login_required
def apply(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':
        contact_form = ContactInformationForm(request.POST)
        cover_form = CoverLetterForm(request.POST)
        experience_formset = ExperienceFormSet(request.POST, prefix='experiences')
        recommendation_formset = RecommendationFormSet(request.POST, prefix='recommendations')

        if (contact_form.is_valid() and cover_form.is_valid() and
                experience_formset.is_valid() and recommendation_formset.is_valid()):

            contact_info = contact_form.save()
            cover_letter = cover_form.save()

            application = Application.objects.create(
                company=job.company,
                job=job,
                applicant=request.user,
                contact_info=contact_info,
                cover_letter=cover_letter,
                status='Pending'
            )

            for form in experience_formset:
                experience = form.save(commit=False)
                experience.application = application
                experience.save()

            for form in recommendation_formset:
                recommendation = form.save(commit=False)
                recommendation.application = application
                recommendation.save()

            return redirect('application-info', args=[job_id])
    else:
        contact_form = ContactInformationForm()
        cover_form = CoverLetterForm()
        experience_formset = ExperienceFormSet(queryset=Experience.objects.none(), prefix='experiences')
        recommendation_formset = RecommendationFormSet(queryset=Recommendation.objects.none(), prefix='recommendations')

    return render(request, 'application/applications.html', {
        'job': job,
        'contact_form': contact_form,
        'cover_form': cover_form,
        'experience_formset': experience_formset,
        'recommendation_formset': recommendation_formset
    })


def success(request):
    return render(request, 'application/success.html', {})