import uuid
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, Float, func


Base = declarative_base()
class KPI(Base):

    __tablename__ = 'kpi'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(250), nullable=False)
    children = Column(String(250), nullable=False)

class Data(Base):

    __tablename__ = 'data'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    time = Column(DateTime)
    asset_id = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    kpi = Column(String(250), nullable=False)
    sum = Column(Float, nullable=False)
    avg = Column(Float, nullable=False)
    min = Column(Float, nullable=False)
    max = Column(Float, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
   
    def __repr__(self):
        return f"<Data(id='{self.id}', name='{self.name}', kpi={self.kpi}, sum={self.sum})>"
