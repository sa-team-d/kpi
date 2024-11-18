from typing import List
from typing import Optional
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# class Machine(BaseModel):
#     asset_id: str = Field(...)
#     category: Optional[str]
#     name: str = Field(...)
#     kpi_list: List['KPI'] = Field(...) 
class Value(BaseModel):
    sum: Optional[float]
    avg: Optional[float]
    min: Optional[float]
    max: Optional[float]
    datetime: Optional[datetime]
    machine_id: str

class Configuration(BaseModel):
    children: List['KPI'] = Field(...)
    formula: Optional[str]

class KPI(BaseModel):
    name: str = Field(...)
    type: Optional[str]
    data: List['Value'] = Field(...)
    config: Configuration = Field(...)
