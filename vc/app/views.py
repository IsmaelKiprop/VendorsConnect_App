from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import VendorRegistrationForm, DistributorRegistrationForm

# Create your views here.
def home(request):
    return render(request,"app/home.html")

def register_as_vendor_views(request):
    # Your registration logic for vendors here
    return render(request, 'app/register_as_vendor.html')

def register_as_distributor_views(request):
    # Your registration logic for vendors here
    return render(request, 'app/register_as_distributor.html')

def orders_view(request):
    # Implement logic to retrieve and display the user's orders
    return render(request, 'app/orders.html')

def search_views(request):
    # Implement logic to retrieve and display the user's orders
    return render(request, 'app/search.html')

def common_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Create a new user account
            user = form.save()

            # Log the user in
            login(request, user)

            # Redirect to a success page (e.g., profile)
            return redirect('profile')
    else:
        form = UserCreationForm()

    return render(request, 'app/register.html', {'form': form})

@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after saving the profile data
    else:
        form = ProfileForm(instance=user.profile)

    context = {
        'form': form,
    }
    return render(request, 'app/profile.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Create a new user account
            user = form.save()
            
            # Log the user in
            login(request, user)
            
            # Redirect to a success page (e.g., profile)
            return redirect('profile')
    else:
        form = UserCreationForm()
    
    return render(request, 'app/register.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important for keeping the user logged in
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')  # Redirect to the profile page or any desired page
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'registration/password_change_form.html', {
        'form': form,
    })
