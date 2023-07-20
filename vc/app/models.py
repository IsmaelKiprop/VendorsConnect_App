from django.db import models






class Vendor(models.Model):
    username = models.CharField(max_length=100, unique=True,default="")
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128,null=True)  # Use a more secure field like PasswordField in production
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    # Add other fields specific to vendors

    def _str_(self):
        return self.username


class Distributor(models.Model):
    username = models.CharField(max_length=100, unique=True,default="")
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128,null=True)  # Use a more secure field like PasswordField in production
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    # Add other fields specific to distributors

    def _str_(self):
        return self.username

