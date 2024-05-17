from django import forms
from django.forms import ModelForm, widgets
from company.models import Company

class CreateCompany(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Company
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'CompanyStart_date': widgets.DateInput(attrs={'class': 'form-control', 'type': 'date'}),  # Use type='date'
            'location': widgets.TextInput(attrs={'class': 'form-control'}),
            'link_to_page': widgets.URLInput(attrs={'class': 'form-control'}),  # Correct widget for URL field
            'description': widgets.Textarea(attrs={'class': 'form-control'}),  # Use Textarea for larger text input
        }
