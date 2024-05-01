"""Выбрать указанную строку"""

import pandas as pd

# Подготовка данных для датафрейма
data = {"student_id": [101, 53, 128, 3], 
        "name": ["Ulysses", "William", "Henry", "Henry"],
        "age": [13, 10, 6, 11]}

# Формирование датафрейма
students = pd.DataFrame(data)


def selectData(students: pd.DataFrame) -> pd.DataFrame:
    """Возвращает указанную строку, без поля ID"""
    return students.loc[students.student_id == 101, ['name', 'age']]


print(selectData(students))
