from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import VendorRegistrationForm, DistributorRegistrationForm
from .models import UserProfile
from .openfoodfacts import get_product_details
from .openfoodfacts import fetch_dairy_products
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm

# Create your views here.
def home(request):
    return render(request,"app/home.html")

def product_details_view(request, barcode):
    product_data = get_product_details(barcode)
    # Process and display the product data as needed

def home(request):
    # Fetch dairy products data from the Open Food Facts API
    dairy_products = fetch_dairy_products()  # Replace this with your own logic

    context = {
        'dairy_products': dairy_products,
    }
    return render(request, 'app/home.html', context)


def product_details_view(request, barcode):
    product_data = get_product_details(barcode)
    # Process and validate product_data as needed
    if product_data and isinstance(product_data, dict) and product_data:
        # Render a template or create a response
        context = {
            'product_data': product_data,
        }
        return render(request, 'app/product_details.html', context)
    else:
        # Return an appropriate response when product data is not found
        return render(request, 'app/product_not_found.html')

def vendor_registration(request):
    if request.method == 'POST':
        form = VendorRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user data
            UserProfile.objects.create(user=user)  # Create a user profile
            # You can also perform additional tasks like sending a welcome email
            return redirect('registration_success')  # Redirect to a success page
    else:
        form = VendorRegistrationForm()
    return render(request, 'app/vendor_registration.html', {'form': form})

def distributor_registration(request):
    if request.method == 'POST':
        form = DistributorRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user data
            UserProfile.objects.create(user=user)  # Create a user profile
            # You can also perform additional tasks like sending a welcome email
            return redirect('registration_success')  # Redirect to a success page
    else:
        form = DistributorRegistrationForm()
    return render(request, 'app/distributor_registration.html', {'form': form})

def registration_success(request):
    return render(request, 'app/registration_success.html')

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



