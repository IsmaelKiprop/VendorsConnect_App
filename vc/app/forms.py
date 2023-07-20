

from django import forms
from .models import Vendor, Distributor

class VendorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['username', 'email', 'password', 'address', 'phone_number'] # Add fields specific to Vendor registration

class DistributorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Distributor
        fields = ['username', 'email', 'password', 'address', 'phone_number'] # Add fields specific to Distributor registration