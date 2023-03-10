# Задача №2:
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
#  а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# Пример:
# 4 4 -> 2 2
# 5 6 -> 2 3
from math import sqrt
s = int(input('Введите сумму загаданных чисел: '))
p = int(input('Введите произведение загаданных чисел: '))


#с помощью системы  уравнений у нас получилось 2 выражения:
# y = s - x
# x**2 - s*x + p = 0 (a*x**2 - b*x + c = 0)
# y = (-b + sqrt(d))/2*a
a = 1
b = -s
c = p

d = ((-b)**2 - 4*a*c) #дискриминант

if d == 0:
    x = -b/2*a
elif d > 0:
    x = (-b + sqrt(d))/2*a

y = s - x
print(f'Загаданные числа {int(x)} {int(y)}')
