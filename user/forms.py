from django import forms
from django.contrib.auth.models import User
from .models import Profile

from PIL import Image


class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(required=True, max_length=50,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(required=True, max_length=50,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))

    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class UpdateProfileForm(forms.ModelForm):
    image = forms.URLField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ['image']