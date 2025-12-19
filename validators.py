from .entities import Product
from .errors import ValidationError

def validate_product(product: Product):
    if not product.name.strip():
        raise ValidationError("Name cannot be empty")
    if product.price <= 0:
        raise ValidationError("Price must be greater than 0")
