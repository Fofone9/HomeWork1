# Павлов Александр Анатольевич
# Вариант 3
# Создайте рекурсивную функцию recursive_func(text), которая будет выводить символы передаваемой ей строки на экран через пробел.

def recursive_func(text):
    if len(text)>0:
        print(text[0], end=' ')
        recursive_func(text[1:])

text = "trikolor"
recursive_func(text)
