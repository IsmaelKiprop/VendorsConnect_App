from django import forms
from .models import UserProfile
from .models import Vendor, Distributor

class VendorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['username', 'email', 'password', 'address', 'phone_number'] # Add fields specific to Vendor registration

class DistributorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Distributor
        fields = ['username', 'email', 'password', 'address', 'phone_number'] # Add fields specific to Distributor registration
        


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['address', 'phone_number', 'profile_picture', 'bio']
        # Add any other fields from the UserProfile model that you want to include in the form

    # You can add additional form validation or customize the form fields here if needed
