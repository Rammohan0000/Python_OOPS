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
