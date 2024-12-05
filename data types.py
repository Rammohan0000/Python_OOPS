# ends the output with '@'
print("Python", end='@')
print("GeeksforGeeks")
print('09','12','2016', sep='-', end='\n')
print('Red','Green','Blue', sep=',', end='@')
print('geeksforgeeks')

x = 12
print(type(x))

x = 33.33
print(type(x))

z = 'string'
print(type(z))

a = 1+2j
print(type(a))

#bool
y = 'Primesoft'
print('Z' in y)

a = True
b = False
print(a and b)   # Output: False (Logical AND)
print(a or b)    # Output: True (Logical OR)

x = 5
y = 10
print(x > y)  # Output: False
print(x < y)  # Output: True
print(x == y) # Output: False
print(x != y) # Output: True

#spl characters
print("there is slash here \nplease be carefull")
print("there is slash here \tplease be carefull")
print("there is slash here(\\)please be carefull")
print("there is slash here \"please be carefull\"")

#raw string
print(r"there is slash here \nplease be carefull")

#format string
a = 'rammohan'
b = 'primesoft'
print(f"{a} works at {b}")
print("{} works at {}".format(a,b))

#str indexing
x = 'abcdefghijkl'
print(x[3:6])
print(x[::-2])

#typecast
new = list((x))
print(new)

