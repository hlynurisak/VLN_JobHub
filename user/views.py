from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

from application.models import Application
from .forms import UpdateUserForm, UpdateProfileForm
from JobHub.anonymous_required import anonymous_required


@anonymous_required('home')
def register(request):
    if request.method == 'POST':
        user_create_form = UserCreationForm(data=request.POST)
        if user_create_form.is_valid():
            user_create_form.save()
            return redirect('login')

        else:
            return render(request,
                          'user/register.html',
                          {'user_create_form': user_create_form, 'errors': user_create_form.errors})

    return render(request, 'user/register.html', {
        'user_create_form': UserCreationForm(),
    })


@anonymous_required('home')
class CustomLogin(LoginView):
    template_name = 'user/login.html'


@login_required
def profile(request):
    applications = Application.objects.filter(applicant=request.user)
    return render(request, 'user/profile.html', context={'applications': applications})


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

