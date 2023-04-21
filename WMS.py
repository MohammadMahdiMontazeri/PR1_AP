import pandas as pd
import os

class WarehouseManagmetSystem:
    def __init__(self):
        self.warehouse1 = pd.read_csv('/Users/mohammad/Desktop/PR1_AP/data/Warehouse1.csv')

    def new_warehouse(self):
        n = 1
        for file in os.listdir('/Users/mohammad/Desktop/PR1_AP/data/'):
            if file.endswith('.csv'):
                n += 1
        warehouse_name = f'warehouse{n}'
        df = pd.DataFrame({'id':[],'name': [],'stock': []})
        df.to_csv(f'/Users/mohammad/Desktop/PR1_AP/data/{warehouse_name}.csv' , index = False)

        setattr(WarehouseManagmetSystem, warehouse_name, pd.read_csv(f'/Users/mohammad/Desktop/PR1_AP/data/{warehouse_name}.csv'))

    def add_product(self, warehouse_number , no : int , name :str , stock : int):
        warehouse_name = f'warehouse{warehouse_number}'
        df = pd.read_csv(f'/Users/mohammad/Desktop/PR1_AP/data/{warehouse_name}.csv')
        dfn = pd.DataFrame({'id':[no],'name': [name],'stock': [stock]})
        df = pd.concat([dfn , df])
        df.to_csv(f'/Users/mohammad/Desktop/PR1_AP/data/{warehouse_name}.csv' , index = False)
        
        setattr(WarehouseManagmetSystem, warehouse_name, pd.read_csv(f'/Users/mohammad/Desktop/PR1_AP/data/{warehouse_name}.csv'))

    def update_warehouse(self, warehouse_number , file_location):
        f = file_location.split('.')

        if f[-1] == 'txt' :
            df = pd.read_csv(file_location , sep=':')

        elif f[-1] == 'csv' :
            df = pd.read_csv(file_location)
        
        warehouse_name = f'warehouse{warehouse_number}'     
        ware_old = pd.read_csv(f'/Users/mohammad/Desktop/PR1_AP/data/{warehouse_name}.csv')
        


