from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

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
