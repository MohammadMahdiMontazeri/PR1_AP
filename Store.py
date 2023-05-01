import WMS
import LS
import ORS
import AMS
import pandas as pd
import os
import time
import sys
from tqdm import trange
cwd = os.getcwd()

class OnlineShop():

    def __init__(self):
        self.warehouse = WMS.WarehouseManagmentSystem()
        self.accountin = AMS.AccountingManagementSystem()
        self.logistics = LS.LogisticsSystem()
        self.order_registration = ORS.OrderRegistrationSystem()

store = OnlineShop()
store.warehouse.new_warehouse()


def start():
    print('1.Seller\n2.Customer\n')
    ne = input()
    print('__________________________________________________________________')
    if ne == '1':
        return seller()
    elif ne == '2':
        store.warehouse.total_stock_data()
        return customer()
    
def seller():
    print('1.Create a new warehouse\n2.Add product\n3.Update the warehouse\n4.Warehouse status\n5.The state of the accounting system\ns.start')
    ne = input()


    if ne == '1':
        store.warehouse.new_warehouse()
        print('__________________________________________________________________')
        print('A new warehouse created.\n')
        print('__________________________________________________________________')
        return seller()
    
    elif ne == '2':
        print('__________________________________________________________________')
        return add_product()
        
    elif ne == '3':
        print('__________________________________________________________________')
        return choose1()
    
    elif ne == '4':
        print('__________________________________________________________________')
        return choose2()

    elif ne == '5':
        print('__________________________________________________________________')
        pass
    
    elif ne == 's':
        print('__________________________________________________________________')
        return start()

def add_product():
    ware_number = int(input('Please enter the warehouse number.\n'))
    if store.warehouse.check_warehouse_number(ware_number):
        no = input('Please enter the product ID.\n')
        stock = int(input('Please enter the product stock.\n'))
        price = int(input('Please enter the price of the product.\n'))
        store.warehouse.add_product(ware_number , no , stock , price)
        print('Product added successfully.\n')
        print('__________________________________________________________________')

        return seller()
    else:
        print('warehouse number is incorrect.\n')
        print('__________________________________________________________________')

        return add_product()
    
def choose1():
    nx = input('1.Update with file location\n2.Update manually\nb.back\ns.start\n')  
    print('__________________________________________________________________')

    if nx == '1':
        return file_locations()
    
    if nx == '2':
        return update_manuall()
    
    elif nx == 'b':
        return seller()
    
    elif nx == 's':
        return start()
    
def file_locations():
    ware_number = int(input('Please enter the warehouse number.\n'))
    if store.warehouse.check_warehouse_number(ware_number):
        file_location = input('Please enter the file location\n')
        store.warehouse.update_warehouse(ware_number , file_location)
        print(f'Warehouse number {ware_number} updated.\n')
        print('__________________________________________________________________')

        return choose1()
    else:
        print('warehouse number is incorrect.\n')
        print('__________________________________________________________________')

        return file_locations()

def update_manuall():
    warehouse_number , no , stock = input('Please enter the information in the format below.\nWarehouse number:ID:stock\n').split(':')
    warehouse_number = int(warehouse_number)
    stock = int(stock)
    if store.warehouse.check_warehouse_number(warehouse_number):
        store.warehouse.update_warehouse_manual(warehouse_number , no , stock)
        print(f'Warehouse number {warehouse_number} updated.\n')
        print('__________________________________________________________________')

        return choose1()
    else:
        print('warehouse number is incorrect.\n')
        print('__________________________________________________________________')

        return update_manuall() 
    
def choose2():
    nx = input('1.csv\n2.txt\nb.back\ns.start\n')  

    if nx == '1':
        return csv()
    
    elif nx == '2':
        return txt()
    
    elif nx == 'b':
        print('__________________________________________________________________')
        return seller()
    
    elif nx == 's':
        print('__________________________________________________________________')
        return start()

def csv():
    print('__________________________________________________________________')
    file_locationl = input('Please enter the file location\n')
    print('__________________________________________________________________')

    store.warehouse.warehouse_status('csv' , file_locationl)
    print('The warehouse status was saved as csv\n')
    print('__________________________________________________________________')

    return choose2()

def txt():
    print('__________________________________________________________________')
    file_locationl = input('Please enter the file location\n')
    print('__________________________________________________________________')

    store.warehouse.warehouse_status('txt' , file_locationl)
    print('The warehouse status was saved as txt\n')
    print('__________________________________________________________________')

    return choose2()

def customer():
    df = pd.read_csv(f'{cwd}/total_stock/total_stock.csv')
    df.loc[df['stock'] == 0 , 'price'] = 'unavailable'
    print(df,'\n\nPleaes enter a ID for adding to your cart\nc.cart\nf.settlement\ns.start\n')
    nc = input()
    print('__________________________________________________________________')

    if nc == 'c':
        return cart()
    
    elif nc == 'f':
        return settlement()
    
    elif nc == 's':
        return start()
    
    else:
        if store.warehouse.check_ID_is_correct(nc):
            if store.warehouse.total_stock()[nc] == 0 :
                print('Sorry, thid product is currently unavailable.\n')
                print('__________________________________________________________________')

                return customer()
            else:
                stock = int(input('How many unints do you want:\n'))
                if store.warehouse.total_stock()[nc] >= stock:
                    store.order_registration.add_to_cart(nc , str(stock))
                    print('Your cart has been updated.\n')
                    print('__________________________________________________________________')

                    return customer()
                else:
                    print('Sorry, there are not enough units in the store.\n')
                    print('__________________________________________________________________')

                    return customer()
        else:
            print('The ID you entered is incorrect, please try again.\n')
            print('__________________________________________________________________')

            return customer()

def cart():
    if len(store.order_registration.cart.keys()) != 0:
        store.order_registration.add_price_to_cart()
        store.order_registration.show_cart()
        print('b.back\nf.settlement\n')
        nw = input()
        if nw == 'b':
            print('__________________________________________________________________')
            return customer()
        
        elif nw == 'f':
            print('__________________________________________________________________')
            return final()
        
    else:
        print('Your cart is empty.\n')
        print('__________________________________________________________________')

        return customer()


print('\n')
for i in trange(20, file=sys.stdout, desc='starting'):
    time.sleep(.3)
print('\n')
time.sleep(0.5)
start()