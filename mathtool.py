import sys

if len(sys.argv) == 0 or sys.argv[1] == '--help':
    print('Всё ок')
    sys.exit('0')
else:
    print('Всё не ок')
    sys.exit('1')