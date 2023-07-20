from django.urls import path
from . import views


app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('registration/', views.registration_page, name='registration_page'),
    path('product/<barcode>/', views.product_details_view, name='product-details'),
]