import pandas as pd
import random 
import os
import time
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
        df = pd.read_csv(f'{cwd}/total_stock/total_stock.csv')
        my_dict = df.to_dict()
        # print(df)
        cart_with_price = {}
        for i in df.loc[:, 'id']:
            for j in df.loc[:, 'price']:
                cart_with_price.update({i : j})
        cart2 = {k : [self.cart.get(k),cart_with_price.get(k)] for k in self.cart.keys() | cart_with_price.keys()}
        cart2 = {k: v for k, v in cart2.items() if v[0] != None}
        for c in cart2:
            cart2[c] = tuple(cart2[c])
        # print(cart2)
        cart_df = pd.DataFrame(cart2)
        cart_df = cart_df.transpose()
        cart_df.columns = ['Stock', 'Price']
        cart_df.index.name = 'ID'
        cart_df.to_csv(f'{cwd}/cart/cart.csv')
        df = pd.read_csv(f'{cwd}/cart/cart.csv')

    def show_cart(self):
        df = pd.read_csv(f'{cwd}/cart/cart.csv')
        df['Total unit price'] = df ['Price'] * df['Stock']
        total_price = df.loc[:, 'Total unit price'].sum()
        print(f'{df}\n\nYour total price is : {total_price}\n')
    
    def empty_cart(self):
        self.cart = {}
        df = pd.DataFrame()
        df.to_csv(f'{cwd}/cart/cart.csv')

    def generate_random_number(self):
        return random.randint(10**10, 10**11 - 1)

    def sum_of_stock(self):
        if confirmation_and_factor :
            sum_stock = sum(int(self.cart.values))
            return sum_stock

    def confirmation_and_factor(self,card_number , full_name, addres  ,phone_number ,timee , delivery_type, rnd):
        n = 0
        m = 0
        if len(card_number) == 16 and card_number.isdigit():
            for file in os.listdir(f'{cwd}/ors/confirmation/successful'):
                if file.endswith('.txt'):
                    n += 1
            file_path = f'{cwd}/ors/confirmation/successful/confirmation{n}.txt'
            file = open(file_path,'w')
            file.write(f'Card number : {card_number}.The order registration was successful.Name : {full_name}')
            file.close()

            for file in os.listdir(f'{cwd}/ors/factor'):
                if file.endswith('.txt'):
                    m += 1
            factor_path = f'{cwd}/ors/factor/factor{m}.txt'
            cart = pd.read_csv(f'{cwd}/cart/cart.csv')[['ID','Price']]
            file = open(factor_path,'w')
            file.write(f'\n{self.cart}\n\nYour addres is : {addres}.\nOrder number : {rnd}.\nName : {full_name}.\nDelivery time :{timee}.\nYour delivery type is : {delivery_type}')
            file.close()
            return True

        else:
            for file in os.listdir(f'{cwd}/ors/confirmation/unsuccessful'):
                if file.endswith('.txt'):
                    n += 1
            file_path1 = f'{cwd}/ors/confirmation/unsuccessful/confirmation{n}.txt'
            file = open(file_path1,'w')
            file.write(f'Card number : {card_number}.The order registration was not successful.Name : {full_name}')
            file.close()
    
    def total_price(self):
        df = pd.read_csv(f'{cwd}/cart/cart.csv')
        df['Total unit price'] = df ['Price'] * df['Stock']
        total_price = df.loc[:, 'Total unit price'].sum()

    def accounting(self , Stock, Order_No, Total_price, Transport_Price):
        if confirmation_and_factor == True :
            df = pd.read_csv(f'{cwd}/ams/Accounting.csv')
            dfn = pd.DataFrame({'Stock':[Stock] , 'Order No':[Order_No], 'Total price':[Total_price], 'Transport Price':[Transport_Price]})
            dfn['Tax'] = (dfn['Total price'] + dfn   ['Transport Price']) * 1.09
            df = pd.concat([df,dfn])
            df.to_csv(f'{cwd}/ams/Accounting.csv')

