import pandas as pd
import os
cwd = os.getcwd()

class AccountingManagementSystem:

    def get_successful_orders(self , _type : str, file_location):
        df = pd.read_csv(f'{cwd}/Accounting.csv')
        if _type == 'csv':
            df.to_csv(f'{file_location}/successful_orders.csv')
        elif _type == 'txt':
            df.to_csv(f'{file_location}/successful_orders.txt' , sep = '\t')
