import numpy as np
import math



def inp(filename):
    num = np.loadtxt(filename , dtype=int)
    num1 = np.array(num)
    squar = [x ** 2 for x in num]
    print('Количество: ', (len(num)))
    print('Сумма: ', '{:4.3f}'.format(sum(num)))
    print("Среднее арифметическое: ", '{:4.3f}'.format((sum(num)/len(num))))
    print('Сумма квадратов', '{:4.3f}'.format(np.sum(num1**2)))
    print('Среднее квадратическое', '{:4.3f}'.format(math.sqrt(sum(squar)/len(squar))))
    print('Дисперсия', '{:4.3f}'.format(np.var(num1)))
    print('СKО: ', '{:4.3f}'.format(np.std(num1)))
    print('Стандартное отклонение: ', '{:4.3f}'.format(np.std(num1, ddof=1)))
    print('Наибольшее и наименьшее: ', '{:4.3f}'.format(max(num), 3), ';', '{:4.3f}'.format(min(num)))
    print('Кол-во положительных и отрицательных: ', len([x for x in num if x > 0]),';', len([x for x in num if x < 0]))
