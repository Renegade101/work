import pandas as pd
Patients = (pd.DataFrame([], columns=['patient_id', 'patient_name', 'conditions']).astype
            ({'patient_id':'int64', 'patient_name':'object', 'conditions':'object'}))
Patients = pd.DataFrame([{'patient_id':1, 'patient_name':'Daniel', 'conditions':'YFEV COUGH'},
                         {'patient_id':2, 'patient_name':'Alice', 'conditions':''},
                         {'patient_id':3, 'patient_name':'Bob', 'conditions':'DIAB100 MYOP'},
                         {'patient_id':4, 'patient_name':'George', 'conditions':'ACNE DIAB100'},
                         {'patient_id':5, 'patient_name':'Alain', 'conditions':'DIAB201'}])

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    df = patients[patients['conditions'].str.contains(r'\bDIAB1')]
    return df


print(find_patients(Patients))