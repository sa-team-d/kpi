from . import repository

def avgData(name, kpi, start_date, end_date, session):
    return repository.avgData(name, kpi, start_date, end_date, session)

def minData(name, kpi, start_date, end_date, session):
    return repository.minData(name, kpi, start_date, end_date, session)

def maxData(name, kpi, start_date, end_date, session):
    return repository.maxData(name, kpi, start_date, end_date, session)

def sumData(name, kpi, start_date, end_date, session):
    return repository.sumData(name, kpi, start_date, end_date, session)