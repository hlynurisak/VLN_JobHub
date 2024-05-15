from django.shortcuts import render, get_object_or_404

import JobHub
from JobHub.models import Job


# Create your views here.
def index(request):
    context = {'JobHub': Job.objects.all().order_by('name')}
    return render(request, 'JobHub/home_page.html', context)

def get_job_by_id(request, id):
    return render('JobHub/home_page.html',{
        'Jobjub': get_object_or_404(JobHub, pk=id)
    })


#def create_job(request):
#    if request.method == 'POST':
#        print(1)
#   else:
#        print(2)
#    return render(request, 'JobHub/create_job.html', {
#        'form': form
#    })
