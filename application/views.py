from django.shortcuts import render, redirect, get_object_or_404
from application.forms.forms import ContactInformationForm, CoverLetterForm, ExperienceForm, RecommendationForm
from JobHub.models import Job


# Create your views here.
def application_view(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'application/application-info.html', {'job': job})


def apply(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':
        contact_form = ContactInformationForm(request.POST)
        cover_form = CoverLetterForm(request.POST)
        experience_form = ExperienceForm(request.POST)
        recommendation_form = RecommendationForm(request.POST)

        if all([contact_form.is_valid(), cover_form.is_valid(), experience_form.is_valid(),
                recommendation_form.is_valid()]):
            # Save the form data to the database
            # ...
            return redirect('applications', job_id=job_id)
    else:
        contact_form = ContactInformationForm()
        cover_form = CoverLetterForm()
        experience_form = ExperienceForm()
        recommendation_form = RecommendationForm()

    return render(request, 'application/applications.html', {
        'job': job,
        'contact_form': contact_form,
        'cover_form': cover_form,
        'experience_form': experience_form,
        'recommendation_form': recommendation_form
    })


def success(request):
    return render(request, 'application/success.html', {})