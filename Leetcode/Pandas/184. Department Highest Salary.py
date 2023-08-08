import pandas as pd

Employee = pd.DataFrame([{'id':1, 'name':'Joe', 'salary':70000, 'departmentId':1},
                         {'id':2, 'name':'Jim', 'salary':90000, 'departmentId':1},
                         {'id':3, 'name':'Henry', 'salary':80000, 'departmentId':2},
                         {'id':4, 'name':'Sam', 'salary':60000, 'departmentId':2},
                         {'id':5, 'name':'Max', 'salary':90000, 'departmentId':1}])

Department = pd.DataFrame([{'id':1, 'name':'IT'},
                           {'id':2, 'name':'Sales'}])

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    max_salary_per_dept = employee.groupby('departmentId')['salary'].transform('max')

    joined = employee.merge(department, how='left', left_on='departmentId', right_on='id')
    joined.rename(columns={'name_y':'Department', 'salary':'Salary', 'name_x':'Employee'}, inplace=True)
    joined = joined[joined['Salary']==max_salary_per_dept]
    return joined[['Department', 'Employee', 'Salary']]

print(department_highest_salary(Employee, Department))