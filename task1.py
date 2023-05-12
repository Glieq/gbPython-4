# Задача 22: Даны два неупорядоченных набора целых чисел(может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

start_two_numbers = [int(x) for x in input().split()]
n = start_two_numbers[0]
m = start_two_numbers[1]
set_1 = set()
set_2 = set()
list_1 = list()
a = [int(x) for x in input().split()]
s = set(a)
for i in s:
    set_1.add(i)
b = [int(x) for x in input().split()]
s1 = set(b)
for i in s1:
    set_2.add(i)
mn_res = set_1 & set_2
total = list(mn_res)
total.sort()
for i in total:
    print(i, end=' ')
