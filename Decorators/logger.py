def logger(filename="log.txt"):
    def logger_decorator(func):
        def wrapper(*args, **kwargs):
            with open(filename, "a") as logfile:
                logfile.write(f"Calling {func.__name__}\n")
                func(*args, **kwargs)
                logfile.write(f"{func.__name__} returned\n")
        return wrapper

    return logger_decorator


@logger(filename="add.log")
def add():
    pass


add()