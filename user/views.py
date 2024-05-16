from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import UpdateUserForm, UpdateProfileForm
from .models import Profile

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
            user = form.save()
            Profile.objects.create(user=user)
            return redirect('login')

    return render(request, 'user/register.html', {
        'form': UserCreationForm()
    })


@login_required
def profile(request):
    return render(request, 'user/profile.html', context={'companies': companies})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request,
                  template_name='user/edit_profile.html',
                  context={'user_form': user_form, 'profile_form': profile_form})


def user_name(request):
    if request.user.is_authenticated:
        return {'user_name': request.user.username}
    return {}
