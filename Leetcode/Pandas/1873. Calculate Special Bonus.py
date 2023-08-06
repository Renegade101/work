import pandas as pd

Employees = (pd.DataFrame([], columns=['employee_id', 'name', 'salary']).astype
             ({'employee_id':'int64', 'name':'object', 'salary':'int64'}))

Employees =pd.DataFrame([{'employee_id':2, 'name':'Meir', 'salary':3000},
                         {'employee_id':3, 'name':'Michael', 'salary':3800},
                         {'employee_id':7, 'name':'Addilyn', 'salary':7400},
                         {'employee_id':8, 'name':'Juan', 'salary':6100},
                         {'employee_id':9, 'name':'Kannon', 'salary':7700}])
def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # Create a new column 'bonus' with default value 0
    employees['bonus'] = 0

    # Calculate bonus based on the conditions
    employees.loc[(employees['employee_id'] % 2 != 0) &
                  (~employees['name'].str.startswith('M')), 'bonus'] = employees['salary']

    # Select only the required columns and sort the result table by employee_id in ascending order
    result_df = employees[['employee_id', 'bonus']].sort_values(by='employee_id', ascending=True)

    return result_df

print(calculate_special_bonus(Employees))