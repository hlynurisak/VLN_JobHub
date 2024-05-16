from django.shortcuts import render, get_object_or_404, redirect

from company.forms.company_form import CreateCompany
from company.models import Company
from JobHub.models import Job, CompanyImage


# Create your views here.
def index(request):
    return render(request, 'company/companies.html', {
        'company': Company.objects.all().order_by('name')
    })

def company_info(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    return render(request, 'company/company-info.html', {'company': company})

def create_company(request):
    if request.method == 'POST':
        form =CreateCompany(data=request.POST)
        if form.is_valid():
            company = form.save()
            company.image = CompanyImage(image= request.POST['image'],company=company)
            company.image.save()
            return redirect('company-index')
    else:
        form = CreateCompany
    return render(request, 'company/create_company.html', {
        'form': form
    })