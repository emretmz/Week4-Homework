"""1-Calculator: General Information: I want to use a program which can calculate basic mathematical operations. Acceptance Criteria:
The calculator must support the Addition, Subtraction, Multiplication and Division operations.
All operations must be in a different module as method.
Operations must define with two float numbers as parametres.
Use math.ceil() for all results.
Create a menu to choose an operation.
User can choose invalid options, so you must handle all possible error. (Use try except :))
Inform user what type of error occured (TypError, ValueError etc.)
This process must continue until user want to quit from calculator.
"""
import math
def Addition(x,y):
    return x+y
def Subtraction(x,y):
    return x-y
def Multiplication(x,y):
    return x*y
def Division(x,y):
    return x/y
print("Select Operation!\n1.Add\n2.Substract\n3.Multiply\n4.Divide\n5.Quit\n")
choice=input("Enter choice 1/2/3/4")
while True:
    if choice in  ('1','2','3','4'):
        num1=float(input("enter first num:"))
        num2=float(input("enter sec num:"))
        if choice == '1':
                print(num1, "+", num2, "=", Addition(num1, num2))

        elif choice == '2':
                print(num1, "-", num2, "=", Subtraction(num1, num2))

        elif choice == '3':
                print(num1, "*", num2, "=", Multiplication(num1, num2))

        elif choice == '4':
                print(num1, "/", num2, "=", Division(num1, num2))
        
        next_calculation = input("Let's do next calculation? (yes/no): ")
            
        if next_calculation == "no":
            break    
    else:
        print("Invalid Input")