from django.shortcuts import render
from company.models import Company
# Create your views here.
def index(request):
    return render(request, 'company/index.html',{
        'comapany': Company.objects.all()
    })

"Testing"