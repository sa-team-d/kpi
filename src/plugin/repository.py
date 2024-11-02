from model.model import Data

def filterData(name, kpi, start_date, end_date, session):
    return session.query(Data).filter(
        Data.name == name,
        Data.kpi == kpi,
        Data.time.between(start_date, end_date)
    ).all()
    
