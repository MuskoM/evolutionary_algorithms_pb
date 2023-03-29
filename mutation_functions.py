from numpy import ndarray, float32

# DE/rand/1
def de_rand_1(F: float32, a: ndarray, b: ndarray, c: ndarray):
    return a + F * (b - c)

# DE/rand/2
def de_rand_2(F: float32, a: ndarray, b: ndarray, c: ndarray, d: ndarray, e: ndarray):
    return a + F * (b - c) + F * (d - e)

# DE/best/1
def de_best_1(F: float32, best: ndarray, a: ndarray, b: ndarray):
    return best + F * (a - b)

# DE/best/2
def de_best_2(F: float32, best: ndarray, a: ndarray, b: ndarray, c:ndarray, d:ndarray):
    return best + F * (a - b) + F * (c - d)


 

