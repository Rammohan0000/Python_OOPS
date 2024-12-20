#count occurance of each character
def occurance(str):
    dict = {}
    for n in str:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
str = input("Enter a string: ")
print(occurance(str))

# most occurring character
def most_occuring_char(occurance_dict):
    max_char = max(occurance_dict, key=occurance_dict.get)
    return max_char
occurance_dict = occurance(str)
print(f"The most occurring character is: {most_occuring_char(occurance_dict)}")