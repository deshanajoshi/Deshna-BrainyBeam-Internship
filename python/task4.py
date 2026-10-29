#type conversion Practice

age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
marks = float(input("Enter your marks: "))

print(f"Age: {age}, Type: {type(age)}")
print(f"Height: {height}, Type: {type(height)}")
print(f"Marks: {marks}, Type: {type(marks)}")

age_after_5_years = age + 5
print(f"Age after 5 years: {age_after_5_years}")