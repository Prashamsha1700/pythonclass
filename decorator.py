def decorator(func):
    def wrapper(a, b):
        print("Enter the numbers:")
        result = func(a, b)
        print("The sum of two numbers is:", result)
        return result
    return wrapper

@decorator
def add(a, b):
    return a + b

add(10, 20)