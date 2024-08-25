completed_tasks = int(input('Количество выполненных ДЗ: '))
hours = float(input('Количество затраченных часов: '))
course = input('Название курса: ')
time_per_task = hours / completed_tasks
print('Курс: ', course, ', всего задач: ', completed_tasks, ', затрачено часов: ', hours, ', среднее время выполнения ', time_per_task,'часа.')