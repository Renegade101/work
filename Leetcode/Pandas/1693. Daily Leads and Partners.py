import pandas as pd
data = [['2020-12-8', 'toyota', 0, 1], ['2020-12-8', 'toyota', 1, 0], ['2020-12-8', 'toyota', 1, 2],
        ['2020-12-7', 'toyota', 0, 2], ['2020-12-7', 'toyota', 0, 1], ['2020-12-8', 'honda', 1, 2],
        ['2020-12-8', 'honda', 2, 1], ['2020-12-7', 'honda', 0, 1], ['2020-12-7', 'honda', 1, 2],
        ['2020-12-7', 'honda', 2, 1]]
DailySales = (pd.DataFrame(data, columns=['date_id', 'make_name', 'lead_id', 'partner_id']).
              astype({'date_id':'datetime64[ns]', 'make_name':'object', 'lead_id':'Int64', 'partner_id':'Int64'}))

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    return daily_sales.groupby(
        ['date_id', 'make_name']
    ).nunique().reset_index().rename(columns={
        'lead_id': 'unique_leads',
        'partner_id': 'unique_partners',
    })

print(daily_leads_and_partners(DailySales))