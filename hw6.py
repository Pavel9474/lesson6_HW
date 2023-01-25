# Задача 1. Дано натуральное число N. Найдите значение 
# выражения:N + NN + NNN
# N может быть любой длины.
import random
def string_sum_number():
    number = (input("Введите число: "))
    result = int(number) + int(number+number) + int(number+number+number)
    print("Результат равен:", result)
string_sum_number()

# Задача 2. Задан массив из случайных цифр на 15 элементов. На вход подаётся 
# трёхзначное натуральное число. Напишите программу, которая определяет,
# есть в массиве 
# последовательность из трёх элементов, совпадающая с введённым числом.
def task2():
    random_values = [str(random.randint(0,9)) for _ in range(15)]
    print(random_values)
    value=(input('Введите трехзначное число: ')) #вообще можно ввести любое число
    list_from_value=list(value)
    print(list_from_value)
    value_length=len(list_from_value)
    for i in range(len(random_values)-value_length+1):
        if list_from_value == random_values[i:i+value_length]:
            result='входит'
            break
        else:
            result='не входит'
    print(result)
task2()
# Задача 3. Найдите все простые несократимые дроби, 
# лежащие между 0 и 1, знаменатель которых не превышает 11.
def task3():
    max_znam=12
    for i in range(1, max_znam):
        for j in range(1, max_znam):
            if  (i%2!=0 or j%2!=0) and (i%3!=0 or j%3!=0) and (i%5!=0 or j%5!=0) and (j%i!=0) and (i>j):
                print(f'{j}/{i}')
task3()