print('Привет!Эта программа поможет тебе решать квадратные уравнения через дисриминант!')
m = input()
x = input()
from math import *
if m == 'Старт':
    print("ax ** 2 + bx + c = 0:")
    print("Введите коэффициенты для неизвестных:")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    
    n = b ** 2 - 4 * a * c
    print("Дискриминант D = %.2f" % n)
    
    if n > 0:
        x1 = (-b + sqrt(n)) / (2 * a)
        x2 = (-b - sqrt(n)) / (2 * a)
        print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
    elif n == 0:
        x = -b / (2 * a)
        print("x = %.2f" % x)
    else:
        print("Корней нет")
   
elif m == 'Стоп':
    print('Надеюсь эта программа была вам полезна')
    exit()
else:
    pass
