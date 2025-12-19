import pytest
from app.application.use_cases.create_product import CreateProduct
from app.domain.errors import ValidationError

class FakeRepo:
    def create(self, product):
        return product

def test_create_product_invalid():
    repo = FakeRepo()
    uc = CreateProduct(repo)
    with pytest.raises(ValidationError):
        uc.execute({"name": "", "price": 10})
