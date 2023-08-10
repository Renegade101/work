import pandas as pd

data = [[1, 'Alice'], [7, 'Bob'], [11, 'Meir'], [90, 'Winston'], [3, 'Jonathan']]
Employees = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'int64', 'name':'object'})
data = [[3, 1], [11, 2], [90, 3]]
EmployeeUNI = pd.DataFrame(data, columns=['id', 'unique_id']).astype({'id':'int64', 'unique_id':'int64'})


def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    df=pd.merge(employees,employee_uni,how='outer',on='id')
    return df[['unique_id','name']]

print(replace_employee_id(Employees, EmployeeUNI))