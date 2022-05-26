"""
This is a simple command line interface calculator script
It can perform addition, subtraction, multiplication, division and modulo operations

It is presently constrained to perform operations on two numbers
"""

# Explain program to user
print(); print("**This program accepts two numbers from you and the operation you want \n\
	to perform on them**"); print()

# List operation that users can perform
print("List of operations:\n\
	\tfor addition enter 1\n\
	\tfor subtraction enter 2\n\
	\tfor division enter 3\n\
	\tfor multiplication enter 4\n\
	\tfor modulo operation enter 5")
print()

# Ask user to enter operation they want to perform
try:
	operation = int(input("Enter the number corresponding to the operation you want to perform: "))
except ValueError:
	print("Your input has to be an integer, please retry!")
	exit()

# Ask user for inputs
try:
	first_num = float(input("Enter the first number (numerator / dividend / minuend): "))
	second_num = float(input("Enter the second number (denominator / divisor / subtrahend): "))
except ValueError:
	print("Your input has to be an integer or a float, please retry!")
	exit()

def calculate(first_num, second_num, operation):
	"""Perform calculation operation on first_num and second_num"""
	if operation == 1:
		op_symbol = '+'
		return first_num + second_num, op_symbol
	elif operation == 2:
		op_symbol = '-'
		return first_num - second_num, op_symbol
	elif operation == 3:
		op_symbol = '/'
		if second_num == 0:
			return ZeroDivisionError
		return first_num / second_num, op_symbol
	elif operation == 4:
		op_symbol = '*'
		return first_num * second_num, op_symbol
	else:
		op_symbol = '%'
		return first_num % second_num, op_symbol

result = calculate(first_num, second_num, operation)
print(); # print("Result tuple", result)

if result != ZeroDivisionError:
	print("Result: {} {} {} = {}".format(first_num, result[1], second_num, result[0]))
else:
	print("You attempted to divide by zero")
