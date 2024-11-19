from . import service
from datetime import datetime
from typing import List

def filterKPI(
    name: str, 
    kpi_name: str, 
    start_date: str,
    end_date: str,
    granularity_days: int,
    granularity_op: str
):
    #try:
    start_date_obj = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
    end_date_obj = datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S")
    return service.filterKPI(name, kpi_name, start_date_obj, end_date_obj, granularity_days, granularity_op)
    #except e as Exception:
    #    print('error in filtering kpi')

def getKPIByName(
    name: str
):
    try:
        return service.getKPIByName(name)
    except:
        print('error in getting kpi')

def createKPI(
    name: str,
    formula: str
):
    try:
        service.createKPI(name, formula)
    except:
        print('error in creating kpi')