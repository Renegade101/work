import pandas as pd
Products = (pd.DataFrame([], columns=['product_id', 'low_fats', 'recyclable']).astype
            ({'product_id':'int64', 'low_fats':'category', 'recyclable':'category'}))

Products = pd.DataFrame([{'product_id':0, 'low_fats':'Y', 'recyclable':'N'},
                         {'product_id':1, 'low_fats':'Y', 'recyclable':'Y'},
                         {'product_id':2, 'low_fats':'N', 'recyclable':'Y'},
                         {'product_id':3, 'low_fats':'Y', 'recyclable':'Y'},
                         {'product_id':4, 'low_fats':'N', 'recyclable':'N'}])
def find_products(products: pd.DataFrame) -> pd.DataFrame:
    df = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]

    df = df[['product_id']]

    return df

print(find_products(Products))