# Program 8: Calculate percentage and grade for three subjects

# Take marks for all three subjects
marks1 = float(input("Enter marks of subject 1: "))
marks2 = float(input("Enter marks of subject 2: "))
marks3 = float(input("Enter marks of subject 3: "))

# Calculate total marks and average percentage
total = marks1 + marks2 + marks3
percentage = total / 3

# Assign a grade based on the percentage
if percentage >= 90:
    grade = "O"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
elif percentage >= 40:
    grade = "E"
else:
    grade = "F"

# Print the marks, percentage, and grade
print("=" * 30)
print("Subject 1 =", marks1)
print("Subject 2 =", marks2)
print("Subject 3 =", marks3)
print("Total Marks =", total)
print("Percentage = {:.2f}%".format(percentage))
print("Grade =", grade)
print("=" * 30)
