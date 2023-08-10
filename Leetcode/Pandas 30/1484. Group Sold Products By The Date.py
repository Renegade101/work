import pandas as pd

data = [['2020-05-30', 'Headphone'], ['2020-06-01', 'Pencil'], ['2020-06-02', 'Mask'],
        ['2020-05-30', 'Basketball'], ['2020-06-01', 'Bible'], ['2020-06-02', 'Mask'], ['2020-05-30', 'T-Shirt']]
Activities = pd.DataFrame(data, columns=['sell_date', 'product']).astype({'sell_date':'datetime64[ns]', 'product':'object'})

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities = activities.drop_duplicates().sort_values(by=['sell_date', 'product'])
    activities['products'] = activities.groupby(['sell_date'])['product'].transform(lambda x: ','.join(x))
    activities = activities[['sell_date', 'products']].drop_duplicates()
    activities['num_sold'] = activities.products.str.count(',') + 1
    return activities[['sell_date', 'num_sold', 'products']]

print(categorize_products(Activities))