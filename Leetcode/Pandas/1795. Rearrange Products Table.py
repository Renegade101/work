import pandas as pd

Product = pd.DataFrame([], columns=['product_id', 'store1', 'store2', 'store3']).astype({'product_id':'int64', 'store1':'int64', 'store2':'int64', 'store3':'int64'})
Products = pd.DataFrame([{'product_id':0, 'store1':95, 'store2':100, 'store3':105},
                         {'product_id':1, 'store1':70, 'store2':None, 'store3':80}])
def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    products = pd.melt(products, id_vars='product_id', var_name='store', value_name='price').dropna() #dropna - drops null
    #Melt function is useful to massage a DataFrame into a format where one or more columns are identifier variables (id_vars),
    #while all other columns, considered measured variables (value_vars), are “unpivoted” to the row axis,
    #leaving just two non-identifier columns, ‘variable’ and ‘value’
    return products
print(rearrange_products_table(Products))
