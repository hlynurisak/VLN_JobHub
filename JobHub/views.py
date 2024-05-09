from django.shortcuts import render

companies = [
    {'name': 'Coca Cola', 'job_listing': "Data Analyst"},
    {'name': 'Dominos', 'job_listing': "Computer Scientist"},
    {'name': 'CCP', 'job_listing': "Nerd"},
    {'name': 'Elko', 'job_listing': "Trúður í Verslun"},
    {'name': 'Sýn', 'job_listing': "Fréttamaður"},
    {'name': 'Rúv', 'job_listing': "Gott framlag í Eurovision"},

]
# Create your views here.
def index(request):
    return render(request, 'JobHub/index.html', context= {'companies': companies})