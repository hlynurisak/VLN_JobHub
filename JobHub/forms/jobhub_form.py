from django import forms
from django.forms import ModelForm, widgets
from JobHub.models import Job

class JobCreateForm(ModelForm):
    class Meta:
        model = Job
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control'}),
            'due_date': widgets.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'company': widgets.Select(attrs={'class': 'form-control'}),
            'start_date': widgets.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'job_type': widgets.Select(attrs={'class': 'form-control'}),
        }
