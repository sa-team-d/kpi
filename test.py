from src.plugin import controller

if __name__ == '__main__':
    name = 'ast-yhccl1zjue2t'
    kpi = 'working_ratio'
    start_date = "2024-09-30 00:00:00"
    end_date = "2024-10-07 00:00:00"
    days = 7
    ops = 'sum'
    res = controller.filterKPI(name, kpi, start_date, end_date, days, ops)
    print(res)
    
    children = []
    kpi = 'working_time'
    res = controller.getKPIByName(kpi)
    children.append(res['_id'])

    kpi = 'offline_time'
    res = controller.getKPIByName(kpi)
    children.append(res['_id'])

    name = 'working_ratio'
    formula = 'working_time/offline_time'
    controller.createKPI(name, children, formula)