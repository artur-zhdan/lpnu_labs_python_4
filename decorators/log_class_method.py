from functools import wraps



def log_class_method(method):
        @wraps(method)
        def wrapper(*args, **kwargs):
            print(f"Виклик методу {method.__name__} з аргументами {args} та {kwargs}")
            result = method(*args, **kwargs)
            return tuple(result)
        return wrapper

