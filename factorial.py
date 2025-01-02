def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("enter the no: "))
result = factorial(n)
print(result)

# removing duplicates in a list
def remove_duplicates(lst):
    return list(set(lst))       

def remove_duplicates2(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

input_list = list(map(int, input("enter the nos: ").split()))
result = remove_duplicates2(input_list)
print(result) 

#return position of fibonacci number
def fibonacci(n):
    if n <= 0:
        return 0  # The 0th Fibonacci number is 0
    elif n == 1:
        return 0  # The 1st Fibonacci number is 0
    elif n == 2:
        return 1  # The 2nd Fibonacci number is 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b
n = int(input("Enter the position of the Fibonacci sequence: "))
print(f"The {n}th Fibonacci number is {fibonacci(n)}")

