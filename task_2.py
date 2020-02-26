time_sec = int(input('Введите время в секундах: '))
hour_time = time_sec // 3600
min_time = (time_sec - hour_time * 3600) // 60
sec_time = time_sec - hour_time * 3600 - min_time * 60
print(f'Время в формате чч:мм:сс равно: {hour_time:02d}:{min_time:02d}:{sec_time:02d}')
