from django.shortcuts import render
from company.models import Company
from JobHub.models import Job
# Create your views here.
def index(request):
    return render(request, 'company/companies.html', {
        'company': Company.objects.all().order_by('name')
    })