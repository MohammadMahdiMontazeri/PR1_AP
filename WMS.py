import pandas as pd
import os
cwd = os.getcwd()

class WarehouseManagmentSystem:

    def warehouse_update_after_sale(self , no , amount):

        def dict_for_a_id(no):

            def warehouse_to_dict():

                list_of_dicts = []
                for file in os.listdir(f'{cwd}/warehouse_data/'):
                    if file.endswith('.csv'):
                        df = pd.read_csv(os.path.join(f'{cwd}/warehouse_data/',file))[['id','stock']]
                        warehouse_number = file[9:-4]   
                        d = df.set_index('id').to_dict(orient='index')
                        d = {k: list(v.values()) for k, v in d.items()}
                        d2 = {k: int(''.join(map(str, v))) for k, v in d.items()}
                        d2['warehouse_id'] = int(warehouse_number)
                        list_of_dicts.append(d2)

                return list_of_dicts

            _dict = {}
            for i in range(len(warehouse_to_dict())):

                if no in list(warehouse_to_dict()[i].keys()):
                    _dict[warehouse_to_dict()[i]['warehouse_id']] = warehouse_to_dict()[i][no]

                else:
                    _dict[warehouse_to_dict()[i]['warehouse_id']] = 0

            return _dict

        def decreasing_from_warehouse(warehouse_number , no , amount):

            warehouse_name = f'warehouse{warehouse_number}'     
            df = pd.read_csv(f'{cwd}/warehouse_data/{warehouse_name}.csv')[['id','stock']]
            dfp = pd.read_csv(f'{cwd}/warehouse_data/{warehouse_name}.csv')[['price']]
            d = df.set_index('id').to_dict(orient='index')
            d = {k: list(v.values()) for k, v in d.items()}
            d2 = {k: int(''.join(map(str, v))) for k, v in d.items()}

            d2[no] -= amount

            d2 = pd.DataFrame.from_dict(d2, orient='index', columns = ['stock'])
            d2.index.name = 'id'

            d2.to_csv(f'{cwd}/warehouse_data/{warehouse_name}.csv')
            d3 = pd.read_csv(f'{cwd}/warehouse_data/{warehouse_name}.csv')
            d3 = pd.concat([d3,dfp] , axis = 1)
            d3.to_csv(f'{cwd}/warehouse_data/{warehouse_name}.csv',columns=['id','stock','price'],index=False)
            

            setattr(WarehouseManagmentSystem, warehouse_name, pd.read_csv(f'{cwd}/warehouse_data/{warehouse_name}.csv'))


        warehouse_number = 0

        for i in dict_for_a_id(no).keys():
            if amount <= dict_for_a_id(no)[i]:
                warehouse_number = i
                break

        if warehouse_number != 0:
            decreasing_from_warehouse(warehouse_number , no , amount)

        else:
            for i in dict_for_a_id(no).keys():
                if dict_for_a_id(no)[i] != 0:
                    if amount > dict_for_a_id(no)[i]:
                        amount -= dict_for_a_id(no)[i]
                        decreasing_from_warehouse(i , no , dict_for_a_id(no)[i])
                        continue
                        
                    else:
                        decreasing_from_warehouse(i , no , amount)
                        break

    def new_warehouse(self):
        n = 1
        for file in os.listdir(f'{cwd}/warehouse_data/'):
            if file.endswith('.csv'):
                n += 1
        warehouse_name = f'warehouse{n}'
        df = pd.DataFrame({'id':[],'stock': [],'price': []})
        df.to_csv(f'{cwd}/warehouse_data/{warehouse_name}.csv' , index = False)

        setattr(WarehouseManagmentSystem, warehouse_name, pd.read_csv(f'{cwd}/warehouse_data/{warehouse_name}.csv'))

    def add_product(self, warehouse_number , no : str , stock : int , price : int):
        warehouse_name = f'warehouse{warehouse_number}'
        df = pd.read_csv(f'{cwd}/warehouse_data/{warehouse_name}.csv')
        dfn = pd.DataFrame({'id':[no],'stock': [stock] , 'price' : [price]})
        df = pd.concat([dfn , df])
        df.to_csv(f'{cwd}/warehouse_data/{warehouse_name}.csv' , index = False)
        
        setattr(WarehouseManagmentSystem, warehouse_name, pd.read_csv(f'{cwd}/warehouse_data/{warehouse_name}.csv'))

    def update_warehouse(self, warehouse_number , file_location):
        f = file_location.split('.')

        if f[-1] == 'txt' :
            df = pd.read_csv(file_location , sep=':')

        elif f[-1] == 'csv' :
            df = pd.read_csv(file_location)
        
        warehouse_name = f'warehouse{warehouse_number}'     
        ware_old = pd.read_csv(f'{cwd}/warehouse_data/{warehouse_name}.csv')[['id','stock']]
        ware_old2 = pd.read_csv(f'{cwd}/warehouse_data/{warehouse_name}.csv')[['price']]
        
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
        
        ware_new.to_csv(f'{cwd}/warehouse_data/{warehouse_name}.csv')
        ware_new2 = pd.read_csv(f'{cwd}/warehouse_data/{warehouse_name}.csv')
        ware_new2 = pd.concat([ware_new2,ware_old2] , axis = 1)
        ware_new2.to_csv(f'{cwd}/warehouse_data/{warehouse_name}.csv',columns=['id','stock','price'],index=False)

        setattr(WarehouseManagmentSystem, warehouse_name, pd.read_csv(f'{cwd}/warehouse_data/{warehouse_name}.csv'))

    def update_warehouse_manual(self , warehouse_number , no , stock ):
        
        warehouse_name = f'warehouse{warehouse_number}'     

        df = pd.DataFrame({'id':[no],'stock': [stock]})
        ware_old = pd.read_csv(f'{cwd}/warehouse_data/{warehouse_name}.csv')[['id','stock']]
        ware_old2 = pd.read_csv(f'{cwd}/warehouse_data/{warehouse_name}.csv')[['price']]
                
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
        
        ware_new.to_csv(f'{cwd}/warehouse_data/{warehouse_name}.csv')
        ware_new2 = pd.read_csv(f'{cwd}/warehouse_data/{warehouse_name}.csv')
        ware_new2 = pd.concat([ware_new2,ware_old2] , axis = 1)
        ware_new2.to_csv(f'{cwd}/warehouse_data/{warehouse_name}.csv',columns=['id','stock','price'],index=False)

        
        setattr(WarehouseManagmentSystem, warehouse_name, pd.read_csv(f'{cwd}/warehouse_data/{warehouse_name}.csv'))

    def total_stock(self):
        
        dict_total = {}
        for file in os.listdir(f'{cwd}/warehouse_data/'):
            if file.endswith('.csv'):
                df = pd.read_csv(os.path.join(f'{cwd}/warehouse_data/',file))[['id','stock']]
                
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

        return(dict_total)
    
    def total_stock_data(self):
        
        dict_total1 = {}
        dict_total2 = {}
        for file in os.listdir(f'{cwd}/warehouse_data/'):
            if file.endswith('.csv'):
                
                df = pd.read_csv(os.path.join(f'{cwd}/warehouse_data/',file))[['id','stock']]
                dfn = pd.read_csv(os.path.join(f'{cwd}/warehouse_data/',file))[['id','price']]
                
                d = df.set_index('id').to_dict(orient='index')
                d = {k: list(v.values()) for k, v in d.items()}
                d2 = {k: int(''.join(map(str, v))) for k, v in d.items()}


                e = dfn.set_index('id').to_dict(orient='index')
                e = {k: list(v.values()) for k, v in e.items()}
                e2 = {k: int(''.join(map(str, v))) for k, v in e.items()}
                
                for i in d2.keys():
                    if i in dict_total1.keys():
                        dict_total1[i] += d2[i]
                    else:
                        dict_total1[i] = d2[i]
                        
                for i in e2.keys():
                    if i not in dict_total2.keys():
                        dict_total2[i] = e2[i]

        total_stock = pd.DataFrame.from_dict(dict_total1, orient='index', columns = ['stock'])
        total_stock.index.name = 'id'

        total_price = pd.DataFrame.from_dict(dict_total2, orient='index', columns = ['price'])
        total_price.index.name = 'id'

        merged_df = pd.merge(total_stock , total_price , on = 'id')

        merged_df.to_csv(f'{cwd}/total_stock/total_stock.csv')
    
    def warehouse_status(self , _type : str):
        
        df = pd.DataFrame({'id':[],'stock': [] , 'warehouse' : []})
        for file in os.listdir(f'{cwd}/warehouse_data/'):
            if file.endswith('.csv'):
                warehouse_number = file[9:-4]
                dfn = pd.read_csv(os.path.join(f'{cwd}/warehouse_data/',file))[['id','stock']]
                dfn['warehouse'] = warehouse_number
                df = pd.concat([dfn , df])
                
        if _type == 'csv':
            df.to_csv(f'{cwd}/warehouse_status/warehouse_status.csv' , index = False)
        elif _type == 'txt':
            df.to_csv(f'{cwd}/warehouse_status/warehouse_status.txt' , sep = '\t' ,  index = False)

    def check_ID_is_correct(self , ID):
        df = pd.read_csv(f'{cwd}/total_stock/total_stock.csv')[['id']]
        df = pd.Series(df.squeeze())
        df_list = df.tolist()
        if ID in df_list:
            return True
        else:
            return False