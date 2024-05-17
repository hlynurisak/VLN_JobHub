from django import forms


class ContactInformationForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    street = forms.CharField(label='Street name', max_length=100)
    house_number = forms.CharField(label='House number', max_length=10)
    city = forms.CharField(label='City', max_length=50)
    country = forms.CharField(label='Country', max_length=50)
    postal_code = forms.CharField(label='Postal code', max_length=20)


class CoverLetterForm(forms.Form):
    cover_letter = forms.CharField(widget=forms.Textarea, label='Cover letter')


class ExperienceForm(forms.Form):
    workplace = forms.CharField(label='Place of work', max_length=100)
    role = forms.CharField(label='Role', max_length=100)
    start_date = forms.DateField(label='Start date', widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(label='End date', widget=forms.DateInput(attrs={'type': 'date'}))


class RecommendationForm(forms.Form):
    rec_name = forms.CharField(label='Name', max_length=100)
    rec_email = forms.EmailField(label='Email')
    rec_phone = forms.CharField(label='Phone number', max_length=15)
    rec_role = forms.CharField(label='Role', max_length=100)
    rec_contact = forms.BooleanField(label='May be contacted', required=False)
