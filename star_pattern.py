# note: https://www.youtube.com/watch?v=fX64q6sYom0
n = 5

for i in range(n):
    for j in range(n):
        print('*', end=' ')
    print()        


# 2nd Example
# increasing triangle pattern
n = 5
for i in range(n):
    for j in range(i+1):
        print('*', end=' ')
    print()

# 3rd Example
# decreasing triangle pattern
n = 5
for i in range(n):
    for j in range(n-i):
        print('*', end=' ')
    print()

# 4th Example
# right angle triangle pattern
n = 5
for i in range(n):
    for j in range(i,n):
        print(' ', end=' ')
    for j in range(i+1):
        print('*', end=' ')
    print()

# 5th Example
# right angle triangle pattern
n = 5
for i in range(n):
    for j in range(i+1):
        print(' ', end=' ')
    for j in range(i,n):
        print('*', end=' ')
    print()        

# 6th Example
# hill pattern
n = 5
for i in range(n):
    for j in range(i,n):
        print(' ', end=' ')
    for j in range(i):
        print('*', end=' ')
    for j in range(i+1):
        print('*', end=' ')
    print()

#reverse hill pattern
n = 5
for i in range(n):
    for j in range(i+1):
        print('', end= ' ')
    for j in range(i, n-1):
            print('*', end=' ')
    for j in range(i,n):
        print('*', end =' ')        
    print()

# diamond pattern


for i in range(n):
    for j in range(i+1):
        print('', end= ' ')     #reverse hill pattern
    for j in range(i, n-1):
            print('*', end=' ')
    for j in range(i,n):
        print('*', end =' ')        
    print()

