#A Python dictionary is a data structure that stores the value in key: value pairs. 
#Values in a dictionary can be of any data type and can be duplicated, whereas keys can’t be repeated and must be immutable.
#ordered and changeable

#dict constructor
mydict = dict(name='ram', age=25, company="primesoft")
print(mydict)

#accesing elements
print(mydict['age'])
x=mydict.get("company")
print(x)

#length of dictionary
print(len(mydict))

#print keys
a = mydict.keys()
print(a)

#print values
b = mydict.values()
print(b)

#print both keys and values
c = mydict.items()
print(c)

#dict are mutable
mydict['age'] = 25.3
print(mydict['age'])

#add entries
mydict['dept'] = 'Automation'
print(mydict.items())

#Removing Items
mydict.pop('name')
print(mydict)
mydict.popitem() #removes last inserted
print(mydict)
del mydict['company'] # removes 
print(mydict)

#update- we can add or modify
mydict.update({'name':'rammohan'})
print(mydict['name'])

#to clear entire dictionary
mydict.clear()
print(mydict)

#create an new dict
new = dict(name='rammohan',age=25, sport='cricket')
print(new)

#accesing both keys and values using iteration
for key,values in new.items():
    print(f"{key} -> {values}")

#accessing keys
for x in new.keys():
    print(x)

#accesing values
for y in new.values():
    print(y)   

#copy dict
new2 = new.copy()
print(new2)    
new3 = dict(new)
print(new3)

####nested dict####
nested = {
    "hyundai": {
        "model": 'venue',
        "year": 2019,
        "color": 'white'
    },
    "mahindra": {
        "model":'thar-roxx',
        "year":2025,
        "color":'black'
    }       
}
print(nested)

#accesing nested dict
print(nested["hyundai"]["year"])
print(nested["mahindra"]["color"])

#adding values
nested["hyundai"]["fuel"] = 'diesel'

#changing values
nested["mahindra"]["model"] = 'xuv700'
print(nested)

#looping through nested dict

for x,y in nested.items():
    print(f"{x} and {y}")

    for key,values in y.items():
        print(f"{key} -> {values}")

#converting list into dict
keys = ['model','year','color']
values = ['venue',2019,'white']
result = dict(zip(keys,values))
print(result)

# fromkeys() method
keys = ['model','year','color']
values = 'NA'
result = dict.fromkeys(keys,values)
print(result)

#adding two dictionaries
dict1 = {'name': 'ram', 'age': 25}
dict2 = {'name': 'kasai', 'city': 'NY'}
dict3 = {key: [dict1.get(key), dict2.get(key)] for key in dict1.keys() | dict2.keys()}
print(dict3)

# swapping keys,values
dict4 = {'rohit' : 'odi', 'age': 37}
dict5 = {v:k for k,v in dict4.items()}
print(dict5)

'''
Method	      Description
clear()	      Removes all the elements from the dictionary
copy()	      Returns a copy of the dictionary
fromkeys()	  Returns a dictionary with the specified keys and value
get()	      Returns the value of the specified key
items()	      Returns a list containing a tuple for each key value pair
keys()	      Returns a list containing the dictionary's keys
pop()	      Removes the element with the specified key
popitem()	  Removes the last inserted key-value pair
setdefault()  Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	  Updates the dictionary with the specified key-value pairs
values()	  Returns a list of all the values in the dictionary
'''