def custom_write(file_name: str, strings: list):
    strings_position = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        line = 1
        for i in strings:
            k = (line, file.tell())
            s = i + '\n'
            file.write(s)
            strings_position[k] = i
            line += 1
    return strings_position

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)