import sys
import math

if len(sys.argv) == 1 or sys.argv[1] == '--help':
    print('''mathtool — решение уравнений вида A*x^2 + B*x + C = 0

Использование:
    python mathtool.py                         вывод справки
    python mathtool.py --help                  вывод справки
    python mathtool.py solve                   ввод коэффициентов с клавиатуры
    python mathtool.py solve 1 -3 2   решение с заданными коэффициентами

Коэффициенты A, B, C — целые числа, по модулю не превышающие 10000.
''')
    sys.exit('0')

elif sys.argv[1] == 'solve' and len(sys.argv) == 2:
    a = str(input('Введите коэффициент A: '))
    if a.isdigit() or (a[0] == '-' and a[1:].isdigit()):
        a = int(a)
    else:
        print('Недопустимый ввод')
        sys.exit('1')
    b = str(input('Введите коэффициент B: '))
    if b.isdigit() or (b[0] == '-' and b[1:].isdigit()):
        b = int(b)
    else:
        print('Недопустимый ввод')
        sys.exit('1')
    c = str(input('Введите коэффициент C: '))
    if c.isdigit() or (c[0] == '-' and c[1:].isdigit()):
        c = int(c)
    else:
        print('Недопустимый ввод')
        sys.exit('1')
    
elif sys.argv[1] == 'solve' and len(sys.argv) == 5:
    if str(sys.argv[2]).isdigit() or (str(sys.argv[2])[0] == '-' and str(sys.argv[2])[1:].isdigit()):
        a = int(sys.argv[2])
    else:
        print('Недопустимый ввод')
        sys.exit('1')
    if str(sys.argv[3]).isdigit() or (str(sys.argv[3])[0] == '-' and str(sys.argv[3])[1:].isdigit()):
            b = int(sys.argv[3])
    else:
        print('Недопустимый ввод')
        sys.exit('1')
    if str(sys.argv[4]).isdigit() or (str(sys.argv[4])[0] == '-' and str(sys.argv[4])[1:].isdigit()):
            c = int(sys.argv[4])
    else:
        print('Недопустимый ввод')
        sys.exit('1')

else:
    print('Недопустимый ввод')
    sys.exit('1')

if (a >=-10000 and a <= 10000) and (b >=-10000 and b <= 10000) and (c >=-10000 and c <= 10000):
    D = (b ** 2) - (4 * a * c)
    print('Дискриминант равен ', D)
    if a == 0 and b == 0 and c == 0:
        print('x - любое число')
            # При a = 0
    elif a == 0:
        print('Линейное уравнение')
        if b == 0:
                print('Недопустимый ввод')
                sys.exit('1')
        else:
            print('x = ', c / b)
    elif a != 0:
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
    sys.exit('0')
else:
    print('Выход за рамки диапозона')
    sys.exit('1')