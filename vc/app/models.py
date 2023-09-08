from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
class Vendor(models.Model):
    username = models.CharField(max_length=100, unique=True, default="")
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, null=True)  # Use a more secure field like PasswordField in production
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    
    # Additional fields specific to vendors
    company_name = models.CharField(max_length=100)
    business_type = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    logo = models.ImageField(upload_to='vendor_logos/', blank=True)
    
    # Fields for business hours
    opening_time = models.TimeField(null=True, blank=True)
    closing_time = models.TimeField(null=True, blank=True)
    
    # Fields for products or services
    product_categories = models.ManyToManyField('ProductCategory', related_name='vendors', blank=True)
    services_offered = models.ManyToManyField('Service', related_name='vendors', blank=True)
    
    # Other custom fields can be added as needed

    def __str__(self):
        return self.username

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Distributor(models.Model):
    username = models.CharField(max_length=100, unique=True, default="")
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, null=True)  # Use a more secure field like PasswordField in production
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    business_type = models.CharField(max_length=100, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    # Add other fields specific to distributors

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    social_media_links = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    # Add any other fields you want for the user profile

    def __str__(self):
        return self.user.username

