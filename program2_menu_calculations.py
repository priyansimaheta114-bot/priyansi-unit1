# Program 2: Menu-driven area and simple interest calculator

# Show the available calculation options
print("----- MENU -----")
print("1. Area of Circle")
print("2. Area of Triangle")
print("3. Area of Square")
print("4. Area of Rectangle")
print("5. Simple Interest")

# Ask the user to select an option
choice = int(input("Enter your choice (1-5): "))

# Perform the calculation selected by the user
if choice == 1:
    radius = float(input("Enter radius: "))
    area = 3.14 * radius * radius
    print("Area of Circle =", area)
elif choice == 2:
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = 0.5 * base * height
    print("Area of Triangle =", area)
elif choice == 3:
    side = float(input("Enter side: "))
    area = side * side
    print("Area of Square =", area)
elif choice == 4:
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))
    area = length * breadth
    print("Area of Rectangle =", area)
elif choice == 5:
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter rate of interest: "))
    time = float(input("Enter time in years: "))

    # Calculate simple interest
    simple_interest = (principal * rate * time) / 100
    print("Simple Interest =", simple_interest)
else:
    # Inform the user if the menu choice is not valid
    print("Invalid choice!")
