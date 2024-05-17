from django import forms
from django.forms import modelformset_factory
from application.models import ContactInformation, CoverLetter, Experience, Recommendation


class ContactInformationForm(forms.ModelForm):
    class Meta:
        model = ContactInformation
        fields = ['name', 'street', 'house_number', 'city', 'country', 'postal_code']


class CoverLetterForm(forms.ModelForm):
    class Meta:
        model = CoverLetter
        fields = ['cover_letter']


class ExperienceForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Start date')
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='End date')

    class Meta:
        model = Experience
        fields = ['workplace', 'role', 'start_date', 'end_date']


class RecommendationForm(forms.ModelForm):
    class Meta:
        model = Recommendation
        fields = ['rec_name', 'rec_email', 'rec_phone', 'rec_role', 'rec_contact']


ExperienceFormSet = modelformset_factory(Experience, form=ExperienceForm, extra=1, can_delete=True)
RecommendationFormSet = modelformset_factory(Recommendation, form=RecommendationForm, extra=1, can_delete=True)
