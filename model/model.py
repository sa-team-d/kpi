from typing import List
from bson import ObjectId
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, validator


# class Machine(BaseModel):
#     asset_id: str = Field(...)
#     category: Optional[str]
#     name: str = Field(...)
#     kpi_list: List['KPI'] = Field(...) 

class PyObjectId(ObjectId):
    """
    Custom ObjectId type to use with Pydantic.
    This ensures validation and serialization of ObjectId fields.
    """
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError(f"Invalid ObjectId: {v}")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string", format="objectid")

class Value(BaseModel):
    sum: Optional[float]
    avg: Optional[float]
    min: Optional[float]
    max: Optional[float]
    datetime: Optional[datetime]
    machine_id: str

class Configuration(BaseModel):
    children: List[PyObjectId] = Field(...)
    formula: Optional[str]

class KPI(BaseModel):
    name: str = Field(...)
    type: Optional[str]
    data: List['Value'] = Field(...)
    config: Configuration = Field(...)
