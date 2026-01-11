import functools

def my_logger(func):
    """A decorator that logs function calls."""
    @functools.wraps(func) # Preserves the original function's name and docstring
    def wrapper(*args, **kwargs):
        print(f">>> Calling function: {func.__name__}")
        result = func(*args, **kwargs) # Call the original function
        print(f"<<< Function {func.__name__} returned: {result}")
        return result # Return the result of the function call
    return wrapper

@my_logger
def add_numbers(a, b):
    """Adds two numbers and returns the sum."""
    return a + b

# Calling the decorated function
sum_result = add_numbers(5, 3)
print(f"Result of the sum: {sum_result}")
