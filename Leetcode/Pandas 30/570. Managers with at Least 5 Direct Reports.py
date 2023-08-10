import pandas as pd

data = [[101, 'John', 'A', None], [102, 'Dan', 'A', 101], [103, 'James', 'A', 101],
        [104, 'Amy', 'A', 101], [105, 'Anne', 'A', 101], [106, 'Ron', 'B', 101]]

Employee = (pd.DataFrame(data, columns=['id', 'name', 'department', 'managerId']).
            astype({'id':'Int64', 'name':'object', 'department':'object', 'managerId':'Int64'}))

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    required_managers = (
        employee
        .groupby('managerId', as_index=False)
        .agg(reporting=('id', 'count'))
        .query('reporting >= 5')
    )['managerId']

    return employee[employee['id'].isin(required_managers)][['name']]

print(find_managers(Employee))