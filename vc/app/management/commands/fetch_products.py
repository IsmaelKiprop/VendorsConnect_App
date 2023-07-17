from django.core.management.base import BaseCommand
import requests
import json
from app.models import Product

# Your Open Food Facts API key
API_KEY = ' '

# API endpoint to retrieve food data
API_URL = f'https://world.openfoodfacts.org/cgi/search.pl?search_terms=food&json=1&api_key={API_KEY}'

class Command(BaseCommand):
    help = 'Fetch and store products from Open Food Facts'

    def handle(self, *args, **kwargs):
        response = requests.get(API_URL)
        data = response.json()

        # Parse and store data in the database
        for product_data in data['products']:
            # Check if the product_name field is present in the API response
            if 'product_name' in product_data:
                # Check if the product with the same product_name already exists in the database
                product_name = product_data['product_name']
                if not Product.objects.filter(product_name=product_name).exists():
                    # Create a new Product instance and set its fields from the API response
                    product = Product(
                        product_name=product_name,
                        generic_name=product_data.get('generic_name', ''),
                        categories=product_data.get('categories', ''),
                        brands=product_data.get('brands', ''),
                        countries=product_data.get('countries', ''),
                        ingredients_text=product_data.get('ingredients_text', ''),
                        serving_size=product_data.get('serving_size', ''),
                        nutrition_grades=product_data.get('nutrition_grades', ''),
                        image_url=product_data.get('image_url', ''),
                        energy_kcal=float(product_data.get('energy-kcal_100g', 0.0)),
                        fat_100g=float(product_data.get('fat_100g', 0.0)),
                        saturated_fat_100g=float(product_data.get('saturated-fat_100g', 0.0)),
                        carbohydrates_100g=float(product_data.get('carbohydrates_100g', 0.0)),
                        sugars_100g=float(product_data.get('sugars_100g', 0.0)),
                        fiber_100g=float(product_data.get('fiber_100g', 0.0)),
                        proteins_100g=float(product_data.get('proteins_100g', 0.0)),
                        salt_100g=float(product_data.get('salt_100g', 0.0)),
                        additives_tags=json.dumps(product_data.get('additives_tags', [])),
                        allergens_tags=json.dumps(product_data.get('allergens_tags', [])),
                        packaging=json.dumps(product_data.get('packaging', [])),
                        labels_tags=json.dumps(product_data.get('labels_tags', [])),
                    )
                    # Save the product in the database
                    product.save()

        self.stdout.write(self.style.SUCCESS('Products fetched and stored successfully.'))
