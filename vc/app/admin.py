from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'categories', 'brands', 'nutrition_grades']
    list_filter = ['categories', 'brands', 'nutrition_grades']
    search_fields = ['product_name', 'generic_name', 'ingredients_text']

# Register the Product model with the custom admin configuration
admin.site.register(Product, ProductAdmin)
