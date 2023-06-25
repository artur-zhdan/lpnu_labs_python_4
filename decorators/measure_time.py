from functools import wraps
import time


def measure_time(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        start_time = time.time()
        result = method(self, *args, **kwargs)
        end_time = time.time()

        print(
            f"Час виконання методу {method.__name__}: {end_time - start_time} секунд")

        return result
    return wrapper
