import requests

def get_product_details(barcode):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    response = requests.get(url)

    if response.status_code == 200:
        product_data = response.json()
        return product_data

    return None


def fetch_dairy_products():
    url = "https://world.openfoodfacts.org/category/dairy-products.json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        products = data.get('products', [])
        dairy_products = []

        for product in products:
            barcode = product.get('code', '')
            image_url = product.get('image_url', '')
            name = product.get('product_name', '')

            dairy_product = {
                'barcode': barcode,
                'image_url': image_url,
                'name': name,
            }
            dairy_products.append(dairy_product)

        return dairy_products

    return []
