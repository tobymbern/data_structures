import pandas as pd

def factorial(n):
    if n == 0:
        return 1
    else:
        print(n)
        return n * factorial(n-1)



print(factorial(3))
