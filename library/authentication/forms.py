from django import forms
from .models import CustomUser

class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            'first_name', 'middle_name', 'last_name', 'email', 'password', 'role', 
        )
    
class LoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            'email', 'password'
        )

    # def  __init__(self, *args, **kwargs):
    #     super(CustomUserForm, self).__init__(*args, **kwargs)
    #     super.fields['email'].empty_label = "Select"
    #     super.fields["password"].required = False