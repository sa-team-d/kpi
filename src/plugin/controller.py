from . import service
from datetime import datetime
from ..config.db import createSession


def filterData(name: str, kpi: str, start_date: str, end_date: str):
    session = createSession()
    start_date_obj = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
    end_date_obj = datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S")
    res = service.filterData(name, kpi, start_date_obj, end_date_obj, session)
    session.close()
    return res