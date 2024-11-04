from model.model import Data
from sqlalchemy import func

'''
agregations
get istance kpi given class kpi

'''

def retrieveKPI(name: str):
    pass

def sumData(name, kpi, start_date, end_date, session):
    return session.query(func.sum(Data.sum)).filter(
        Data.name == name,
        Data.kpi == kpi,
        Data.time.between(start_date, end_date)
    ).scalar()
    
def avgData(name, kpi, start_date, end_date, session):
    return session.query(func.avg(Data.avg)).filter(
        Data.name == name,
        Data.kpi == kpi,
        Data.time.between(start_date, end_date)
    ).scalar()
    
def minData(name, kpi, start_date, end_date, session):
    return session.query(func.min(Data.min)).filter(
        Data.name == name,
        Data.kpi == kpi,
        Data.time.between(start_date, end_date)
    ).scalar()
    
def maxData(name, kpi, start_date, end_date, session):
    return session.query(func.max(Data.max)).filter(
        Data.name == name,
        Data.kpi == kpi,
        Data.time.between(start_date, end_date)
    ).scalar()
    
