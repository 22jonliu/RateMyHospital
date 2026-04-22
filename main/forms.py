from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
import re

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'years_of_experience', 'work_title']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'profile-input', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'profile-input', 'placeholder': 'Last Name'}),
            'years_of_experience': forms.NumberInput(attrs={'class': 'profile-input', 'placeholder': 'Years of Experience'}),
            'work_title': forms.TextInput(attrs={'class': 'profile-input', 'placeholder': 'Work Title'}),
        }
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name and not re.search(r'[a-zA-Z]', first_name):
            raise forms.ValidationError("First name must contain at least one letter.")
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if last_name and not re.search(r'[a-zA-Z]', last_name):
            raise forms.ValidationError("Last name must contain at least one letter.")
        return last_name
    
    def clean_years_of_experience(self):
        years = self.cleaned_data.get('years_of_experience')
        if years is not None and years < 0:
            raise forms.ValidationError("Years of experience cannot be negative.")
        return years
