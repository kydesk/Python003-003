import time
import math
from functools import wraps

def timer(func):
    @wraps(func)
    def t_counter(*args, **kwargs):
        start_time = time.time()
        ret = func(*args, **kwargs)
        end_time = time.time()
        print(f'The running of function {func.__name__} has taken {end_time - start_time:.9f} second.')
        return ret
    return t_counter

@timer
def solve_quadratic(a,b,c):
    d = b*b - 4*a*c
    if d < 0:
        return 'b^2-4ac is less then 0, there is no solution to the equation!'
    else:
        if a == 0:
            x = -c/b
            return x
        else:
            x1 = (-b + math.sqrt(d))/(2*a)
            x2 = (-b - math.sqrt(d))/(2*a)
            return x1, x2

# 测试方程求解
print(solve_quadratic(4,6,2))
print(solve_quadratic(2,5,-3))
print(solve_quadratic(3,2,5))