import sys
import calc
import stats
import ser
import argparse
from root import calculate as rootcalc
from ratio import calculate as ratiocalc

con = range(-10000, 10000)

#1
if len(sys.argv) == 1 or sys.argv[1] == '--help':
    print('''mathtool — решение уравнений вида A*x^2 + B*x + C = 0

Использование:
    python mathtool.py                         вывод справки
    python mathtool.py --help                  вывод справки
    python mathtool.py solve                   ввод коэффициентов с клавиатуры
    python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами a, b и c в произвольном порядке''')

    print('Коэффициенты A, B, C — целые числа, по модулю не превышающие ' + str(max(con)+1) + '.')
    sys.exit(0)

#2
elif sys.argv[1] == 'solve':
    args_dict = {}
    for i in range(len(sys.argv)):
        if sys.argv[i] == '-a':
            args_dict['A'] = sys.argv[i+1]
        elif sys.argv[i] == '-b':
            args_dict['B'] = sys.argv[i+1]
        elif sys.argv[i] == '-c':
            args_dict['C'] = sys.argv[i+1]
    
    if not all(j in args_dict for j in['A', 'B', 'C']):
        a = str(input('Введите коэффициент A: '))
        if a.isdigit() or (a[0] == '-' and a[1:].isdigit()):
            args_dict['A'] = a
        else:
            sys.stderr.write('Недопустимый ввод')
            sys.exit(1)
        b = str(input('Введите коэффициент B: '))
        if b.isdigit() or (b[0] == '-' and b[1:].isdigit()):
            args_dict['B'] = b
        else:
            sys.stderr.write('Недопустимый ввод')
            sys.exit(1)
        c = str(input('Введите коэффициент C: '))
        if c.isdigit() or (c[0] == '-' and c[1:].isdigit()):
            args_dict['C'] = c
        else:
            sys.stderr.write('Недопустимый ввод')
            sys.exit(1) 

    calc.Calc(int(args_dict['A']), int(args_dict['B']), int(args_dict['C']), con)

elif sys.argv[1] == 'stats':
    args_dict ={}
    for i in range(len(sys.argv)-1):
        if sys.argv[i] == '--input':
            args_dict['input'] = sys.argv[i+1]
    if not ('input' in args_dict):
        vvod = '0'
        with open('notinp.txt', 'w') as file:
            while vvod != '':
                vvod = input('-- ')
                if str(vvod).isdigit() or (len(str(vvod)) != 0) and (str(vvod)[0] == '-') and (str(vvod)[1:].isdigit()):
                    file.writelines(str(vvod) + '\n')
        stats.inp('notinp.txt')
        sys.exit(0)

    else:
        stats.inp(args_dict['input'])
        sys.exit(0)

elif sys.argv[1] == 'series':
    args_dict = {}
    for i in range(len(sys.argv)):
        if sys.argv[i] == '--func':
            args_dict['func'] = sys.argv[i+1]
        elif sys.argv[i] == '--terms' or sys.argv[i] == '--eps':
            args_dict['parameter'] = sys.argv[i+1]
            args_dict['oper'] = sys.argv[i]

    if not all(k in args_dict for k in ['func', 'parameter', 'oper']):
        sys.stderr.write('Недопустимый ввод')
        sys.exit(1)

    if args_dict['oper'] =='--terms':
        ser.terms(str(args_dict['func']), int(args_dict['parameter']))
    elif args_dict['oper'] == '--eps':
        ser.epsil(str(args_dict['func']), float(args_dict['parameter']))

elif sys.argv[1] == 'integrate':
    # Словарь для поиска значений после ключей
    args_dict = {}
    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == '--func':
            args_dict['func'] = sys.argv[i+1]
        elif sys.argv[i] == '--from':
            args_dict['from'] = float(sys.argv[i+1])
        elif sys.argv[i] == '--to':
            args_dict['to'] = float(sys.argv[i+1])
        elif sys.argv[i] == '--steps':
            args_dict['steps'] = int(sys.argv[i+1])
        i += 2

    if not all(k in args_dict for k in ['func', 'from', 'to', 'steps']):
        sys.stderr.write('Недопустимый ввод')
        sys.exit(1)

    if args_dict['func'] == 'ratio':
        ratiocalc(args_dict['from'], args_dict['to'], args_dict['steps'])
        sys.exit(0)

    elif args_dict['func'] == 'root':
        rootcalc(args_dict['from'], args_dict['to'], args_dict['steps'])
        sys.exit(0)

else:
    sys.stderr.write('Недопустимый ввод')
    sys.exit(1)