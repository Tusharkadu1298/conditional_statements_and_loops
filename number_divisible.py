# 2.	Write a Python program to check whether a number is divisible by another number. Accept two integer’s values form the user.

number = float(input("enter a number :-- "))
division = float(input("enter a division :--"))
div = number % division == 0
if ( number % division == 0):
    print("yes the number is divisible")
else:
    print("No the number is not divisible")
