from src.plugin import controller

if __name__ == '__main__':
    name = 'Large Capacity Cutting Machine 1'
    kpi = 'working_time'
    start_date = "2024-03-01 00:00:00"
    end_date = "2024-03-10 00:00:00"
    res = controller.filterData(name, kpi, start_date, end_date)
    print(len(res))