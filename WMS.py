import pandas as pd
anbar = {}
def add_or_update_product():
    a = input('Please add the merch code first and how much you want to add second like this 1044:20\n')
    a = a.split(':')
    anbar.update({int(a[0]) : int(a[1])})
def add_or_update_product_csv():
    b = input('Please insert the file location \n')
    df = pd.read_csv(b)
    for line in df.index:
        print(df.loc[line, 'code'], df.loc[line, 'amount'])
        anbar.update({df.loc[line, 'code']:df.loc[line, 'amount']})

