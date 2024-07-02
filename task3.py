# Павлов Александр Анатольевич
# Вариант 3
# Декоратор замедляющий время выполнения функции

import time

def MyDecorator(func):
    def wrapper(*args):
        time.sleep(5)
        func(*args)
    return wrapper

@MyDecorator
def BubbleSort(array):
    size = len(array)
    for i in range(size):
        for j in range(size-i-1):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]



array = [i for i in range(100, 0, -1)]
BubbleSort(array)
print(array)
