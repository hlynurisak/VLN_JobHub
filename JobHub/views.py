from django.shortcuts import render

companies = [
    {'name': 'Coca Cola', 'job_listing': "Data Analyst"},
    {'name': 'Dominos', 'job_listing': "Computer Scientist"}
]
# Create your views here.
def index(request):
    return render(request, 'JobHub/index.html', context= {'companies': companies})