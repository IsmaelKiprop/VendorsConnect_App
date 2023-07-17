from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=200, default='')
    generic_name = models.TextField(blank=True, null=True)
    categories = models.TextField(blank=True, null=True)
    brands = models.CharField(max_length=100, blank=True, null=True)
    countries = models.TextField(blank=True, null=True)
    ingredients_text = models.TextField(blank=True, null=True)
    serving_size = models.CharField(max_length=50, blank=True, null=True)
    nutrition_grades = models.CharField(max_length=1, blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)

    energy_kcal = models.FloatField(blank=True, null=True)
    fat_100g = models.FloatField(blank=True, null=True)
    saturated_fat_100g = models.FloatField(blank=True, null=True)
    carbohydrates_100g = models.FloatField(blank=True, null=True)
    sugars_100g = models.FloatField(blank=True, null=True)
    fiber_100g = models.FloatField(blank=True, null=True)
    proteins_100g = models.FloatField(blank=True, null=True)
    salt_100g = models.FloatField(blank=True, null=True)

    additives_tags = models.TextField(blank=True, null=True)
    allergens_tags = models.TextField(blank=True, null=True)
    packaging = models.TextField(blank=True, null=True)
    labels_tags = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.product_name
