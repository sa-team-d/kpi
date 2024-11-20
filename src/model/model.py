from typing import List
from bson import ObjectId
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic_mongo import PydanticObjectId

# class Machine(BaseModel):
#     asset_id: str = Field(...)
#     category: Optional[str]
#     name: str = Field(...)
#     kpi_list: List['KPI'] = Field(...) 


class Value(BaseModel):
    sum: Optional[float] = None
    avg: Optional[float] = None
    min: Optional[float] = None
    max: Optional[float] = None
    datetime: Optional[datetime]
    machine_id: str

class Configuration(BaseModel):
    children: List[PydanticObjectId] = Field(...)
    formula: Optional[str]

class KPI(BaseModel):
    id: PydanticObjectId = Field(alias="_id")
    name: str = Field(...)
    type: Optional[str] = None
    description: Optional[str] = None
    unite_of_measure: Optional[str] = None
    data: Optional[List['Value']] = None
    config: Configuration = Field(...)
    
class ComputedValue(BaseModel):
    value: float = Field(...)
