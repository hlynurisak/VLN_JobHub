from django.shortcuts import render, get_object_or_404
from company.models import Company
from JobHub.models import Job
# Create your views here.
def index(request):
    return render(request, 'company/companies.html', {
        'company': Company.objects.all().order_by('name')
    })

def company_info(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    return render(request, 'company/company-info.html', {'company': company})