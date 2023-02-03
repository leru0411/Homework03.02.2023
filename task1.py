# Задача №1:
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.
# Пример:
# 5 -> 1 0 1 1 0

n = int(input('Введите кол-во монет: '))
if n == 1 or n == 0:
    print(0)
else:
    coins = []
    count = 0
    for _ in range(n):
        coin = input('Орел (0) или решка (1)? ')
        coins.append(coin)
        if coin == '1':
            count += 1
    
    if count < len(coins) - count:
        print(count)
    else:
        print(len(coins) - count)