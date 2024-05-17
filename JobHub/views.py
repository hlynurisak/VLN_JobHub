from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from JobHub.forms.jobhub_form import JobCreateForm
from JobHub.models import Job, JobCategory, Company

def index(request):
    job_offers = Job.objects.all()
    categories = JobCategory.objects.all()
    companies = Company.objects.all()

    # Filtering
    category_id = request.GET.get('category')
    if category_id:
        job_offers = job_offers.filter(category_id=category_id)

    company_id = request.GET.get('company')
    if company_id:
        job_offers = job_offers.filter(company_id=company_id)

    applied_filter = request.GET.get('applied')
    if applied_filter:
        # Assuming 'applied' is a boolean field in the Job model
        job_offers = job_offers.filter(applied=applied_filter)

    # Searching
    search_query = request.GET.get('search')
    if search_query:
        job_offers = job_offers.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))

    # Ordering
    order_by = request.GET.get('order_by')
    if order_by == 'date':
        job_offers = job_offers.order_by('-start_date')
    elif order_by == 'due_date':
        job_offers = job_offers.order_by('due_date')

    context = {
        'job_offers': job_offers,
        'categories': categories,
        'companies': companies
    }
    return render(request, 'JobHub/home_page.html', context)

def get_job_by_id(request, id):
    return render(request, 'JobHub/home_page.html', {
        'JobHub': get_object_or_404(Job, pk=id)
    })

def create_joblisting(request):
    if request.method == 'POST':
        form = JobCreateForm(data=request.POST)
        if form.is_valid():
            job = form.save()
            job.save()
            return redirect('/')
    else:
        form = JobCreateForm()
    return render(request, 'JobHub/create_joblisting.html', {
        'form': form
    })

def delete_joblisting(request, id):
    job = get_object_or_404(Job, pk=id)
    job.delete()
    return redirect('/')
