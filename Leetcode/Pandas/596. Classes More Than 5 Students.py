import pandas as pd
data = [['A', 'Math'], ['B', 'English'], ['C', 'Math'], ['D', 'Biology'],
        ['E', 'Math'], ['F', 'Computer'], ['G', 'Math'], ['H', 'Math'], ['I', 'Math']]
Courses = pd.DataFrame(data, columns=['student', 'class']).astype({'student':'object', 'class':'object'})

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    stats = courses.groupby(['class']).count().reset_index()
    return stats[stats['student'] >= 5][['class']]

print(find_classes(Courses))