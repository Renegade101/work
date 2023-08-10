import pandas as pd
data = [[1, 2, 3], [1, 2, 4], [1, 3, 3], [2, 1, 1], [2, 2, 1], [2, 3, 1], [2, 4, 1]]
Teacher = (pd.DataFrame(data, columns=['teacher_id', 'subject_id', 'dept_id']).
           astype({'teacher_id':'Int64', 'subject_id':'Int64', 'dept_id':'Int64'}))

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    df = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index()
    df.columns = ['teacher_id', 'cnt']
    return df

print(count_unique_subjects(Teacher))