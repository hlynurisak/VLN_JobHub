from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
companies = [
    {'name': 'Coca Cola', 'job_listing': "Data Analyst"},
    {'name': 'Dominos', 'job_listing': "Computer Scientist"},
    {'name': 'CCP', 'job_listing': "Nerd"},
    {'name': 'Elko', 'job_listing': "Trúður í Verslun"},
    {'name': 'Sýn', 'job_listing': "Fréttamaður"},
    {'name': 'Rúv', 'job_listing': "Gott framlag í Eurovision"},

]


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, 'user/register.html', {
        'form': UserCreationForm()
    })


def profile(request):
    return render(request, 'user/profile.html', context={'companies': companies})
