
from pydantic import BaseModel, Field

class TransactionRequest(BaseModel):
    amount: float = Field(..., example=85000)
    hour: int = Field(..., example=2)
    day_of_week: int = Field(..., example=6)
    distance_from_home: float = Field(..., example=120)

