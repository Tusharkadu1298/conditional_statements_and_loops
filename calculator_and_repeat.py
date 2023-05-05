# 8.    Write a program to create a calculator and use while loop so the user can use it again without running the program. 


while True:
    print("*"*40)
    print("CALCULATOR")
    print("*"*40)
    num1 = float(input("enter the number :-- "))
    num2 = float(input("enter a number :-- "))
    print(''' 
    press 1 to +
    press 2 to -
    press 3 to *
    press 4 to /
    ''')
    choice = input("choose your choice from 1 - 4 ")
    if choice == 1:
        print(num1 + num2)
    elif choice == 2:
        print(num1 - num2)
    elif choice == 3:
        print(num1 * num2)
    elif choice == 4:
        print(num1 / num2)
    else:
        print("invalid statement")

        repeat = input("do you want to start again ?")
        if repeat == "no":
            break
