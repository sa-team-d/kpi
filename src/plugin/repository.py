from ..config.db import kpis_collection
from sympy import sympify
from datetime import datetime
from typing import List

def filterKPI(
    machine_id, 
    kpi, 
    start_date, 
    end_date, 
    granularity_days, 
    granularity_op
):
    '''
    machine_id: id of the machine
    kpi: kpi name
    start_date
    end_date
    granularity_days: number of days to subaggregate data
    granularity_operation: sum, avg, min, max
    '''
    kpi_obj = getKPIByName(kpi)
    if 'data' not in kpi_obj:
        return retrieveCompositeKPI(
            machine_id, 
            kpi, 
            start_date, 
            end_date, 
            granularity_days, 
            granularity_op
        )
    else:
        return retrieveAtomicKPI(
            machine_id, 
            kpi, 
            start_date, 
            end_date, 
            granularity_days, 
            granularity_op
        )

def retrieveCompositeKPI(
    machine_id, 
    kpi, 
    start_date, 
    end_date, 
    granularity_days, 
    granularity_op
):
    kpi_obj = getKPIByName(kpi)
    children = kpi_obj['config']['children']
    formula = kpi_obj['config']['formula']
    values = []
    for child in children:
        kpi_dep = getKPIById(child)
        value = filterKPI(
            machine_id, 
            kpi_dep['name'], 
            start_date,
            end_date,
            granularity_days, 
            granularity_op
        )
        values.append({ kpi_dep['name']: value })
    value = values[0]
    key = next(iter(value.keys()))
    results = []
    for index in range(len(value[key])):
        symbol_dict = { next(iter(v.keys())): v[next(iter(v.keys()))][index]['value'] for v in values}
        parsed_expression = sympify(formula)
        result = parsed_expression.subs(symbol_dict)
        results.append({'value': result})
    return results

def retrieveAtomicKPI(
    machine_id, 
    kpi, 
    start_date, 
    end_date, 
    granularity_days, 
    granularity_op
):
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
                "data.machine_id": machine_id,
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
                        "$divide": ["$index", granularity_days]
                    }
                }
            }
        },
        {
            "$group": {
                "_id": "$groupIndex",
                "value": {
                    f"${granularity_op}": f"$documents.data.{granularity_op}"
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
    
def getKPIByName(name: str):
    return kpis_collection.find_one({"name": name})

def getKPIById(id: str):
    return kpis_collection.find_one({"_id": id})

def createKPI(
    name: str,
    children: List[str], 
    formula: str
):
    return kpis_collection.insert_one(
        {
            "name": name,
            "config": 
            {
                "children": children,
                "formula": formula
            }
        }
    )