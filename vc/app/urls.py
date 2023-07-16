from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path("", views.home),
     path('product/<barcode>/', views.product_details_view, name='product-details'),
         
]

