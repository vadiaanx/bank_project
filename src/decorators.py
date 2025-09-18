import functools


def log(filename: str = None):
    """Регистрирует детали выполнения функций, такие как время вызова, имя функции,
    передаваемые аргументы, результат выполнения и информации об ошибках."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message + "\n")
                else:
                    print(message)
                return result
            except Exception as e:
                error_type = type(e).__name__
                message = f"{func.__name__} error: {error_type}. " f"Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message + "\n")
                else:
                    print(message)
                raise

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


@log()  # вывод в консоль
def div(x, y):
    return x / y


print(div(10, 2))  # → выведет в консоль "div ok"
