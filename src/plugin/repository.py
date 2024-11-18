from ..config.db import kpis_collection
from datetime import datetime
'''
agregations
get istance kpi given class kpi

'''
def retrieveKPI(name: str):
    pass

def sumData(name, kpi, start_date, end_date):
    pipeline = [
        {
            "$match": {
                "name": kpi
            }
        },
        {
            "$unwind": {
                "path": "$data"
            }
        },
        {
            "$match": {
                "data.machine_id": name,
                "data.datetime": {
                    "$gte": start_date,
                    "$lte": end_date
                }
            }
        },
        {
            "$group": {
                "_id": None,
                "documents": {
                    "$push": "$$ROOT"
                }
            }
        },
        {
            "$unwind": {
                "path": "$documents",
                "includeArrayIndex": "index"
            }
        },
        {
            "$addFields": {
                "groupIndex": {
                    "$floor": {
                        "$divide": ["$index", 2]
                    }
                }
            }
        },
        {
            "$group": {
                "_id": "$groupIndex",
                "value": {
                    "$avg": "$documents.data.avg"
                }
            }
        },
        {
            "$sort": {
                "_id": 1
            }
        },
        {
            "$project": {
                "_id": 0,
                "value": 1
            }
        }
    ]
    return list(kpis_collection.aggregate(pipeline))
    
def avgData(name, kpi, start_date, end_date):
    pass
    
def minData(name, kpi, start_date, end_date):
    pass
    
def maxData(name, kpi, start_date, end_date):
    pass
    
