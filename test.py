from src.plugin import controller

if __name__ == '__main__':
    name = 'Large Capacity Cutting Machine 1'
    kpi = 'working_time'
    start_date = "2024-09-30 00:00:00"
    end_date = "2024-10-04 00:00:00"
    res = controller.filterKPI(name, kpi, start_date, end_date, 'max')
    print(res)