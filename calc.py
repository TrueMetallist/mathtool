import math
import sys

def Calc(a, b, c, con):
    print('Уравнение: ', str(a), 'x^2 + ', str(b), 'x + ', str(c), ' = 0 ')
    #3
    if (a in con and b in con and c in con):

        #4
        D = (b ** 2) - (4 * a * c)

        if a == 0 and b == 0 and c == 0:
            sys.stderr.write('Нет неизвестного')
            sys.exit(1)

        elif a == 0:
            print('Линейное уравнение')
            if b == 0:
                    sys.stderr.write('Нет неизвестного')
                    sys.exit(1)
            else:
                print('x = ', c / b)
                
        elif a != 0:
                    print('Дискриминант равен ', D)
                    if b == 0:
                        print('Неполное квадратное уравнение')
                    
                    if D > 0:
                        x1 = (-b - math.sqrt(D)) / (2*a)
                        x2 = (-b + math.sqrt(D)) / (2*a)
                        print('x1 = ', '{:4.2f}'.format(x1), 'x2 = ', '{:4.2f}'.format(x2))
                    
                    elif D == 0:
                        x1 = b /(2*a)
                        print('x = ', '{:4.2f}'.format(x1))
                    elif D < 0:
                        print('Нет действительных корней')
        sys.exit(0)
    else:
        sys.stderr.write('Выход за рамки диапозона')
        sys.exit(1)