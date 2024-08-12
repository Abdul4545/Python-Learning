# Function caching is a technique for improving the performance of a program by storing the results of a function call so that we can reuse the results instead of recomputing them everytime the function is called

import functools

@functools.lru_cache()
def fib(n):
    if n < 2:
        return 1
    
    return fib(n - 1) + fib(n - 2)

print(fib(120))