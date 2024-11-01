from ..config.db import createSession
from . import service

def filterData(name):
    session = createSession()
    res = service.filterData(name, session)
    session.close()
    return res