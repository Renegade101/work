import pandas as pd

Users = pd.DataFrame([], columns=['user_id', 'name']).astype({'user_id':'Int64', 'name':'object'})

Users = pd.DataFrame([{'user_id':1, 'name':'aLice'},
                      {'user_id': 2, 'name': 'bOB'}                      ,
                      {'user_id': 3, 'name': 'DaNilA'}])

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.capitalize()

    # Sort the result table by user_id in ascending order
    result_df = users.sort_values(by='user_id', ascending=True)

    return result_df

print(fix_names(Users))