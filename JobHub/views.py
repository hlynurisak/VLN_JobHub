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
        'Jobjub': get_object_or_404(JobHub, pk=id)
    })


def create_joblisting(request):
    if request.method == 'POST':
        form =JobCreateForm(data=request.POST)
        if form.is_valid():
            job = form.save()
            job_image = CompanyImage(image=request.POST['image'], job=job)
            job_image.save()
            return redirect('Jobhub-index')
    else:
        form = JobCreateForm
    return render(request, 'JobHub/create_joblisting.html', {
        'form': form
    })
