#Aiden Frye
#September 14, 2026
#P1HW1
#Purpose: This program will calculate whole numbers for the user

#Calcualting an Exponenet
print("--------Expoenents----------")
print()

#Ask the user for a base number and exponent
Base = int(input("Enter the base value: "))
Exponent = int(input("Enter the exponent value: "))

#calculate and print the result of the base raised to the power of the exponent
Result = Base ** Exponent

print(f"{Base} raised to the power of {Exponent} is {Result}")

#Calculate adding and subtracting two numbers
print()
print("--------Adding and Subtracting----------")
print()

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the number you wish to add: "))
num3 = int(input("Enter the number you wish to subtract: "))

#Store the results in a variable and print results to the user
sum_result = num1 + num2
final_result = sum_result - num3

print(f"The result of adding {num1} and {num2} and then subtracting {num3} is: {final_result}")
