import pandas as pd

# Подготовка данных
data = {"name": ["Piper", "Grace", "Georgia", "Willow", "Finn", "Thomas"], 
        "salary": [4548, 28150, 1103, 6593, 74576, 24433]}

# Формирование фрейма данных
employees = pd.DataFrame(data)


def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    """
    Вход: Датафрейм с полями ['name', 'salary']
    Выход: Датафрейм с полями ['name', 'salary', 'bonus']

    Добавление поля bonus в датафрейм employees по условию:
        - значения поля bonus == salary * 2
    """
    employees["bonus"] = employees.salary * 2

    return employees


print(createBonusColumn(employees))
