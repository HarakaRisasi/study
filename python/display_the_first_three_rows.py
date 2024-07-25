"""
Вывести на экран первые три строчки датафрейма.
"""
import pandas as pd

# Подготовка данных
data = {"employee_id": [3, 90, 9, 60, 49, 43],
        "name": ["Bob", "Alice", "Tatiana", "Annabelle", "Jonathan",
                 "Khaled"],
        "department": ["Operation", "Sales", "Engineering",
                       "InformationTechology", "HumanResources",
                       "Administration"],
        "salary": [28675, 11096, 33805, 37678, 23793, 40454]}

# Создаю dataframe
employees = pd.DataFrame(data)


def selectFirstRows(df: pd.DataFrame) -> pd.DataFrame:
    """Возвращает первые три строки датафрейма"""
    return df.head(3)


print(selectFirstRows(employees))
