# this is a training for using of decorators
from functools import wraps
import time


def decorator_without_parameters(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Start of decoration')
        res = func(*args, **kwargs)
        print('End of the decoration')
        return res
    return wrapper


def decorator_with_parameters(message):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(message)
            print('Start of decoration')
            res = func(*args, **kwargs)
            print('End of the decoration')
            return res
        return wrapper
    return decorator


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f'time for execution {end - start} seconds')
        return res
    return wrapper


@timer
@decorator_with_parameters('My message before execution\n')
def decorated_function():
    """Some documentation"""
    print('Execution of the function')
    return None


if __name__ == '__main__':
    #these 2 rows below show how the function would work if it would be called without a special sign "@" which is written above the function

    # decorated_function = decorator_without_parameters(decorated_function)
    # decorated_function = decorator_with_parameters('My message before execution\n')(decorated_function)
    decorated_function()
    print(f"""
    Since <wraps> from <functools> is also used while creating of decorators - metadata about the function is also saved:
    
    __name__ : {decorated_function.__name__}
    __doc__ : {decorated_function.__doc__}
    __module__ : {decorated_function.__module__}
    
    If you want to check the reverse effect, you just need to comment out the lines of code where it says ‘@wraps(func)’. 
    """)

