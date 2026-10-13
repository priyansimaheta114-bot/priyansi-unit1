# Program 7: Create a menu-driven calculator using functions

# Return the sum of two numbers
def addition(a, b):
    return a + b

# Return the difference between two numbers
def subtraction(a, b):
    return a - b

# Return the product of two numbers
def multiplication(a, b):
    return a * b

# Return the quotient of two numbers
def division(a, b):
    return a / b


# Display the calculator menu
print("----- CALCULATOR MENU -----")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Read the user's choice and numbers
choice = int(input("Enter your choice (1-4): "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Call the selected function
if choice == 1:
    print("Addition =", addition(num1, num2))
elif choice == 2:
    print("Subtraction =", subtraction(num1, num2))
elif choice == 3:
    print("Multiplication =", multiplication(num1, num2))
elif choice == 4:
    # Check that the divisor is not zero
    if num2 != 0:
        print("Division =", division(num1, num2))
    else:
        print("Cannot divide by zero")
else:
    print("Invalid choice")
