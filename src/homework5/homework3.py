# Task4: Дан список чисел. Посчитайте, сколько в нем пар элементов,
# равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать.

def task4():
    list_1 = [1, 2, 3, 3, 4, 5, 6, 6, 4, 5, 1]
    len_l = len(list_1)
    container = 0
    for i in range(len_l):
        for j in range(i + 1, len_l):
            if list_1[i] == list_1[j]:
                container += 1
    return container


# Task5: Дан список. Выведите те его элементы, которые встречаются
# в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются
# в списке.

def task5():
    list_ = ['a', 'b', 'c', 'd', 'b', 'c', 'd', 'c', 'f', 5]
    result = []

    for i in range(len(list_)):
        if list_.count(list_[i]) == 1:
            result.append(list_[i])

    return result


# Task6: Дан список целых чисел. Требуется переместить все ненулевые
# элементы в левую часть списка,
# не меняя их порядок, а все нули - в правую часть. Порядок ненулевых
# элементов изменять нельзя,
# дополнительный список использовать нельзя, задачу нужно выполнить за
# один проход по списку.
# Распечатайте полученный список.


def task6():
    list1 = [1, 0, 2, 0, 10, 33, 0, 1]

    for i in range(len(list1)):
        if list1[i] == 0:
            list1.append(list1[i])
            del list1[i]

    return list1
