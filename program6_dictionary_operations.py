# Program 6: Demonstrate common dictionary operations

# Create a dictionary containing student details
student = {
    "name": "Rahul",
    "course": "MCA",
    "semester": 1,
    "marks": 85
}

# Print the complete dictionary
print("Dictionary:", student)

# Access values using their keys
print("Student Name:", student["name"])
print("Course:", student["course"])

# Use get() to retrieve values
print("Semester:", student.get("semester"))
print("Marks:", student.get("marks"))

# Update the student's marks and semester
student["marks"] = 90
student["semester"] = 2

# Display the updated dictionary
print("Dictionary after changing values:", student)

# Count the key-value pairs in the dictionary
print("Number of items:", len(student))
