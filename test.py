from src.plugin import controller

if __name__ == '__main__':
    name = 'Large Capacity Cutting Machine 1'
    res = controller.filterData(name)
    print(len(res))