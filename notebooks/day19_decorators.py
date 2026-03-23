# decorators : Decorators in Python are a way to modify or extend the behavior of a function without changing its actual code
def decorator(func):
    def wrapper(name):
        print("Before execution")
        func(name)
        print("After execution")
    return wrapper

@decorator
def greet(name):
    print(f"Hello {name}")

greet("Aman")

#------------------new-----------------------
print("\n")
@decorator
def print_age(age):
    print(f"My age is {age} ")

print_age(20)