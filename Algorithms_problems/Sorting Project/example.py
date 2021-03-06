
# The functions to compare
import math


def f1(degrees):
    return math.cos(degrees)


def f2(degrees):
    e = 2.718281828459045
    return (
        (e**(degrees * 1j) + e**-(degrees * 1j)) / 2
    ).real


# Assertions
assert f1(100) == f2(100) == 0.862318872287684
assert f1(1) == f2(1) == 0.5403023058681398


# Reporting
import time
import random
import statistics

functions = f1, f2
times = {f.__name__: [] for f in functions}

for i in range(100000):  # adjust accordingly so whole thing takes a few sec
    func = random.choice(functions)
    t0 = time.time()
    func(i)
    t1 = time.time()
    times[func.__name__].append((t1 - t0) * 1000)

for name, numbers in times.items():
    print('FUNCTION:', name, 'Used', len(numbers), 'times')
    print('\tMEDIAN', statistics.median(numbers))
    print('\tMEAN  ', statistics.mean(numbers))
    print('\tSTDEV ', statistics.stdev(numbers))
    