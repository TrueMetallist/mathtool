import sys

if len(sys.argv) == 0 or sys.argv[1] == '--help':
    print('''mathtool — решение уравнений вида A*x^2 + B*x + C = 0

Использование:
    python mathtool.py                         вывод справки
    python mathtool.py --help                  вывод справки
    python mathtool.py solve                   ввод коэффициентов с клавиатуры
    python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами

Коэффициенты A, B, C — целые числа, по модулю не превышающие 10000.
''')
    sys.exit('0')

elif sys.argv[1] == '--solve' and len(sys.argv) == 1:
    a = int(input('Введите коэффициент A: '))
    b = int(input('Введите коэффициент B: '))
    c = int(input('Введите коэффициент C: '))
elif sys.argv[1] == '--solve' and len(sys.argv) == 4:
    a = int(sys.argv[2])
    b = int(sys.argv[3])
    c = int(sys.argv[4])

else:
    print('Недопустимый ввод')
    sys.exit('1')