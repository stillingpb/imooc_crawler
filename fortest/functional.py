import time, functools


def performance(unit):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            s = time.time()
            result = func(*args, **kw)
            e = time.time()
            t = (e-s) if unit == 's' else (e-s)*1000
            return result
        return wrapper
    return deco

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial.__name__