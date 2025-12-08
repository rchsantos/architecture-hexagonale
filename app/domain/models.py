from pydantic import BaseModel, Field, field_validator
from uuid import uuid4


class Product(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0)


    @field_validator("name")
    @classmethod
    def name_must_not_be_blank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Product name must not be blank")
        return value

    class ConfigDict:
        frozen = True