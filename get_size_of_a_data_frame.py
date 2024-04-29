"""
Простая функция, которая принимает DataFrame из библиотеки pandas
в качестве входных данных и возвращает список,
содержащий количество строк и столбцов этого DataFrame.
"""

import pandas as pd

# Определяю данные для будущего датафрейма.
data = [
    {"player_id": [846, 749, 155, 583, 388, 883]},
    {"name": ["Manson", "Riley", "Bob", "Isabella", "Zachary", "Ava"]},
    {"age": [21, 30, 28, 32, 24, 23]},
    {"position": ["Forward", "Winger", "Striker", "Goalkeepre", "Midfielder", "Defender"]},
    {"team": ["RealMadrid", "Barcelona", "ManchesterUnited", "Liverpool", "BayerMunich", "Chelsea"]}
    ]

# Формирую датафрейм
players = pd.DataFrame(data)


def getDataframeSize(players: pd.DataFrame) -> list[int]:
    """Определяет размер кол-во строк (0) и кол-во столбцов (1)"""
    return [players.shape[0], players.shape[1]]


print(getDataframeSize(players))
