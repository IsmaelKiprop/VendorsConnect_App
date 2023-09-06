from django.db import models
from django.contrib.auth.models import User


class Vendor(models.Model):
    username = models.CharField(max_length=100, unique=True, default="")
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, null=True)  # Use a more secure field like PasswordField in production
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    # Add other fields specific to vendors

    def __str__(self):
        return self.username

class Distributor(models.Model):
    username = models.CharField(max_length=100, unique=True, default="")
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, null=True)  # Use a more secure field like PasswordField in production
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    # Add other fields specific to distributors

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    # Add any other fields you want for the user profile

    def __str__(self):
        return self.user.username

    


