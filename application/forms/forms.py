from django import forms
from django.forms import modelformset_factory
from application.models import ContactInformation, CoverLetter, Experience, Recommendation


class ContactInformationForm(forms.ModelForm):
    class Meta:
        model = ContactInformation
        fields = '__all__'


class CoverLetterForm(forms.ModelForm):
    class Meta:
        model = CoverLetter
        fields = '__all__'


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
        labels = {
            'rec_name': 'Recommender Name',
            'rec_email': 'Recommender Email',
            'rec_phone': 'Recommender Phone',
            'rec_role': 'Recommender Role',
            'rec_contact': 'Contact Permission'
        }


ExperienceFormSet = modelformset_factory(Experience, form=ExperienceForm, extra=1, can_delete=False)
RecommendationFormSet = modelformset_factory(Recommendation, form=RecommendationForm, extra=1, can_delete=False)
