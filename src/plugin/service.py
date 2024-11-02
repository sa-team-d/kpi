from . import repository

def filterData(name, kpi, start_date, end_date, session):
    return repository.filterData(name, kpi, start_date, end_date, session)