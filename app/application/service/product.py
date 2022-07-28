from app.domain.entity import Product


def create_product(product_name=str):
    product = Product(name=product_name)
    return product
