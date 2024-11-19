from . import repository
from .repository import MapOps
from typing import List
from ..config.db import kpis_collection
from sympy import sympify

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
    expr = sympify(formula)
    kpis_in_formula = {str(symbol) for symbol in expr.free_symbols}
    
    # Query MongoDB to check if these KPIs exist
    # The query will look for any documents where the 'name' field is one of the KPIs
    existing_kpis = kpis_collection.find({"name": {"$in": list(kpis_in_formula)}}, {"_id": 0, "name": 1})

    # Extract the names of the KPIs that exist in the database
    existing_kpi_names = {doc["name"] for doc in existing_kpis}
    
    # Return missing KPIs
    missing_kpis = kpis_in_formula - existing_kpi_names
    if missing_kpis:
        print(f"The following KPIs are missing from the database: {missing_kpis}")
        raise ValueError("Missing KPIs")

    repository.createKPI(name, children, formula)