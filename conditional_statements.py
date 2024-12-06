###if-else###

def greatest(*args):
    if a > b:
        print("a is greatest")
    elif b > c:
        print("b is greatest")
    else:
        print("c is greatest")
a = 10
b = 11
c = 12
greatest(a,b,c)

#short-hand if
x = 1
y = 1
if x ==y: print("check your numbers")

#short hand if-else
m = 2
n = 3
print("m") if m>n else print("n")

###logical operators###
a = 10
b = 'abcd'
c = 12
if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
    print("check the format of number you have given")    
else:
    print("you have entered correct numbers")
    
###nested-if####
age = int(input("Enter age: "))
marks = int(input("Enter the total marks: "))
if age > 20:
    if marks > 70:
        print("you are eligible for admission ")
    else:
        print("you are not eligible because of your marks")
else:
    print("you are not eligible because of your age")  

#********************************************************************************************************************************************
####While Loop#####
import random

number_to_guess = random.randint(1,10)
attempts = 0

while True:
    guess = int(input("enter the number between \"1 to 10 only\" to check the guess: "))
    attempts +=1
    if guess == number_to_guess:
        print(f"hey you have entered corect guess number!!!! {guess} for {number_to_guess} ")
        break
    elif guess < number_to_guess:
        print(f"you have entered number with less value than guess_number {guess} for {number_to_guess}")
        continue
    else:
        print("Too high!!! {guess} for {number_to_guess} try again")
        continue
print(f"{attempts} made so far") 




   