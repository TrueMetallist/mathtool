import random
import os

def filling(c, low, high, seed, out):
    os.truncate(out, 0)
    with open(out, 'a') as file:
        random.seed(seed)
        for i in range (1, c):
            a = random.randint(low, high)
            file.write(str(a) + '\n')