from django.shortcuts import render, redirect, get_object_or_404
from application.forms.forms import ContactInformationForm, CoverLetterForm, ExperienceFormSet, RecommendationFormSet
from JobHub.models import Job
from application.models import Application, Experience, Recommendation


# Create your views here.
def application_view(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'application/application-info.html', {'job': job})


def apply(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    user = request.user

    if request.method == 'POST':
        contact_form = ContactInformationForm(request.POST)
        cover_form = CoverLetterForm(request.POST)
        experience_formset = ExperienceFormSet(request.POST, prefix='experiences')
        recommendation_formset = RecommendationFormSet(request.POST, prefix='recommendations')

        if all([contact_form.is_valid(), cover_form.is_valid(), experience_formset.is_valid(),
                recommendation_formset.is_valid()]):

            contact_info = contact_form.save(commit=False)
            contact_info.save()

            cover_letter = cover_form.save(commit=False)
            cover_letter.save()

            experiences = experience_formset.save(commit=False)
            experiences.save()

            recommendations = recommendation_formset.save(commit=False)
            recommendations.save()

            application = Application.objects.create(
                company=job.company,
                applicant=user,
                job=job,
                experience=experience,
                recommendation=recommendation,
                cover_letter=cover_letter,
                status='Pending'
            )

            for experience in experiences:
                application.experience.add(experience)

            for recommendation in recommendations:
                application.recommendation.add(recommendation)

            return redirect('applications', job_id=job_id)
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