from threading import Thread
from time import sleep
from datetime import datetime
def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}')
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')
time_start = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end = datetime.now()
print(f'{time_end - time_start}')
time_start = datetime.now()
text_1 = Thread(target=write_words, args=(10, 'example1.txt'))
text_2 = Thread(target=write_words, args=(30, 'example2.txt'))
text_3 = Thread(target=write_words, args=(200, 'example3.txt'))
text_4 = Thread(target=write_words, args=(100, 'example4.txt'))
text_1.start()
text_2.start()
text_3.start()
text_4.start()

text_1.join()
text_2.join()
text_3.join()
text_4.join()

time_end = datetime.now()
print(f'{time_end - time_start}')