# 4.    Write a program to print multiplication table of any given number in the format given below:
#            12 x 1 = 12
#            12 x 2 = 24

num = int(input("enter a number you eant the table of :-- "))
for i in range (1,11):
    print(num , "X" , i , "=" , num*i)

repeat = input("Do you want to repeat a table again :-- ")
if repeat == "yes":
    num = int(input("enter a number you eant the table of :-- "))
    for i in range (1,11):
        print(num , "X" , i , "=" , num*i)
elif repeat == "no":
    print("ok")
else:
    print("invalid syntax")
