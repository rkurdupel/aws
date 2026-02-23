from django import forms
from authentication.models import CustomUser

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            'first_name', 'middle_name', 'last_name', 'email'
        )
