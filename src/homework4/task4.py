# Даны два списка чисел. Посчитайте,
# сколько различных чисел входит только в один из этих списков

list_1 = [1, 2, 3, 4, 5, 6]
list_2 = [3, 4, 5, 6, 7, 8]
print(set(list_1) ^ (set(list_2)))