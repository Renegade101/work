import pandas as pd
Store = (pd.DataFrame([], columns=['bill_id', 'customer_id', 'amount']).
         astype({'bill_id':'int64', 'customer_id':'int64', 'amount':'int64'}))

Store = pd.DataFrame([{'bill_id':6, 'customer_id':1, 'amount':549},
                      {'bill_id':8, 'customer_id':1, 'amount':834},
                      {'bill_id': 4, 'customer_id': 2, 'amount': 394},
                      {'bill_id': 11, 'customer_id': 3, 'amount': 657},
                      {'bill_id': 13, 'customer_id': 3, 'amount': 257}])

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    df = store[store.amount > 500]
    rich_count = df['customer_id'].nunique()
    result_df = pd.DataFrame({'rich_count':[rich_count]})
    return result_df

print(count_rich_customers(Store))