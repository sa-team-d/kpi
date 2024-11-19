from . import repository
from typing import List
from ..config.db import kpis_collection
from sympy import sympify

def checkValidOps(op):
    if op == 'sum':
        return True
    if op == 'avg':
        return True
    if op == 'min':
        return True
    if op == 'max':
        return True
    return False
    
def filterKPI(
    name, 
    kpi,
    start_date,
    end_date,
    granularity_days,
    granularity_op
):
    if not checkValidOps(granularity_op):
        raise Exception('Not valid op')
    return repository.filterKPI(name, kpi, start_date, end_date, granularity_days, granularity_op)

def getKPIByName(name: str):
    return repository.getKPIByName(name)

def createKPI(
    name: str,
    formula: str
):
    expr = sympify(formula)
    kpis_in_formula = {str(symbol) for symbol in expr.free_symbols}
    
    existing_kpis = kpis_collection.find({"name": {"$in": list(kpis_in_formula)}}, {"_id": 1, "name": 1})

    existing_kpi_names = set()
    children = []
    for doc in existing_kpis:
        existing_kpi_names.add(doc["name"])
        children.append(doc["_id"])

    missing_kpis = kpis_in_formula - existing_kpi_names
    if missing_kpis:
        print(f"The following KPIs are missing from the database: {missing_kpis}")
        raise ValueError("Missing KPIs")
    repository.createKPI(name, children, formula)