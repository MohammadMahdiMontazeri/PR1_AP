import pandas as pd
import os

class WarehouseManagmetSystem:
    def __init__(self):
        self.warehouse1 = pd.read_csv('/Users/mohammad/Desktop/PR1_AP/warehouse_data/Warehouse1.csv')

    def new_warehouse(self):
        n = 1
        for file in os.listdir('/Users/mohammad/Desktop/PR1_AP/warehouse_data/'):
            if file.endswith('.csv'):
                n += 1
        warehouse_name = f'warehouse{n}'
        df = pd.DataFrame({'id':[],'stock': []})
        df.to_csv(f'/Users/mohammad/Desktop/PR1_AP/warehouse_data/{warehouse_name}.csv' , index = False)

        setattr(WarehouseManagmetSystem, warehouse_name, pd.read_csv(f'/Users/mohammad/Desktop/PR1_AP/warehouse_data/{warehouse_name}.csv'))

    def add_product(self, warehouse_number , no : int , stock : int):
        warehouse_name = f'warehouse{warehouse_number}'
        df = pd.read_csv(f'/Users/mohammad/Desktop/PR1_AP/warehouse_data/{warehouse_name}.csv')
        dfn = pd.DataFrame({'id':[no],'stock': [stock]})
        df = pd.concat([dfn , df])
        df.to_csv(f'/Users/mohammad/Desktop/PR1_AP/warehouse_data/{warehouse_name}.csv' , index = False)
        
        setattr(WarehouseManagmetSystem, warehouse_name, pd.read_csv(f'/Users/mohammad/Desktop/PR1_AP/warehouse_data/{warehouse_name}.csv'))

    def update_warehouse(self, warehouse_number , file_location):
        f = file_location.split('.')

        if f[-1] == 'txt' :
            df = pd.read_csv(file_location , sep=':')

        elif f[-1] == 'csv' :
            df = pd.read_csv(file_location)
        
        warehouse_name = f'warehouse{warehouse_number}'     
        ware_old = pd.read_csv(f'/Users/mohammad/Desktop/PR1_AP/warehouse_data/{warehouse_name}.csv')

        #
        
        ware_new.to_csv(f'/Users/mohammad/Desktop/PR1_AP/warehouse_data/{warehouse_name}.csv' , index = False)
        
        setattr(WarehouseManagmetSystem, warehouse_name, pd.read_csv(f'/Users/mohammad/Desktop/PR1_AP/warehouse_data/{warehouse_name}.csv'))

    def update_warehouse_manual(self , warehouse_number , no , stock):
        
        warehouse_name = f'warehouse{warehouse_number}'     

        df = pd.DataFrame({'id':[no],'stock': [stock]})
        ware_old = pd.read_csv(f'/Users/mohammad/Desktop/PR1_AP/warehouse_data/{warehouse_name}.csv')

                
        #changed the dataframe to a dictionary
        d = df.set_index('id').to_dict(orient='index')
        d = {k: list(v.values()) for k, v in d.items()}
        d2 = {k: int(''.join(map(str, v))) for k, v in d.items()}

        #changed the dataframe to a dictionary
        e = ware_old.set_index('id').to_dict(orient='index')
        e = {k: list(v.values()) for k, v in e.items()}
        e2 = {k: int(''.join(map(str, v))) for k, v in e.items()}

        ware_new = e2 | d2

        ware_new = pd.DataFrame.from_dict(ware_new, orient='index', columns = ['stock'])
        ware_new.index.name = 'id'

        ware_new.to_csv(f'/Users/mohammad/Desktop/PR1_AP/warehouse_data/{warehouse_name}.csv')
        
        setattr(WarehouseManagmetSystem, warehouse_name, pd.read_csv(f'/Users/mohammad/Desktop/PR1_AP/warehouse_data/{warehouse_name}.csv'))

    def total_stock(self):
        
        dict_total = {}
        for file in os.listdir('/Users/mohammad/Desktop/PR1_AP/warehouse_data/'):
            if file.endswith('.csv'):
                df = pd.read_csv(os.path.join('/Users/mohammad/Desktop/PR1_AP/warehouse_data/',file))
                
                d = df.set_index('id').to_dict(orient='index')
                d = {k: list(v.values()) for k, v in d.items()}
                d2 = {k: int(''.join(map(str, v))) for k, v in d.items()}
                
                for i in d2.keys():
                    if i in dict_total.keys():
                        dict_total[i] += d2[i]
                    else:
                        dict_total[i] = d2[i]

        total_stock = pd.DataFrame.from_dict(dict_total, orient='index', columns = ['stock'])
        total_stock.index.name = 'id'

        total_stock.to_csv('/Users/mohammad/Desktop/PR1_AP/total_stock/total_stock.csv')

        return(dict_total)
    