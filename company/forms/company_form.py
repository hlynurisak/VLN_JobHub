from django.forms import ModelForm, widgets
from django import forms
from company.models import Company


class CreateCompany(ModelForm):
        image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

        class Meta:
            model = Company
            exclude = ['id']
            widgets = {
                'name': widgets.TextInput(attrs={'class': 'form-control'}),
                'address': widgets.DateInput(attrs={'class': 'form-control'}),
                'link_to_page': widgets.TextInput(attrs={'class': 'form-control'}),
            }