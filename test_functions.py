from numpy import ndarray
import numpy as np

def spherical(vec: ndarray):
    return (vec**2).sum()

def rastagin():
    ...

def griewank():
    ...

def rosenbrock():
    ...

def ackley(vec: ndarray):
    return -20.0 * np.exp(
        -0.2 * np.sqrt((1/len(vec)) * (vec**2).sum())
    ) - np.exp(
        (1/len(vec)) * np.cos(2*np.pi*vec).sum()
    ) - 20 + np.exp(1)