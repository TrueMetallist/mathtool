import sys
import math

con = range(-10000, 10000)
#1
if len(sys.argv) == 1 or sys.argv[1] == '--help':
    print('''mathtool — решение уравнений вида A*x^2 + B*x + C = 0

Использование:
    python mathtool.py                         вывод справки
    python mathtool.py --help                  вывод справки
    python mathtool.py solve                   ввод коэффициентов с клавиатуры
    python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами a, b и c в произвольном порядке

Коэффициенты A, B, C — целые числа, по модулю не превышающие 10000.
''')
    sys.exit(0)

#2
elif sys.argv[1] == 'solve' and len(sys.argv) == 8:
    if sys.argv.count('-a') == 1 and sys.argv.count('-b') == 1 and sys.argv.count('-c') == 1:
    # Приём значения первого аргумента
        if sys.argv[2] == '-a':
            if str(sys.argv[3]).isdigit() or (str(sys.argv[3])[0] == '-' and str(sys.argv[3])[1:].isdigit()):
                a = int(sys.argv[3])  
            else:
                sys.stderr.write('Недопустимый ввод')
                sys.exit(1)
        elif sys.argv[2] == '-b':
            if str(sys.argv[5]).isdigit() or (str(sys.argv[5])[0] == '-' and str(sys.argv[5])[1:].isdigit()):
                a = int(sys.argv[5])  
            else:
                sys.stderr.write('Недопустимый ввод')
                sys.exit(1)
        elif sys.argv[2] == '-c':
            if str(sys.argv[7]).isdigit() or (str(sys.argv[7])[0] == '-' and str(sys.argv[7])[1:].isdigit()):
                a = int(sys.argv[7])  
            else:
                sys.stderr.write('Недопустимый ввод')
                sys.exit(1)

    # Приём значения второго аргумента
        if sys.argv[4] == '-a':
            if str(sys.argv[3]).isdigit() or (str(sys.argv[3])[0] == '-' and str(sys.argv[3])[1:].isdigit()):
                b = int(sys.argv[3])  
            else:
                sys.stderr.write('Недопустимый ввод')
                sys.exit(1)
        elif sys.argv[4] == '-b':
            if str(sys.argv[5]).isdigit() or (str(sys.argv[5])[0] == '-' and str(sys.argv[5])[1:].isdigit()):
                b = int(sys.argv[5])  
            else:
                sys.stderr.write('Недопустимый ввод')
                sys.exit(1)
        elif sys.argv[2] == '-c':
            if str(sys.argv[7]).isdigit() or (str(sys.argv[7])[0] == '-' and str(sys.argv[7])[1:].isdigit()):
                b = int(sys.argv[7])  
            else:
                sys.stderr.write('Недопустимый ввод')
                sys.exit(1)

    # Приём значения третьего аргумента
        if sys.argv[6] == '-a':
            if str(sys.argv[3]).isdigit() or (str(sys.argv[3])[0] == '-' and str(sys.argv[3])[1:].isdigit()):
                c = int(sys.argv[3])  
            else:
                sys.stderr.write('Недопустимый ввод')
                sys.exit(1)
        elif sys.argv[6] == '-b':
            if str(sys.argv[5]).isdigit() or (str(sys.argv[5])[0] == '-' and str(sys.argv[5])[1:].isdigit()):
                c = int(sys.argv[5])  
            else:
                sys.stderr.write('Недопустимый ввод')
                sys.exit(1)
        elif sys.argv[6] == '-c':
            if str(sys.argv[7]).isdigit() or (str(sys.argv[7])[0] == '-' and str(sys.argv[7])[1:].isdigit()):
                c = int(sys.argv[7])  
            else:
                sys.stderr.write('Недопустимый ввод')
                sys.exit(1)

        
    else:
        sys.stderr.write('Недопустимый ввод')
        sys.exit(1)

else:
    sys.stderr.write('Недопустимый ввод')
    sys.exit(1)

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