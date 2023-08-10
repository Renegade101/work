import pandas as pd

Person = pd.DataFrame([], columns=['id', 'email']).astype({'id':'Int64', 'email':'object'})

Person = pd.DataFrame([{'id':1, 'email':'john@example.com'},
                       {'id':2, 'email':'bob@example.com'},
                       {'id':3, 'email':'john@example.com'}])

def delete_duplicate_emails(person: pd.DataFrame):
    person.sort_values(by='id', inplace=True)# Sort the rows based on id (Ascending order)
    person.drop_duplicates(subset=['email'], inplace=True)        # Drop the duplicates based on email.

    return person

print(delete_duplicate_emails(Person))