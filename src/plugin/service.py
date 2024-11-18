from . import repository

def avgData(name, kpi, start_date, end_date):
    return repository.avgData(name, kpi, start_date, end_date)

def minData(name, kpi, start_date, end_date):
    return repository.minData(name, kpi, start_date, end_date)

def maxData(name, kpi, start_date, end_date):
    return repository.maxData(name, kpi, start_date, end_date)

def sumData(name, kpi, start_date, end_date):
    return repository.sumData(name, kpi, start_date, end_date)