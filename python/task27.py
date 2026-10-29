#Dictionaries

#Student Information Dictionary

student = {
    "name": "Alia",
    "age": 20,
    "course": "Python Programming",
    "city": "New York",
    "percentage": 85.5
}

# Accessing values in the dictionary

print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])
print("City:", student["city"])
print("Percentage:", student["percentage"])

# Update the percentage

student["percentage"] = 90.0

# Add a new field called email

student["email"] = "alia@example.com"

print("\nAfter updating percentage and adding email:")
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])
print("City:", student["city"])
print("Percentage:", student["percentage"])
print("Email:", student["email"])