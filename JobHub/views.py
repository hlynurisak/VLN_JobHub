from django.shortcuts import render
from JobHub.models import Job


# Create your views here.
def index(request):
    context = {'JobHub': Job.objects.all().order_by('name')}
    return render(request, 'JobHub/home_page.html', context)