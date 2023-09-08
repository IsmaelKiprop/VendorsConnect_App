from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['address', 'phone_number', 'profile_picture', 'bio']

class DistributorRegistrationForm(UserCreationForm):
    company_name = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'company_name', 'phone_number']

class VendorRegistrationForm(UserCreationForm):
    company_name = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'company_name', 'phone_number']

class CustomProfileForm(forms.ModelForm):
    address = forms.CharField(max_length=200, required=True)  # Updated to required=True
    phone_number = forms.CharField(max_length=20, required=True)  # Updated to required=True
    profile_picture = forms.ImageField(required=False)
    bio = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = UserProfile
        fields = ['address', 'phone_number', 'profile_picture', 'bio']
