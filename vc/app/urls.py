from django.urls import path
from . import views


app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
     path('vendor-registration/', views.vendor_registration, name='vendor_registration'),
    path('distributor-registration/', views.distributor_registration, name='distributor_registration'),
    path('product/<barcode>/', views.product_details_view, name='product-details'),
    path('profile/', views.profile, name='profile'),
]