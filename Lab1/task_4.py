users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

stat_logs = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}

stat_logs["Общее количество"] = len(users)
stat_logs["Уникальные посещения"] = len(set(users))

print(stat_logs)
