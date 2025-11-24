# calculator.py
"""
Calculator utility for Lab 11 (Partner 1 & Partner 2)
Implements the functions required by the lab documents.
"""

import math

def square_root(a):
    if a < 0:
        raise ValueError("square_root: input must be non-negative")
    return math.sqrt(a)


def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    """Return a + b"""
    return a + b


def subtract(a, b):
    """Return a - b"""
    return a - b


def sub(a, b):
    return subtract(a, b)


def multiply(a, b):
    """Return a * b"""
    return a * b


def mul(a, b):
    return multiply(a, b)


def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("divide: division by zero (denominator 'a' is zero)")
    return b / a


def div(a, b):
    return divide(a, b)

def logarithm(base, value):
    if base <= 0 or base == 1:
        raise ValueError("logarithm: base must be positive and not equal to 1")
    if value <= 0:
        raise ValueError("logarithm: value must be positive")
    return math.log(value, base)


def log(base, value):
    return logarithm(base, value)


def exponent(a, b):
    """Return a ** b"""
    return a ** b


def exp(a, b):
    return exponent(a, b)
