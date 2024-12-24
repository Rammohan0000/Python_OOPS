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

