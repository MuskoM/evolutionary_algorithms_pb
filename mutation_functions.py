from numpy import ndarray, float32

def rand1bin(F: float32, a: ndarray, b: ndarray, c: ndarray):
    return a * F * (b - c)

def rand1exp():
    ...

def rand2bin():
    ...

def best1bin():
    ...

def best2bin(F: float32, best: ndarray, a: ndarray, b: ndarray, c:ndarray, d:ndarray):
    return best + F * (a - b) + F * (c - d)

def best2exp():
    ... 

def current1bin(F: float32, i: ndarray, a: ndarray, b: ndarray):
    return i + F * (a - b)