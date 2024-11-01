from model.model import Data

def filterData(name, session):
    return session.query(Data).filter(Data.name == name).all()

def showDataById(id, session):
    return session.query(Data).filter(Data.id == id).first()

def updateDataById(id, session):
    return session.query(Data).filter(Data.id == id).first()
    
