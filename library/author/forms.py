from django import forms
from .models import Author

class CreateEditAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'  # to show all fields
