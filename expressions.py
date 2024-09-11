import math
import operator

def add(x, y):
    return x + y

def mul(x, y):
    return x * y

# calling expressions
add(1 + 1, 3)

# nested procedure
mul(add(4, mul(4, 6)), add(3, 5))

