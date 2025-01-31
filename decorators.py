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

#2nd example
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
        func(user) 
        if user == "admin":
            print("Access granted")
        else:
            print("Access denied")
    return wrapper
@auth_decorator
def sensitive_action(user):
    print(f"Performing sensitive action for {user}")
sensitive_action("admin")
sensitive_action("guest")


# chaining decorator
def decor1(func): 
    def inner(): 
        x = func() 
        return x * x 
    return inner 

def decor(func): 
    def inner(): 
        x = func() 
        return 2 * x 
    return inner 
@decor1
@decor
def num(): # bottom-up execution 10*2 = 20, 20*20 = 400
    return 10
@decor
@decor1
def num2():
    return 10
print(num()) # 400
print(num2()) # 200