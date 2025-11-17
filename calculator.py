# https://github.com/Adrian11126/
# Partner roles: Adrian (Partner 1), Camryn (Partner 2)

import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Base must be positive and not equal to 1.")
    if b <= 0:
        raise ValueError("Number must be positive.")
    return math.log(b, a)

def exp(a, b):
    return a ** b

