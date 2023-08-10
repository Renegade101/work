import pandas as pd

data = [[1, 'Alice'], [2, 'Bob'], [13, 'John'], [6, 'Alex']]
Students = (pd.DataFrame(data, columns=['student_id', 'student_name']).
            astype({'student_id':'Int64', 'student_name':'object'}))
data = [['Math'], ['Physics'], ['Programming']]
Subjects = pd.DataFrame(data, columns=['subject_name']).astype({'subject_name':'object'})
data = [[1, 'Math'], [1, 'Physics'], [1, 'Programming'], [2, 'Programming'], [1, 'Physics'],
        [1, 'Math'], [13, 'Math'], [13, 'Programming'], [13, 'Physics'], [2, 'Math'], [1, 'Math']]
Examinations = (pd.DataFrame(data, columns=['student_id', 'subject_name']).
                astype({'student_id':'Int64', 'subject_name':'object'}))

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    examinations = examinations.groupby(['student_id', 'subject_name'])
    examinations = examinations.agg(attended_exams=('subject_name', 'count')).reset_index()
    df = pd.merge(students, subjects, how = 'cross')
    df = df.sort_values(by = ['student_id' , 'subject_name'])
    df = pd.merge( df, examinations, how = 'left', on = ['student_id', 'subject_name'])
    df = df.fillna(0)
    return df[['student_id', 'student_name', 'subject_name', 'attended_exams']]

print(students_and_examinations(Students, Subjects,Examinations))