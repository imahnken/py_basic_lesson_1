income = int(input('Введите общую сумму выручки: '))
cost = int(input('Введите общую сумму затрат: '))
profit = income - cost
if profit > 0:
    print('Ваша фирма отработала с прибылью')
    print(f'Сумма прибыли за период составляет: {profit}')
    print(f'Рентабельность выручки составляет: {profit / income:.2f}')
    workers = int(input('Введите численность персонала: '))
    print(f'Прибыль на каждого сотрудника: {profit / workers:.2f}')
else:
    print('Ваша фирма отработала в убыток.')
# не стал делать различные проверки на корректность ввода
