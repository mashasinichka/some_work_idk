import math as m
from sys import setrecursionlimit
setrecursionlimit(1000)

class Pow():
    def pow2(self, x):
        return x * x
    def pow2_math(self, a):
        return m.pow(a, 2)
    def pow3_math(self, a):
        return m.pow(a, 3)
def find_fibonacci(n):
    if n in (1, 2):
        return 1
    return find_fibonacci(n - 1) + find_fibonacci(n - 2)