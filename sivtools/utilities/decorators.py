"""Useful Decorators"""

import time


def print_(func):
    """Print the return value of the function"""
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        print(value)
        return value
    return wrapper


def timer(*args, **kwargs):
    """Decorator to time function"""
    def wrapper(func):
        def inner(*func_args, **func_kwargs):
            start = time.time()
            value = func(*func_args, **func_kwargs)
            end = time.time()

            elapsed = end - start
            print('Total Time Elapsed: {:.4f}s'.format(elapsed))

            return value
        return inner
    return wrapper
