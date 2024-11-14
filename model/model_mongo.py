import uuid
from typing import List
from typing import Optional
from pydantic import BaseModel, Field

class Value(BaseModel):
    sum: Optional[float]
    avg: Optional[float]
    min: Optional[float]
    max: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                "sum": 0,
                "avg": 0,
                "min": 0,
                "max": 0
            }
        }

class Configuration(BaseModel):
    children: List['KPI'] = Field(...)
    formula: str

class KPI(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    type: str = Field(...)
    data: Value = Field(...)
    config: Configuration = Field(...)


class Machine(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    category: str = Field(...)
    name: str = Field(...)
    kpi_list: List['KPI'] = Field(...) 
        
