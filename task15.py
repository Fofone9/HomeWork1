# Павлов Александр Анатольевич
# Вариант 3

# На вход функция more_than_five(lst) получает список из целых чисел. 
# Результатом работы функции должен стать новый список, в котором содержатся только те числа, которые больше 5 по модулю.

def more_than_five(lst):
    lst = list(filter(lambda x: x>5, lst))
    return lst


myList = [i for i in range(10)]
print(myList)
myList = more_than_five(myList)
print(myList)