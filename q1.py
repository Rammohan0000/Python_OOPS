list1 = [10,9,2,3,5,1,3,110,4]
list2 = []
for i in range(len(list1)-1):
    print(list1[i],list1[i+1])
    if abs(list1[i] - list1[i+1]) == 1:
        list2.append(list1[i])
        list2.append(list1[i+1])
print(list2)          
print(sum(list2))


