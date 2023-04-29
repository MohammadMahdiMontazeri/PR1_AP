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
            p = ''
            for i in cart.keys():
                p += str(i)+ ' : ' + str(cart[i]) * 1 + '\n'
            file = open(factor_path,'w')
            file.write(f'product id : price\n{p}Your addres is : {addres}.Name : {full_name}.Delivery time :{timee}.Your delivery type is : {delivery_type}')
            file.close()

        else:
            for file in os.listdir(f'{cwd}/ors/confirmation/unsuccessful'):
                if file.endswith('.txt'):
                    n += 1
            file_path1 = f'{cwd}/ors/confirmation/unsuccessful/confirmation{n}.txt'
            file = open(file_path1,'w')
            file.write(f'Card number : {card_number}.The order registration was not successful.Name : {full_name}')
            file.close()