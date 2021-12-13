
from itertools import permutations
import numpy as np
import matplotlib.pylab as plt
import math

def test():
    n = 10
    input = 1+np.random.permutation(n)
    #input = np.array([ 63,  64,   2,  99,  67,  31,  65,  74,  39,  14,  46,  20,  91,  23,   5, 12,  69,  51,   6,  48,  57,  50,  94,  40,  90,  52,  98,  37,  47,  62, 55,  19, 100,  32,  26,  45,  85,  80,  16,  77,  58,  11,  68,   3,  18, 72,  83,  41,  30,  33,  44,  38,  93,  25,  66,  95,  21,  17,  76,  56, 15,  60,  13,  73,  97,  87,  86,   9,   1,  81,  70,  84,  28,  79,  10, 24,  82,  22,  71,  92,  61,   4,  75,  42,   7,  29,  78,  35,  89,  88, 53,  27,  96,   8,  43,  49,  59,  34,  54,  36])
    print(np.array2string(input, separator=', '))
    print("opt: {0}".format(opt(input)))
    print("c: {0}".format(c(input)))

def full_test(n):
    r = 1 + np.arange(n)
    perms = set(permutations(r))
    fac = math.factorial(n)

    ratio = 1
    for count, p in enumerate(perms):
        if count % 10000 == 0:
            print("done: {0}/{1}".format(count,fac))
        ar = np.array(p)
        o = opt(ar)
        m = c(ar)
        if ratio < o/m:
            print(ar)
            ratio = o/m
            print(ratio)
    print("final ratio = {0}".format(ratio))

def opt(input):
    out = 0
    for i in range(input.shape[0]):
        for j in range(i, input.shape[0]):
            if out < (input[j] - input[i] + 1):
                out = input[j] - input[i] + 1
    return out
def c(input):
    n = input.shape[0]
    missing = 1 + np.arange(n)
    for i in range(n):
        missing[input[i] - 1] = 0
        opt_future = np.max(missing)
        out = opt_future - input[i] + 1

        if out >= np.sqrt(n):
            return out
    return 1
def plot(n):
    x1 = n - np.arange(n) - 1
    x2 = n - np.arange(n) - 1
    ns = int(np.floor(np.sqrt(n)))
    x1[ns] = n
    x2[-1] = n
    plt.plot(np.arange(n) +1,x1, '--o')
    plt.plot(np.arange(n) +1,x2, '--*')
    plt.show()


plot(64)