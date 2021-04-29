from random import randint
count=0
a=0
b=0
a = int(input("enter the start of range of number:"))
b = int(input("enter the end of range of number:"))

randint(a,b)
for i in range(a,b):
    i = input("Enter any number in the range: ")
    if i!=randint(a,b):
        print("you choosed wrong. Try again!")
        count=count+1
        if count == 3:
            break
    else:
        print("you won")
print("better luck next time")


