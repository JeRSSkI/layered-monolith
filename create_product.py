from app.domain.validators import validate_product
from app.domain.entities import Product

class CreateProduct:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, dto):
        product = Product(**dto)
        validate_product(product)
        return self.repository.create(product)
