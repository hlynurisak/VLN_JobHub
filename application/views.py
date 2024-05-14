from django.shortcuts import render, get_object_or_404
from JobHub.models import Job


# Create your views here.
def application_view(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'application/applications.html', {'job': job})