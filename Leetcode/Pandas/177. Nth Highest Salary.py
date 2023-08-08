import pandas as pd

employee = (pd.DataFrame([], columns=['id', 'salary']).astype
            ({'id':'int64', 'salary':'int64'}))
employee = pd.DataFrame([{'id':1, 'salary':100},
                         {'id':2, 'salary':200},
                         {'id':3, 'salary':300}])
N = int(input())
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    unique_salaries = employee['salary'].drop_duplicates()

    # Sort the unique salaries in descending order and get the Nth highest salary
    sorted_salaries = unique_salaries.sort_values(ascending=False)

    # If N exceeds the number of unique salaries, return None
    if N > len(sorted_salaries):
        return pd.DataFrame({'Nth Highest Salary': [None]})

    # Get the Nth highest salary from the sorted salaries
    nth_highest = sorted_salaries.iloc[N - 1]

    return pd.DataFrame({'Nth Highest Salary': [nth_highest]})

print(nth_highest_salary(employee, N))