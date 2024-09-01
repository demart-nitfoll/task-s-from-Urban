def calc_pass(n):
    result = ''
    for i in range(1,n):
        for j in range(1,n):
            if ((i + j) == n or n % (i + j) == 0) and (f'{i}+{j}' not in result and f'{j}+{i}' not in result) and i != j:
                result += str(i) + '+' + str(j) + ' '
    result = result.replace("+","")
    result = result.replace(" ", "")
    return result

print('Привет, я "супер-умный алгоритм", чтобы не дать тебе умереть в ловушках типа 42\nБлиже к твоему выживанию,')
is_end = False
while is_end != True:
    f_pan = input('что на первой панели?: ')
    if f_pan == 'ничего':
        print('Ну что ж.. Вы достали не тот прибор.\nЖелаю удачи, или в крайнем случае безболезненной смерти.\nНадеюсь вы не в ловушке типа 56')
        is_end = True
    else:
        print(f'Введите во вторую панель это:\n{calc_pass(int(f_pan))}')
