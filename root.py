import math

def integrate_left_rectangles(func, a, b, n):
    
    h = (b - a) / n 
    total_sum = 0.0

    for i in range(n):
        x_i = a + i * h
        total_sum += func(x_i)
        
    return total_sum * h

def calculate( a, b, steps):
    print('F(x) = math.sqrt(x**2+1)')
    result = integrate_left_rectangles(f, a, b, steps)
    print(result)

def f(x):
    return math.sqrt(x**2+1)