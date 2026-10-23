#!/usr/bin/env python3
import argparse
import sys
import calc
import stats
import ser
from root import calculate as rootcalc
from ratio import calculate as ratiocalc
import fill

# Константа диапазона сохранена из исходного кода
con = range(-10000, 10001)
ran = range(-100, 101)

def main():
    # Основной парсер с описанием и сырой текстовой справкой для сохранения форматирования
    parser = argparse.ArgumentParser(
        prog='mathtool',
        description='Решение уравнений вида A*x^2 + B*x + C = 0 и другие математические утилиты.',
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    # Подкоманды (solve, stats, series, integrate)
    subparsers = parser.add_subparsers(dest='command', required=True, help='Доступные команды')

    # --- Подкоманда solve ---
    solve_parser = subparsers.add_parser('solve', help='Решение квадратного уравнения A*x^2 + B*x + C = 0')
    solve_parser.add_argument('-a', '--a', type=int, required=False, help='Коэффициент A')
    solve_parser.add_argument('-b', '--b', type=int, required=False, help='Коэффициент B')
    solve_parser.add_argument('-c', '--c', type=int, required=False, help='Коэффициент C')

    # --- Подкоманда stats ---
    stats_parser = subparsers.add_parser('stats', help='Статистика по числам из файла или stdin')
    stats_parser.add_argument('--input', type=str, help='Путь к входному файлу')

    # --- Подкоманда series ---
    series_parser = subparsers.add_parser('series', help='Работа с числовыми рядами')
    series_parser.add_argument('--func', type=str, required=True, help='Название функции ряда')
    
    # Группа взаимоисключающих аргументов: либо количество членов, либо точность
    group = series_parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--terms', type=int, help='Вычислить сумму N членов')
    group.add_argument('--eps', type=float, help='Вычислить сумму с точностью eps')

    # --- Подкоманда integrate ---
    int_parser = subparsers.add_parser('integrate', help='Численное интегрирование')
    int_parser.add_argument('--func', type=str, required=True, choices=['ratio', 'root'], help='Функция для интегрирования')
    # Используем dest='from_', так как 'from' — это зарезервированное ключевое слово Python
    int_parser.add_argument('--from', dest='from_', type=float, required=True, help='Нижний предел интегрирования')
    int_parser.add_argument('--to', type=float, required=True, help='Верхний предел интегрирования')
    int_parser.add_argument('--steps', type=int, required=True, help='Количество шагов разбиения')

    # --- Подкоманда fill ---
    fill_parser = subparsers.add_parser('fill', help='Заполнение массива чисел')
    fill_parser.add_argument('-c', '--count', required=True, type=int, help='Количество чисел от 1 до 1 000 000')
    fill_parser.add_argument('--min', required=False, type = int, default = -100, help='Нижний предел числа')
    fill_parser.add_argument('--max', required=False, type = int, default = 100, help='Верхний предел числа')
    fill_parser.add_argument('--seed', required=False, type=float, help='Семя числа')
    fill_parser.add_argument('-o1', '--output1', required=True, type=str, help='Файл для массива')

    # --- Подкоманда sort ---
    sort_parser = subparsers.add_parser('sort', help='Сортировка массива')
    sort_parser.add_argument('-m', '--method', required=True, choices=['bubble', 'selection', 'insertion', 'counting'], help='Метод сортировки')
    sort_parser.add_argument('--order', required=False, choices=['asc', 'desc'], help='По возрастанию или по убыванию')
    sort_parser.add_argument('-i', '--input', dest='input_', required=False, type=str, help='Файл с исходным массивом')
    sort_parser.add_argument('-o2', '--output2', required=False, type=str, help='Файл с отсортированным массивом')

    args = parser.parse_args()

    # Логика выполнения в зависимости от выбранной подкоманды
    if args.command == 'solve':
        # Если коэффициенты не переданы через флаги, запрашиваем их интерактивно
        if None in (args.a, args.b, args.c):
            try:
                if args.a is None:
                    args.a = int(input('Введите коэффициент A: '))
                if args.b is None:
                    args.b = int(input('Введите коэффициент B: '))
                if args.c is None:
                    args.c = int(input('Введите коэффициент C: '))
            except ValueError:
                sys.stderr.write('Недопустимый ввод: коэффициенты должны быть целыми числами\n')
                sys.exit(1)
        
        # Проверка диапазона (согласно исходной логике con = range(-10000, 10000))
        if not (args.a in con and args.b in con and args.c in con):
            sys.stderr.write('Коэффициенты должны быть в диапазоне [-10000, 10000]\n')
            sys.exit(1)
        
        calc.Calc(args.a, args.b, args.c, con)

    elif args.command == 'stats':
        if args.input:
            stats.inp(args.input)
        else:
            # Режим ручного ввода, если файл не указан
            with open('notinp.txt', 'w') as file:
                print('Вводите числа (пустая строка для завершения):')
                while True:
                    line = input('-- ')
                    if line == '':
                        break
                    if line.lstrip('-').isdigit():
                        file.write(line + '\n')
                    else:
                        sys.stderr.write('Недопустимый ввод, число пропущено\n')
            stats.inp('notinp.txt')

    elif args.command == 'series':
        if args.terms is not None:
            ser.terms(args.func, args.terms)
        else:
            ser.epsil(args.func, args.eps)

    elif args.command == 'integrate':
        if args.func == 'ratio':
            ratiocalc(args.from_, args.to, args.steps)
        elif args.func == 'root':
            rootcalc(args.from_, args.to, args.steps)

    elif args.command == 'fill':
        if args.min in ran and args.max in ran:
            fill.filling(args.count+1, args.min, args.max, args.seed, args.output1)
        else:
            sys.stderr.write('Выход за пределы значений min и max')
            sys.exit(1)
            
    elif args.command == 'sort':
        if args.method == 'bubble':
            print('bubble')
        if args.method == 'selection':
            print('selection')
        if args.method == 'insertion':
            print('insertion')
        if args.method == 'counting':
            print('counting')
        

if __name__ == '__main__':
    main()