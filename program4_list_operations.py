# Program 4: Demonstrate common list operations

# Create a list of programming languages
languages = ["Python", "Java", "C++", "JavaScript"]
print("Original List:", languages)

# Insert an item at index 1
languages.insert(1, "C")
print("After insert():", languages)

# Remove C++ from the list
languages.remove("C++")
print("After remove():", languages)

# Add a new item at the end of the list
languages.append("PHP")
print("After append():", languages)

# Count the items currently in the list
print("Length of list:", len(languages))

# Remove and return the last item
languages.pop()
print("After pop():", languages)

# Delete the item at index 1
del languages[1]
print("After del:", languages)
