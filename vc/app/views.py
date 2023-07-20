from django.shortcuts import render
from .openfoodfacts import get_product_details
from .openfoodfacts import fetch_dairy_products
from .forms import VendorRegistrationForm, DistributorRegistrationForm

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





def registration_page(request):
    vendor_form = VendorRegistrationForm(prefix='vendor')
    distributor_form = DistributorRegistrationForm(prefix='distributor')

    if request.method == 'POST':
        vendor_form = VendorRegistrationForm(request.POST, prefix='vendor')
        distributor_form = DistributorRegistrationForm(request.POST, prefix='distributor')
        if vendor_form.is_valid() and distributor_form.is_valid():
            # Save the forms if both are valid
            vendor_form.save()
            distributor_form.save()
            # Redirect to a success page or another view
            # return redirect('success_url')

    return render(request, 'app/registration_page.html', {
        'vendor_form': vendor_form,
        'distributor_form': distributor_form,
    })

