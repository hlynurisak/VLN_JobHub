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
        fields = '__all__'


class RecommendationForm(forms.ModelForm):
    class Meta:
        model = Recommendation
        fields = '__all__'


ExperienceFormSet = modelformset_factory(Experience, form=ExperienceForm, extra=1, can_delete=True)
RecommendationFormSet = modelformset_factory(Recommendation, form=RecommendationForm, extra=1, can_delete=True)
