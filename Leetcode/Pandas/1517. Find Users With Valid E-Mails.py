import pandas as pd

Users = pd.DataFrame([], columns=['user_id', 'name', 'mail']).astype({'user_id':'int64', 'name':'object', 'mail':'object'})
Users = pd.DataFrame([{'user_id':1, 'name':'Winston', 'mail':'winston@leetcode.com'},
                      {'user_id':2, 'name':'Jonathan', 'mail':'jonathanisgreat'},
                      {'user_id':3, 'name':'Annabelle', 'mail':'bella-@leetcode.com'},
                      {'user_id':4, 'name':'Sally', 'mail':'sally.come@leetcode.com'},
                      {'user_id':5, 'name':'Marwan', 'mail':'quarz#2020@leetcode.com'},
                      {'user_id':6, 'name':'David', 'mail':'david69@gmail.com'},
                      {'user_id':7, 'name':'Shapiro', 'mail':'.shapo@leetcode.com'}])

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    # Use the str.match() method with a regex pattern to find valid emails
    valid_emails_df = users[users['mail'].str.match(r'^[A-Za-z][A-Za-z0-9_\.\-]*@leetcode(\?com)?\.com$')]

    return valid_emails_df

print(valid_emails(Users))