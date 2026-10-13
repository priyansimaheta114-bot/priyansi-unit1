# Program 5: Demonstrate common tuple operations

# Create a tuple of programming languages
languages = ("C++", "Java", "PHP")

# Tuples cannot be changed directly, so create a new tuple to add items
languages = ("React",) + languages + ("Python",)
print("Tuple after adding items:", languages)

# Check whether an item exists in the tuple
if "React" in languages:
    print("React is present in the tuple")
else:
    print("React is not present in the tuple")

# Find the number of items in the tuple
print("Length of tuple:", len(languages))

# Access items by their index
print("First item:", languages[0])
print("Second item:", languages[1])
print("Last item:", languages[-1])
