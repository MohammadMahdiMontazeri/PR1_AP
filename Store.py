import WMS
import LS
import ORS
import AMS


class OnlineShop():

    def __init__(self):
        self.warehouse = WMS.WarehouseManagmentSystem()
        self.accountin = AMS.AccountingManagementSystem()
        self.logistics = LS.LogisticsSystem()
        self.order_registration = ORS.OrderRegistrationSystem()

store = OnlineShop()
store.warehouse.new_warehouse()


def start():
    print('1.Seller\n2.Customer')
    ne = input()
    if ne == '1':
        return seller()
    elif ne == '2':
        return customer()
    
def seller():
    print('1.Create a new warehouse\n2.Add product\n3.Update the warehouse\n4.Warehouse status\n5.The state of the accounting system\n# start')
    ne = input()

    if ne == '1':
        store.warehouse.new_warehouse()
        print('A new warehouse created.\n')
        return seller()
    
    elif ne == '2':
        return add_product()
        
    elif ne == '3':
        return choose1()
    
    elif ne == '4':
        return choose2()

    elif ne == '5':
        pass
    
    elif ne == '#':
        return start()

def add_product():
    ware_number = int(input('Please enter the warehouse number.\n'))
    no = input('Please enter the product ID.\n')
    stock = int(input('Please enter the product stock.\n'))
    price = int(input('Please enter the price of the product.\n'))
    store.warehouse.add_product(ware_number , no , stock , price)
    print('Product added successfully.\n')
    return seller()

def choose1():
    nx = input('1.Update with file location\n2.Update manually\n* back\n# start\n')  

    if nx == '1':
        return file_location()
    
    if nx == '2':
        return update_manuall()
    
    elif nx == '*':
        return seller()
    
    elif nx == '#':
        return start()
    
def file_location():
    ware_number = int(input('Please enter the warehouse number.\n'))
    file_location = input('Please enter the file location\n')
    store.warehouse.update_warehouse(ware_number , file_location)
    print(f'Warehouse number {ware_number} updated.\n')
    return choose1()

def update_manuall():
    warehouse_number , no , stock = input('Please enter the information in the format below.\nWarehouse number:ID:stock\n').split(':')
    warehouse_number = int(warehouse_number)
    stock = int(stock)
    store.warehouse.update_warehouse_manual(warehouse_number , no , stock)
    print(f'Warehouse number {warehouse_number} updated.\n')
    return choose1()

def choose2():
    nx = input('1.csv\n2.txt\n* back\n# start\n')  

    if nx == '1':
        return csv()
    
    if nx == '2':
        return txt()
    
    elif nx == '*':
        return seller()
    
    elif nx == '#':
        return start()

def csv():
    store.warehouse.warehouse_status('csv')
    print('The warehouse status was saved as csv\n')
    return choose2()

def txt():
    store.warehouse.warehouse_status('txt')
    print('The warehouse status was saved as txt\n')
    return choose2()





def customer():
    pass



start()