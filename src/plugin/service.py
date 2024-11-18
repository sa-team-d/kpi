from . import repository
from .repository import MapOps
from typing import List

def getGranularityOperation(op):
    if op == 'sum':
        return MapOps.sum
    if op == 'avg':
        return MapOps.avg
    if op == 'min':
        return MapOps.min
    if op == 'max':
        return MapOps.max
    
def filterKPI(
    name, 
    kpi,
    start_date,
    end_date,
    granularity_days,
    granularity_op
):
    granularity_op = getGranularityOperation(granularity_op)
    return repository.filterKPI(name, kpi, start_date, end_date, granularity_days, granularity_op)

def getKPIByName(name: str):
    return repository.getKPIByName(name)

def createKPI(
    name: str,
    children: List[str], 
    formula: str
):
    repository.createKPI(name, children, formula)