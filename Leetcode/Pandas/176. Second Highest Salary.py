import pandas as pd

employee = pd.DataFrame([], columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})
employee = pd.DataFrame([{'id':1, 'salary':100},
                         {'id':2, 'salary':200},
                         {'id':3, 'salary':300}])
def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sorted_salaries = employee['salary'].sort_values(ascending=False).drop_duplicates()
    return pd.DataFrame({
        'SecondHighestSalary': [None if sorted_salaries.size < 2 else sorted_salaries.iloc[1]]})

print(second_highest_salary(employee))