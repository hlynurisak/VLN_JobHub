from django.shortcuts import render
from company.models import Company
from JobHub.models import Job
# Create your views here.
def index(request):
    return render(request, 'company/companies.html', {
        'company': Company.objects.all()
    })


def company_logo(request):
    logo = ''
    job_id = request.resolver_match.kwargs.get('job_id')
    if job_id:
        try:
            job = Job.objects.get(id=job_id)
            company = job.company  # Assuming a ForeignKey from Job to Company
            logo = company.logo
        except Job.DoesNotExist:
            logo = ''
    return {'logo': logo}