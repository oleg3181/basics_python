# Задание 4

# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.


string = input("введите несколько слов: ")
word = []
number = 1
for i in range(string.count(' ') + 1):
    word = string.split()
    if len(str(word)) <= 10:
        print(f" {number} {word[i]}")
        number += 1
    else:
        print(f" {number} {word[i][0:10]}")
        number += 1
