# Program 3: Calculate an employee's bonus

# Take the basic salary and years of service as input
basic_salary = float(input("Enter basic salary: "))
years = int(input("Enter years of service: "))

# Select the bonus percentage based on years of service
if years < 2:
    bonus = basic_salary * 5 / 100
elif years <= 5:
    bonus = basic_salary * 10 / 100
elif years <= 10:
    bonus = basic_salary * 15 / 100
else:
    bonus = basic_salary * 20 / 100

# Add the bonus to the basic salary
gross_salary = basic_salary + bonus

# Display the final details
print("Basic Salary =", basic_salary)
print("Bonus =", bonus)
print("Gross Salary =", gross_salary)
