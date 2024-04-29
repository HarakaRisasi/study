
"""Создать фрейм данных из списка со списками чисел, 
разместить их в фреймегде будет два поля с названиями 'student_id', 'age']"""

import pandas as pd

student_data = [[1, 15], [2, 11], [3, 11], [4, 20]]

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=['student_id', 'age'])

