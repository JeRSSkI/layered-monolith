import asyncpg
from app.domain.entities import Product

class PostgresProductRepository(ProductRepository):
    def __init__(self, pool):
        self.pool = pool

    async def create(self, product: Product):
        async with self.pool.acquire() as conn:
            row = await conn.fetchrow(
                "INSERT INTO products(name, price) VALUES($1, $2) RETURNING id, name, price",
                product.name, product.price
            )
        return Product(**row)

    async def list(self):
        async with self.pool.acquire() as conn:
            rows = await conn.fetch("SELECT id, name, price FROM products")
        return [Product(**row) for row in rows]
