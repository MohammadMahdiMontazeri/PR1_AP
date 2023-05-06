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
        return accounting()
    
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


    store.warehouse.warehouse_status('csv' , file_locationl)
    print('The warehouse status was saved as csv\n')
    print('__________________________________________________________________')

    return choose2()

def txt():
    print('__________________________________________________________________')
    file_locationl = input('Please enter the file location\n')


    store.warehouse.warehouse_status('txt' , file_locationl)
    print('The warehouse status was saved as txt\n')
    print('__________________________________________________________________')

    return choose2()

def accounting():
    nu = input('1.csv\n2.txt\nb.back\ns.start\n')  

    if nu == '1':
        return csv2()
    
    elif nu == '2':
        return txt2()
    
    elif nu == 'b':
        print('__________________________________________________________________')
        return seller()
    
    elif nu == 's':
        print('__________________________________________________________________')
        return start()

def csv2():
    print('__________________________________________________________________')
    file_locationl = input('Please enter the file location\n')


    store.accountin.get_successful_orders('csv' , file_locationl)
    print('The state of the accounting system was saved as csv\n')
    print('__________________________________________________________________')

    return accounting()

def txt2():
    print('__________________________________________________________________')
    file_locationl = input('Please enter the file location\n')


    store.accountin.get_successful_orders('txt' , file_locationl)
    print('The state of the accounting system was saved as txt\n')
    print('__________________________________________________________________')

    return accounting()

def customer():
    df = pd.read_csv(f'{cwd}/total_stock/total_stock.csv')
    df.loc[df['stock'] == 0 , 'price'] = 'unavailable'
    print(df,'\n\nPleaes enter an ID for adding to your cart\nc.cart\nf.settlement\ns.start\n')
    nc = input()
    print('__________________________________________________________________')

    if nc == 'c':
        return cart()
    
    elif nc == 'f':
        return final()
    
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
                if nc in store.order_registration.cart.keys():
                    if store.warehouse.total_stock()[nc] >= (stock + int(store.order_registration.cart[nc])):
                        store.order_registration.add_to_cart(nc , str(stock))
                        print('Your cart has been updated.\n')
                        print('__________________________________________________________________')

                        return customer()
                    else:
                        print('Sorry, there are not enough units in the store.\n')
                        print('__________________________________________________________________')

                        return customer()
                else:
                    if store.warehouse.total_stock()[nc] >= stock :
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
        nw = input('r.remove from cart\nf.settlement\nb.back\n')
        if nw == 'b':
            print('__________________________________________________________________')
            return customer()
        
        elif nw == 'f':
            print('__________________________________________________________________')
            return final()
        
        elif nw == 'r':
            return remove()
        
    else:
        print('Your cart is empty.\n')
        print('__________________________________________________________________')

        return customer()

def remove():
    id_remove = input('Pleaes enter an ID for removing from your cart:')
    store.order_registration.remove_from_cart(id_remove)
    print('__________________________________________________________________')
    return cart()

def final():
    if len(store.order_registration.cart.keys()) != 0:
        store.order_registration.add_price_to_cart()
        return Full_name()
    
    else:
        print('Your cart is empty.\n')
        print('__________________________________________________________________')

        return customer()

def Full_name():
    global full_name
    full_name = input('While you are in settlement you can use these keys :\no.shop\nc.cart\n\nPlease enter your full name:')
    if full_name == 'c':
        print('__________________________________________________________________')
        return cart()
    
    elif full_name == 'o':
        print('__________________________________________________________________')
        return customer()
    
    else:
        return Phone_number()

def Phone_number():
    global phone_number
    phone_number = input('Please enter your phone number:')
    if phone_number == 'c':
        print('__________________________________________________________________')
        return cart()

    elif phone_number == 'o':
        print('__________________________________________________________________')
        return customer()
    
    else:
        return City()
    
