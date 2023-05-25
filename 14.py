# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

number = int(input('Введите число: '))
two = 2
step = 0
while two**step <= number:
    print(two**step)
    step += 1