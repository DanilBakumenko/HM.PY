# Задача 2: Найдите сумму цифр трехзначного числа. 

# print('Enter the number whith 3 digits')
# numb = int(input())
# sum = 0
# if numb > 99 and numb < 1000:
#     while numb > 0:
#         sum = sum + numb % 10
#         numb = numb // 10
# else:
#     print('You entered a number whithout 3 digits')
# if numb == 0:
#     print(sum)


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

# print('Enter the number of Petya products')
# p = int(input())
# s = p
# k = ( p + s ) * 2
# print ( 'Petya did {} products, Sergei did {} products, Katia did {} products, together they did {} products'.format(p,s,k,p + s + k))

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

# print('Enter the number whith 6 digits')
# numb = int(input())
# sum_f = 0
# sum_s = 0
# if numb > 99999 and numb < 1000000:
#     first = numb // 1000
#     second = numb % 1000
#     while first > 0:
#         sum_f = sum_f + first % 10
#         first = first // 10
#         sum_s = sum_s + second % 10
#         second = second // 10
# else:
#     print('You entered a number whithout 6 digits')
# if sum_f == sum_s:
#     print('Congratulations! You got your lucky ticket')
# else:
#     print('Good Luck! Better luck next time (')    

# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).

print('Enter the number n')
n = int(input())
print('Enter the number m')
m = int(input())
print('Enter the number k')
k = int(input())
if k % m == 0 or k % n == 0:
    print('you can break off {} pieces'.format(k))
else:
    print('you cant break off {} pieces'.format(k))
