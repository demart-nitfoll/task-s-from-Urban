my_dict ={}
print(type(my_dict))
def add_person():
    n = int(input('Сколько человек мы вводим в базу? '))
    for i in range(n):
        name = input('Введите имя человека:')
        birth_date = int(input('и его дату рождения: '))
        my_dict[name] = birth_date
    print(my_dict)
def search_person():
    is_it_end = False
    while is_it_end != True:
        search = input('Кого ищем? ')
        print(my_dict.get(search, 'Такого не знаем'))
        a = input('Ищем дальше?(да/нет) ')
        if a == 'нет':
            is_it_end = True
    is_it_end = False
def remove_person():
    is_it_end = False
    while is_it_end != True:
        search = input('Кого убрать? ')
        print(my_dict.get(search, 'Такого не знаем'))
        my_dict.pop(search)
        a = input('Убираем дальше?(да/нет) ')
        if a == 'нет':
            is_it_end = True
    is_it_end = False
#add_person()
#search_person()
#add_person()
#remove_person()
#print(my_dict)
my_set = {1,2,2,2,3,'da',1,3,'net','da'}
print(my_set)
my_set.add(input('Добавьте в это множество пару уникальных элементов, 1: '))
my_set.add(input('и 2: '))
my_set.discard(int(input('А теперь уберите какое-нибудь число из множества. Что убрать? ')))
print(my_set)
