import pandas as pd
import random 
import os
import time
cwd = os.getcwd()
cart = {}

class OrderRegistrationSystem:
    def add_to_cart(self,no,amount):
        cart.update({no : amount})

    def remove_from_cart(self,no):
        if no in cart.keys():
            if cart[no] >= 1:
                cart[no] -= 1

    def add_price_to_cart(self): 
        df = pd.read_csv(f'{cwd}/total_stock/total_stock.csv')
        my_dict = df.to_dict()
        # print(df)
        cart_with_price = {}
        for i in df.loc[:, 'id']:
            for j in df.loc[:, 'price']:
                cart_with_price.update({i : j})
        cart2 = {k : [cart.get(k),cart_with_price.get(k)] for k in cart.keys() | cart_with_price.keys()}
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
        
        
    def confirmation_and_factor(self,card_number , full_name, addres  ,phone_number ,timee , delivery_type):
        n = 0
        m = 0
        if len(card_number) == 16 and card_number.isdigit():
            rand = random.randint(10**10, 10**11 - 1)
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
            file.write(f'\n{cart}\n\nYour addres is : {addres}.\nName : {full_name}.\nDelivery time :{timee}.\nYour delivery type is : {delivery_type}')
            file.close()

        else:
            for file in os.listdir(f'{cwd}/ors/confirmation/unsuccessful'):
                if file.endswith('.txt'):
                    n += 1
            file_path1 = f'{cwd}/ors/confirmation/unsuccessful/confirmation{n}.txt'
            file = open(file_path1,'w')
            file.write(f'Card number : {card_number}.The order registration was not successful.Name : {full_name}')
            file.close()