from chardet import detect

words = ['первое слово', 'сетевое программирование', 'сокет', 'декоратор']

with open('test_file.txt', 'w') as file:
    for i in words:
        file.write(i + '\n')

with open('test_file.txt', 'rb') as file:
    ENCODING = detect(file.readline())['encoding']
    print('Кодировка по умолчанию ' + ENCODING)
    data = file.read()
    data = data.decode(ENCODING)

with open('test_file.txt', 'w', encoding='utf-8') as file:
    file.write(data)

with open('test_file.txt', 'r', encoding='utf-8') as file:
    print(file.read())
    pass
