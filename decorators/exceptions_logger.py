import logging
class NegativeRatingException(Exception):
    pass


def logged(exception, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                logger = logging.getLogger(__name__)
                if mode == "console":
                    logging.basicConfig(level=logging.ERROR)
                elif mode == "file":
                    logging.basicConfig(filename="log.txt", level=logging.ERROR)
                logger.error(f"Error occurred: {str(e)}")
        return wrapper
    return decorator