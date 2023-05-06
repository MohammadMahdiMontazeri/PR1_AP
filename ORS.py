import pandas as pd
import random 
import os
cwd = os.getcwd()

class OrderRegistrationSystem:
    def __init__(self):
        self.cart = {}

    def add_to_cart(self,no,amount):
        self.cart.update({no : amount})

    def remove_from_cart(self,no):
        if no in self.cart.keys():
            if int(self.cart[no]) >= 1:
                self.cart[no] = str(int(self.cart[no]) - 1)

    def add_price_to_cart(self): 
        df = pd.read_csv(f'{cwd}/total_stock/total_stock.csv')[['id','price']]
        a = self.cart
        dfn = pd.DataFrame.from_dict(a, orient = 'index', columns = ['stock'])
        dfn.index.name = 'id'
        cart_df = pd.merge(dfn,df,on = 'id')
        cart_df.to_csv(f'{cwd}/cart/cart.csv')
        df = pd.read_csv(f'{cwd}/cart/cart.csv')

    def show_cart(self):
        df = pd.read_csv(f'{cwd}/cart/cart.csv')[['id','stock','price']]
        df['Total unit price'] = df ['price'] * df['stock']
        total_price = df.loc[:, 'Total unit price'].sum()
        print(f'{df}\n\nYour total price is : {total_price}\n')
    
    def empty_cart(self):
        self.cart = {}
        df = pd.DataFrame({'id' : [] ,'stock' : [] ,'price' : []})
        df.to_csv(f'{cwd}/cart/cart.csv')

    def generate_random_number(self):
        return random.randint(10**10, 10**11 - 1)

    def sum_of_stock(self):
        sum_stock = sum(map(int,(self.cart.values())))
        return sum_stock
        
    def check_card_number(self,card_number):
        if len(card_number) == 16 and card_number.isdigit():
            return True
        else:
            return False
        
    def successful_confirmation_and_factor(self , full_name, city_name , town_name , details  ,timet , delivery_type, rand, card_number):
        n = 0
        m = 0
        address = f'{city_name} , {town_name} , {details}' if details != '' else f'{city_name} , {town_name}'
        for file in os.listdir(f'{cwd}/ors/confirmation/successful'):
            if file.endswith('.txt'):
                n += 1
        file_path = f'{cwd}/ors/confirmation/successful/confirmation{n}.txt'
        file = open(file_path,'w')
        file.write(f'Card number : {card_number}\nThe order registration was successful\nName : {full_name}')
        file.close()

        for file in os.listdir(f'{cwd}/ors/factor'):
            if file.endswith('.txt'):
                m += 1
        factor_path = f'{cwd}/ors/factor/factor{m}.txt'
        cart = pd.read_csv(f'{cwd}/cart/cart.csv')[['id','price']]
        file = open(factor_path,'w')
        file.write(f'{cart}\n\nYour address is : {address}\nOrder number : {rand}\nName : {full_name}\nDelivery time : {timet}\nYour delivery type is : {delivery_type}')
        file.close()

    def unsuccessful_confirmation(self , full_name, card_number):
        n = 0
        for file in os.listdir(f'{cwd}/ors/confirmation/unsuccessful'):
            if file.endswith('.txt'):
                n += 1
        file_path1 = f'{cwd}/ors/confirmation/unsuccessful/confirmation{n}.txt'
        file = open(file_path1,'w')
        file.write(f'Card number : {card_number}\nThe order registration was not successful\nName : {full_name}')
        file.close()
    
    def total_price(self):
        df = pd.read_csv(f'{cwd}/cart/cart.csv')
        df['Total unit price'] = df ['price'] * df['stock']
        total_price = df.loc[:, 'Total unit price'].sum()
        return total_price

    def accounting(self , Stock, Order_No, Total_price, Transport_Price):

        df = pd.read_csv(f'{cwd}/ams/Accounting.csv')[['Stock','Order No','Total price','Transport Price','Tax']]
        dfn = pd.DataFrame({'Stock':[Stock] , 'Order No':[Order_No], 'Total price':[Total_price], 'Transport Price':[Transport_Price]})
        dfn['Tax'] = str(int((dfn['Total price'] + dfn ['Transport Price']) * 1.09))
        df = pd.concat([df,dfn])
        df.to_csv(f'{cwd}/ams/Accounting.csv')