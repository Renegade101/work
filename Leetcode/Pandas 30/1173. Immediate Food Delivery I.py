import pandas as pd
Delivery = (pd.DataFrame([], columns=['delivery_id', 'customer_id', 'order_date', 'customer_pref_delivery_date']).
            astype({'delivery_id':'Int64', 'customer_id':'Int64', 'order_date':'datetime64[ns]', 'customer_pref_delivery_date':'datetime64[ns]'}))
Delivery = pd.DataFrame([{'delivery_id':1, 'customer_id':1, 'order_date':'2019-08-01', 'customer_pref_delivery_date':'2019-08-02'},
{'delivery_id':2, 'customer_id':5, 'order_date':'2019-08-02', 'customer_pref_delivery_date':'2019-08-02'},
{'delivery_id':3, 'customer_id':1, 'order_date':'2019-08-11', 'customer_pref_delivery_date':'2019-08-11'},
{'delivery_id':4, 'customer_id':3, 'order_date':'2019-08-24', 'customer_pref_delivery_date':'2019-08-26'},
{'delivery_id':5, 'customer_id':4, 'order_date':'2019-08-21', 'customer_pref_delivery_date':'2019-08-22'},
{'delivery_id':6, 'customer_id':2, 'order_date':'2019-08-11', 'customer_pref_delivery_date':'2019-08-13'}])

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    df= delivery[delivery['order_date']==delivery['customer_pref_delivery_date']]
    return pd.DataFrame([round((len(df)/len(delivery))*100,2)],columns=['immediate_percentage'])

print(food_delivery(Delivery))