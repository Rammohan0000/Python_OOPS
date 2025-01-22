# number pattern -1
n = 5
p = 1 
for i in range(n):
    for j in range(i+1):
        print(p, end = " ")
    p += 1
    print()

# number pattern -2
n = 5   
p = 5
for i in range(n):
    for j in range(n-i):
        print(p, end = " ")
    p -= 1
    print()     

# number pattern -3
n = 5
p = 0 
for i in range(n):
    for j in range(i+1):
        print(p, end = " ")
    p += 2
    print()   

# alternative pattern - 4
n = 5
for i in range(n):
    for j in range(i+1):
        if (i%2 == 0):
            print(1, end = " ")
        else:
            print('2', end = " ")
    print()       

#diamond pattern for increment numbers
'''       1 
        2 2 2 
      3 3 3 3 3 
    4 4 4 4 4 4 4 
  5 5 5 5 5 5 5 5 5 
    6 6 6 6 6 6 6 
      7 7 7 7 7 
        8 8 8 
          9
'''           
n = 5
p = 1
for i in range(n-1):
    for j in range(i,n):
        print(" ", end = " ")
    for j in range(i):
        print(p, end = " ")
    for j in range(i+1):
        print(p, end = " ")
    p += 1
    print()
for i in range(n):
    for j in range(i+1):
        print(" ", end = " ")
    for j in range(i,n-1):
        print(p, end = " ")
    for j in range(i,n):
        print(p, end = " ")
    p += 1
    print()        

#incrementing number pattern
'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
'''
n = 5
for i in range(n):
    p = 1
    for j in range(i+1):
        print(p, end = " ")
        p += 1
    print()