"""
This is a simple program to add two integers
"""

print()
print("**This is a program that accepts two integers from you and adds them**")
print()

integer1 = int(input("Enter the first integer to be added: "))
integer2 = int(input("Enter the second integer to be added: "))
print()

sum = integer1 + integer2

print("The sum of {} and {} is {}".format(integer1, integer2, sum))
