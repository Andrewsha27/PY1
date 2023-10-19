money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
months = 0
monthly_budget = salary + money_capital
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while spend < monthly_budget:
    months += 1
    monthly_budget = monthly_budget + salary - spend
    spend = spend + spend * increase
print("Количество месяцев, которое можно протянуть без долгов:", months)
