def fibonacci(n, cache = {0: 0, 1: 1}):
    if n in cache:
        return cache[n]
    else:
        cache[n] = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
        return cache[n]


from functools import cache

@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
