def add_everything_up(a, b):
    try:
        return round(a + b, 6)
    except:
        return f'{a}' + f'{b}'
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))