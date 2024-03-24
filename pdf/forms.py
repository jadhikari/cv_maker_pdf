# forms.py
from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'  # You can specify the fields you want in the form explicitly instead of using '__all__'
