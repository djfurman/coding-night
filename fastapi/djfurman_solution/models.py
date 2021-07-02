from typing import Optional

from pydantic import BaseModel, root_validator


class CircleArea(BaseModel):
    area: float
    radius: float


class ClientInput(BaseModel):
    diameter: Optional[float]
    radius: Optional[float]

    @root_validator
    def any_of(cls, v):
        if not any(v.values()):
            raise ValueError("One of diameter or radius is required")
        return v
