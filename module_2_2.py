first = int(input('Введите 1-е число: '))
second = int(input('Введите 2-е число: '))
third = int(input('Введите 3-е число: '))
print("*сложные мыслительные процессы*")
if first == second == third:
    print('3 \n именно столько из них равны')
elif first == second or first == third or third == second:
    print('2 \n именно столько из них равны')
else:
    print('0 \n именно столько из них равны')