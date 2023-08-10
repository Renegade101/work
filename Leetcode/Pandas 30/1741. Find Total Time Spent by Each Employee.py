import pandas as pd
data = [['1', '2020-11-28', '4', '32'], ['1', '2020-11-28', '55', '200'], ['1', '2020-12-3', '1', '42'], ['2', '2020-11-28', '3', '33'], ['2', '2020-12-9', '47', '74']]
Employees = (pd.DataFrame(data, columns=['emp_id', 'event_day', 'in_time', 'out_time']).
             astype({'emp_id':'Int64', 'event_day':'datetime64[ns]', 'in_time':'Int64', 'out_time':'Int64'}))
def total_time(employees: pd.DataFrame) -> pd.DataFrame:

    employees['total_time'] = employees['out_time'] - employees['in_time']
    employees = employees.groupby(['event_day', 'emp_id'], as_index=False).agg(sum)
    employees = employees.rename(columns={'event_day': 'day'})
    return employees.drop(columns=['out_time', 'in_time'])

print(total_time(Employees))