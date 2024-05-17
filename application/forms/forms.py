from django import forms
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
    class Meta:
        model = Experience
        fields = ['workplace', 'role', 'start_date', 'end_date']


class RecommendationForm(forms.ModelForm):
    class Meta:
        model = Recommendation
        fields = ['rec_name', 'rec_email', 'rec_phone', 'rec_role', 'rec_contact']
