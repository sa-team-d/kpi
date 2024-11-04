from . import service
from datetime import datetime
from ..config.db import createSession


def filterKPI(name: str, kpi: str, start_date: str, end_date: str, op: str):
    session = createSession()
    start_date_obj = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
    end_date_obj = datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S")
    if op == 'sum':
        res = service.sumData(name, kpi, start_date_obj, end_date_obj, session)
    if op == 'avg':
        res = service.avgData(name, kpi, start_date_obj, end_date_obj, session)
    if op == 'min':
        res = service.minData(name, kpi, start_date_obj, end_date_obj, session)
    if op == 'max':
        res = service.maxData(name, kpi, start_date_obj, end_date_obj, session)
    session.close()
    return res