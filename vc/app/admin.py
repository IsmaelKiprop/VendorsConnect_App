# admin.py
from django.contrib import admin
from .models import Vendor, Distributor, UserProfile


class VendorAdmin(admin.ModelAdmin):
    list_display = ('username','email',  'password', 'address', 'phone_number')  # Customize the fields displayed in the admin list view
    search_fields = ('username', 'email', 'phone_number')  # Enable search by name, email, and phone number

admin.site.register(Vendor, VendorAdmin)

class DistributorAdmin(admin.ModelAdmin):
    list_display = ('username','email',  'password', 'address', 'phone_number')  # Customize the fields displayed in the admin list view
    search_fields = ('username', 'email', 'phone_number')  # Enable search by name, email, and phone number

admin.site.register(Distributor, DistributorAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone_number' , 'profile_picture' , 'bio')  # Customize the fields displayed in the admin list view
    search_fields = ('adress' , 'phone_number') 
    
admin.site.register(UserProfile, UserProfileAdmin)
    

