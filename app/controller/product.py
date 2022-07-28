from app.application.service.product import create_product


def make():
    product = create_product(product_name="moni")
    return product
