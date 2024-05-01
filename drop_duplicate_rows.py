import pandas as pd

data = {'customer_id': [1, 2, 3, 4, 5, 6], 
        'name': ["Ella", "David", "Zachary", "Alice", "Finn", "Violet"],
        'email': ["emily@example.com", "michael@example.com",
                  "sarah@example.com", "john@example.com",
                  "john@example.com", "alice@example.com"]}

customers = pd.DataFrame(data)


def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    """
    Вход: фрейм данных с дублями в поле email
    Выход: фрейм данных бех дублей в поле email

    Удаляет дубликаты в датафрейме по полю email,
    при том оставляет нетронутым первое дублируемое вхождение
    """
    return customers.drop_duplicates(subset='email', keep='first')


print(dropDuplicateEmails(customers))
