# Задача 10: На столе лежат n монеток. Некоторые из них лежат 
# вверх решкой, а некоторые – гербом. Определите минимальное 
# число монеток, которые нужно перевернуть, чтобы все монетки 
# были повернуты вверх одной и той же стороной. Выведите минимальное 
# количество монет, которые нужно перевернуть

# countF = 0
# countR = 0

# n = int(input("Enter quantity of coins "))

# print("Enter 0 if front side, and 1 if back side ")
# for Coincount in range(n):
#     side = int(input("Enter side of coin "))
#     if side == 0:
#         countF += 1
#     elif side == 1:
#         countR += 1
#     else:
#         print("You entered the wrong digit")

# if countF < countR :
#     print("Less face-up coins =", countF)
# elif countR < countF :
#     print("Fewer coins lying back up", countR)
# else:
#     print("Coins the same number =", countF)
        



# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P.
#  Помогите Кате отгадать задуманные Петей числа.

# s = int(input("Enter the sum of numbers "))
# p = int(input("Enter the product of numbers "))

# x = (s + ((s*s - 4*p) ** (0.5)))/2
# y = (s - ((s*s - 4*p) ** (0.5)))/2

# print("X = {}, Y = {}".format(x,y))


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.

n = int(input("Enter the number "))

k = 2

if n < 2:
    print("2 >",n)

while k <= n:
    print(k," ")
    k = k * 2