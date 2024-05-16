from django.shortcuts import render, get_object_or_404, redirect

import JobHub
from JobHub.forms.jobhub_form import JobCreateForm
from JobHub.models import Job, CompanyImage


# Create your views here.
def index(request):
    context = {'JobHub': Job.objects.all().order_by('name')}
    return render(request, 'JobHub/home_page.html', context)

def get_job_by_id(request, id):
    return render('JobHub/home_page.html',{
        'JobHub': get_object_or_404(JobHub, pk=id)
    })


def create_joblisting(request):
    if request.method == 'POST':
        form =JobCreateForm(data=request.POST)
        if form.is_valid():
            job = form.save()
            job.save()
            return redirect('/')
    else:
        form = JobCreateForm
    return render(request, 'JobHub/create_joblisting.html', {
        'form': form
    })

def delete_joblisting(request, id):
    job = get_object_or_404(Job, pk=id)
    job.delete()
    return redirect('/')
