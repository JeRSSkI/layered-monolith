from app.domain.entities import Product

class ProductRepository:
    def create(self, product: Product) -> Product:
        raise NotImplementedError

    def list(self) -> list[Product]:
        raise NotImplementedError
