# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

# n = int(input("Enter the number of numbers in first array "))
# m = int(input("Enter the number of numbers in second array "))

# FirstArray =  [int(input()) for i in range(n)] #[1, 5, 2, 4, 3]
# SecondArray =  [int(input()) for i in range(m)] #[5, 8, 6, 7, 9]

# end = FirstArray + SecondArray

# def sortArray (x):
#     l = len(x)
#     for i in range(l):
#         for j in range(l - i - 1):
#             if x[j] > x[j+1]:
#                 temp = x[j]
#                 x[j] = x[j+1]
#                 x[j+1] = temp

# sortArray(end)
# print('These numbers are in both arrays :', end=" ")

# if end[1] == end[2]:
#     print(end[1], end=" ")

# for i in range(n + m - 1):
#     if end[i] == end[i + 1] and end[i] > end[i-1]:
#         print(end[i],end=' ')


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора 
# на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать
# за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

# n = int(input("Enter the number of bushes "))
# a =  [int(input()) for i in range(n)] #[1, 5, 2, 4, 3]
# max = 0

# for i in range(n):
#     if i == n-1:
#         if a[i] + a[0] + a[i-1] > max :
#             max = a[i] + a[0] + a[i-1]
#     else:
#         if a[i] + a[i+1] + a[i-1] > max:
#             max = a[i] + a[i+1] + a[i-1]

# print('Maximum berries can be collected is',max)       