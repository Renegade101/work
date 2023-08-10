import pandas as pd


Customers = pd.DataFrame([], columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})
Orders = pd.DataFrame([], columns=['id', 'customerId']).astype({'id':'Int64', 'customerId':'Int64'})

Customers = pd.DataFrame([{'id':1, 'name':'Joe'},
                          {'id':2, 'name':'Henry'},
                          {'id':3, 'name':'Sam'},
                          {'id':4, 'name':'Max'}])

Orders = pd.DataFrame([{'id':1, 'customerId':3},
                       {'id':2, 'customerId':1}])

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Select the rows which `id` is not present in orders['customerId'].
    df = customers[~customers['id'].isin(orders['customerId'])]

    # Build a dataframe that only contains the column `name`
    # and rename the column `name` as `Customers`.
    df = df[['name']].rename(columns={'name': 'Customers'})
    return df
print(find_customers(Customers, Orders))