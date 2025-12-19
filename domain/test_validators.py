import pytest
from app.domain.entities import Product
from app.domain.validators import validate_product
from app.domain.errors import ValidationError

def test_empty_name():
    p = Product(id=None, name="", price=10)
    with pytest.raises(ValidationError):
        validate_product(p)

def test_negative_price():
    p = Product(id=None, name="Desk", price=-5)
    with pytest.raises(ValidationError):
        validate_product(p)
