# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# a = int(input('Enter base number'))
# b = int(input('Enter the degree'))

# def sqrt(a,b):
#     ans = a
#     if b > 1:
#         ans = ans * sqrt(a,b-1)
#     return ans
    
# ans = sqrt(a,b)
# print('We got',ans)

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

# a = int(input('Enter the number A '))
# b = int(input('Enter the number B '))

# def sum(a,b):
#     if b == 0:
#         return a
#     else: return sum(a+1,b-1)
# ans = sum(a,b)
# print('We got',ans)