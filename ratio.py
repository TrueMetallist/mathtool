def integrate_left_rectangles(func, a, b, n):
    
    h = (b - a) / n 
    total_sum = 0.0
    
    for i in range(n):
        x_i = a + i * h
        total_sum += func(x_i)
        
    return total_sum * h

def calculate( a, b, steps):
    print('F(x) = x / (x + 1)')
    result = integrate_left_rectangles(f, a, b, steps)
    print("Значение интеграла ≈ ", round(result, 5))

def f(x):
    return x/(x+1)