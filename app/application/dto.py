from pydantic import BaseModel, Field


class ProductCreateDTO(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0)