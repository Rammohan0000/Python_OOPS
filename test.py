d1 = {'1':'2', '2':'5', '6':'4', '7':'10'}
d2 = {'1':'3', '5':'5', '6':'4', '8':'10'}
 
#result = d1.extend(d2)
#print(result)

d1.update(d2)
print(d1)
