import functools
import time

# 装饰器要写在类外面
def function_cost_time(func):
    """
    打印排序完成的数组与排序消耗时间
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        lis = func(*args, **kwargs)
        end_time = time.time()
        print("function '{}' time cost:{}".format(func.__qualname__, end_time - start_time))
        print(lis)
        return lis
    return wrapper