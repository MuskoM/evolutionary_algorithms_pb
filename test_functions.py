from numpy import ndarray
import numpy as np

def spherical(vec: ndarray):
    vec = np.asarray_chkfinite(vec)
    return (vec**2).sum()

def rastagin(vec: ndarray):
    vec = np.asarray_chkfinite(vec)
    n = len(vec)
    return 10*n + np.sum( vec**2 - 10 * np.cos( 2 * np.pi * vec ))

def griewank(vec: ndarray, fr=4000):
    vec = np.asarray_chkfinite(vec)
    n = len(vec)
    j = np.arange( 1., n+1 )
    s = np.sum( vec**2 )
    p = np.prod( np.cos( vec / np.sqrt(j) ))
    return s/fr - p + 1

def rosenbrock(vec: ndarray):
    vec = np.asarray_chkfinite(vec)
    x0 = vec[:-1]
    x1 = vec[1:]
    return (np.sum( (1 - x0) **2 )
        + 100 * np.sum( (x1 - x0**2) **2 ))

def ackley(vec: ndarray):
    vec = np.asarray_chkfinite(vec)
    n = len(vec)
    s1 = np.sum( vec**2 )
    s2 = np.sum( np.cos( 2*np.pi * vec ))
    return -20*np.exp( -0.2*np.sqrt( s1 / n )) - np.exp( s2 / n ) + 20 + np.exp(1)

def dixonprice( vec ):
    vec = np.asarray_chkfinite(vec)
    n = len(vec)
    j = np.arange( 2, n+1 )
    x2 = 2 * vec**2
    return np.sum( j * (x2[1:] - vec[:-1]) **2 ) + (vec[0] - 1) **2

def levy( vec ):
    vec = np.asarray_chkfinite(vec)
    n = len(vec)
    z = 1 + (vec - 1) / 4
    return (np.sin( np.pi * z[0] )**2
        + np.sum( (z[:-1] - 1)**2 * (1 + 10 * np.sin( np.pi * z[:-1] + 1 )**2 ))
        +       (z[-1] - 1)**2 * (1 + np.sin( 2 * np.pi * z[-1] )**2 ))

def michalewicz( vec, michalewicz_m = 0.5 ):
    vec = np.asarray_chkfinite(vec)
    n = len(vec)
    j = np.arange( 1., n+1 )
    return - np.sum( np.sin(vec) * np.sin( j * vec**2 / np.pi ) ** (2 * michalewicz_m) )

def powell( vec ):
    vec = np.asarray_chkfinite(vec)
    n = len(vec)
    n4 = ((n + 3) // 4) * 4
    if n < n4:
        vec = np.append( vec, np.zeros( n4 - n ))
    vec = vec.reshape(( 4, -1 ))
    f = np.empty_like( vec )
    f[0] = vec[0] + 10 * vec[1]
    f[1] = np.sqrt(5) * (vec[2] - vec[3])
    f[2] = (vec[1] - 2 * vec[2]) **2
    f[3] = np.sqrt(10) * (vec[0] - vec[3]) **2
    return np.sum( f**2 )

def schwefel( vec ):
    vec = np.asarray_chkfinite(vec)
    n = len(vec)
    return 418.9829*n - np.sum( vec * np.sin( np.sqrt( np.abs( vec ))))