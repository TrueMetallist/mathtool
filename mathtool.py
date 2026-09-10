import sys

if len(sys.argv) == 1 or sys.argv[1] == '--help':
    print('''mathtool — решение уравнений вида A*x^2 + B*x + C = 0

Использование:
    python mathtool.py                         вывод справки
    python mathtool.py --help                  вывод справки
    python mathtool.py solve                   ввод коэффициентов с клавиатуры
    python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами

Коэффициенты A, B, C — целые числа, по модулю не превышающие 10000.
''')
    sys.exit('0')

elif sys.argv[1] == 'solve' and len(sys.argv) == 2:
    a = str(input('Введите коэффициент A: '))
    if a.isdigit():
        a = int(a)
    else:
        print('Недопустимый ввод')
        sys.exit('1')
    b = str(input('Введите коэффициент B: '))
    if b.isdigit():
        b = int(b)
    else:
        print('Недопустимый ввод')
        sys.exit('1')
    c = str(input('Введите коэффициент C: '))
    if c.isdigit():
        c = int(c)
    else:
        print('Недопустимый ввод')
        sys.exit('1')
    
elif sys.argv[1] == 'solve' and len(sys.argv) == 4:
    if str(sys.argv[2]).isdigit():
        a = int(sys.argv[2])
    else:
        print('Недопустимый ввод')
        sys.exit('1')
    if str(sys.argv[3]).isdigit():
            b = int(sys.argv[3])
    else:
        print('Недопустимый ввод')
        sys.exit('1')
    if str(sys.argv[4]).isdigit():
            c = int(sys.argv[4])
    else:
        print('Недопустимый ввод')
        sys.exit('1')

else:
    print('Недопустимый ввод')
    sys.exit('1')