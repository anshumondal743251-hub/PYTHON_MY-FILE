# Square of a number using Python

# Method 1: Using multiplication
number = 5
square = number * number
print(f"Square of {number} using multiplication: {square}")

# Method 2: Using exponentiation operator
square = number ** 2
print(f"Square of {number} using ** operator: {square}")

# Method 3: Using power function
import math
square = math.pow(number, 2)
print(f"Square of {number} using math.pow(): {int(square)}")

# Method 4: Using a function
def square_number(num):
    return num ** 2

result = square_number(7)
print(f"\nSquare of 7 using function: {result}")

# Method 5: Taking user input
user_input = int(input("\nEnter a number: "))
result = user_input ** 2
print(f"Square of {user_input} is: {result}")
