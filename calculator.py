# https://github.com/Adrian11126/
# Partner roles: Adrian (Partner 1), Camryn (Partner 2)

# https://github.com/Adrian11126/lab10-AE-CW
# Partner roles: Adrian (Partner 1), <Partner Name> (Partner 2)

import math

# Square root function
def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(a)

# Hypotenuse function
def hypotenuse(a, b):
    return math.hypot(a, b)

# Add
def add(a, b):
    return a + b

# Subtract
def sub(a, b):
    return a - b

# Multiply
def mul(a, b):
    return a * b

# Divide (b / a)
def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

# Logarithm: log base a of b
def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Invalid base for logarithm")
    if b <= 0:
        raise ValueError("Cannot take log of non-positive number")
    return math.log(b, a)

# Exponent
def exp(a, b):
    return a ** b
