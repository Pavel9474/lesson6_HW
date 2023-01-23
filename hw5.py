# # Задача 1. Задайте список случайных чисел от 1 до 10,
# #  выведите все элементы больше 5. Используйте для решения лямбда-функцию.
# # 2, 3, 4, 6, 7, 8 -> 6, 7, 8
import random
random_values = [random.randint(0,10) for _ in range(6)]
print(random_values)
result = print(list(filter(lambda num:num>5, random_values)))

# # Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа, 
# # описывающие случайную возрастающую последовательность. 
# # Порядок элементов менять нельзя.
# # [1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [2, 7] или [4, 6, 7] и т.д.
random_values = [random.randint(0,10) for _ in range(15)]
def random_rising_sequence(nums):
    random_rising_sequence=[]
    for i in range(len(nums)):
        if nums[i] == max(nums[:i+1:]) and nums[i] not in random_rising_sequence:
            random_rising_sequence.append(nums[i])
    return random_rising_sequence
print(random_values)
print(random_rising_sequence(random_values))
# # Задача 3. Задайте список случайных чисел от 1 до 10. 
# # Посчитайте, сколько всего совпадающих элементов есть в списке. 
# # Удалите все повторяющиеся элементы.
random_values = [random.randint(0,10) for _ in range(15)]
print(random_values)
lsit2=[]
unique_values = []
i=0
for number in random_values:
    if number not in unique_values:
        i+=1
        unique_values.append(number)
print(f'{i} элементов совпадают')
print(f'Список уникальных элементов {unique_values}')
# Задача 4*. Создайте игру в крестики-нолики.
map= [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
def print_map(w):
    for i in w:
        print(i)
print_map(map)
print(map[0][1])
game_is_on = True
while game_is_on:
    move = input("Сделайте ход введя координаты и символ (Например:[0][0] = 'X'): ")
    exec("map" + move)
    for row in map:
        print(row)
        filled_map= [map[0],map[1],map[2],
        [i[0] for i in map],[i[1] for i in map],[i[2] for i in map],
        [map[0][0], map[1][1], map[2][2]],[map[0][2], map[1][1], map[2][0]]]
    for item in filled_map:
        result = list(set(item))
        if len(result) == 1 and result[0] != " ":
            print("Game over!")
            game_is_on = False
            break
