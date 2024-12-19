# decorators -> to modify or enhance the behaviour of a function or class.
# They are often used to add functionality to existing code in a clean and reusable way.
# A decorator is a function that takes another function as an argument
def simple_decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper
def say_hello():
    print("Hello!")
decorated_function = simple_decorator(say_hello)
decorated_function()

def inner_div(func):
    def wrapper(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return wrapper
@inner_div
def division(a,b):
    return a/b
result = division(2,10)
print(result)    

#Authorization decorator
def auth_decorator(func):
    def wrapper(user):
        if user == "admin":
            print("Access granted")
            func()
        else:
            print("Access denied")
    return wrapper
@auth_decorator
def sensitive_action():
    print("Performing sensitive action")
sensitive_action("admin")
sensitive_action("guest")