def City():
    global city
    city = input('Please enter your city:\n1.Tehran\n2.Isfahan\n3.Tabriz\n')
    if city == '1':
        global city_name
        city_name = 'Tehran'
        return tehran()
    
    elif city == '2':
        
        city_name = 'Isfahan'
        return isfahan()
    
    elif city == '3':
        
        city_name = 'Tabriz'
        return tabriz()
            
    elif city == 'c':
        print('__________________________________________________________________')
        return cart()

    elif city == 'o':
        print('__________________________________________________________________')
        return customer()  
    
    else:
        global town
        town = '8'
        return Postal_code()

def tehran():
    global town
    town = input('1.Tehran\n2.Varamin\n')
    if town == 'c':
        print('__________________________________________________________________')
        return cart()

    elif town == 'o':
        print('__________________________________________________________________')
        return customer()
    else:
        global town_name
        if town == '1':
            town_name = 'Tehran'
        elif town == '2':
            town_name = 'Varamin'
        global details
        details = input('Please enter address details:')
        return Postal_code()
    
def isfahan():
    global town
    town = input('1.Isfahan\n2.Khomeyni Shahr\n')
    if town == 'c':
        print('__________________________________________________________________')
        return cart()

    elif town == 'o':
        print('__________________________________________________________________')
        return customer()
    else:
        global town_name
        if town == '1':
            town_name = 'Isfahan'
        elif town == '2':
            town_name = 'Khomeyni Shahr'
        global details
        details = input('Please enter address details:')
        return Postal_code()
    
def tabriz():
    global town
    town = input('1.Tabriz\n2.Jolfa\n')
    if town == 'c':
        print('__________________________________________________________________')
        return cart()

    elif town == 'o':
        print('__________________________________________________________________')
        return customer()
    else:
        global town_name
        if town == '1':
            town_name = 'Tabriz'
        elif town == '2':
            town_name = 'Jolfa'
        global details
        details = input('Please enter address details:')
        return Postal_code()
    
def Postal_code():
    global postal_code
    postal_code = input('Please enter your postal code:')
    if postal_code == 'c':
        print('__________________________________________________________________')
        return cart()

    elif postal_code == 'o':
        print('__________________________________________________________________')
        return customer()

    else:
        return delivery_time()

def delivery_time():
    print('Please enter your delivery time:')
    store.logistics.delivery_time_allocation()
    global timet
    timet = input()
    if timet == 'c':
        print('__________________________________________________________________')
        return cart()

    elif timet == 'o':
        print('__________________________________________________________________')
        return customer()
    
    else:
        return Card_number()

def Card_number():

    for i in trange(10, file=sys.stdout, desc='Payment gateway'):
        time.sleep(.3)
    print('\n')
    time.sleep(0.5)
    global card_number
    card_number = input('Please enter your card number:')
    if card_number == 'c':
        print('__________________________________________________________________')
        return cart()

    elif card_number == 'o':
        print('__________________________________________________________________')
        return customer()   

    else:
        return condition()

def condition():
    
    if store.logistics.address_check(int(city) , int(town) , postal_code) == False:

        print('Your address is incorrect, please try again.')
        return City()

    if store.order_registration.check_card_number(card_number) == True:
        return successful()
    else:
        return unsuccessful()

def successful():

    rand = store.order_registration.generate_random_number()
    store.order_registration.successful_confirmation_and_factor(full_name,city_name,town_name , details ,store.logistics._time(int(timet)),store.logistics.post_or_courier(int(city)),rand ,card_number)
    
    for i in store.order_registration.cart.keys():
        store.warehouse.warehouse_update_after_sale(i , int(store.order_registration.cart[i]))
    
    store.logistics.update_dict(int(timet))
    store.order_registration.accounting(store.order_registration.sum_of_stock(),rand,store.order_registration.total_price(), 20000 if store.logistics.post_or_courier(int(city)) == 'courier' else 30000)
    store.order_registration.empty_cart()
    print('Your purchase was successful.')
    print('__________________________________________________________________')
    return start()

def unsuccessful():

    store.order_registration.unsuccessful_confirmation(full_name,card_number)
    store.order_registration.empty_cart()
    print('Your purchase was unsuccessful.')
    print('__________________________________________________________________')
    return start()

print('\n')
for i in trange(20, file=sys.stdout, desc='starting'):
    time.sleep(.3)
print('\n')
time.sleep(0.5)
start()