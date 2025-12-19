from pydantic import BaseModel, Field, validator

class Product(BaseModel):
    id: int | None = None
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0)
