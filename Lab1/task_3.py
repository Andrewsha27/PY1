list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

number_of_players = len(list_players)
border_of_teams = round(number_of_players / 2)

team1 = list_players[:border_of_teams]
team2 = list_players[border_of_teams:]

print(team1)
print(team2)
