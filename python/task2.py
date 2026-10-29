# Program to calculate total marks, average marks, and percentage
python = float(input("Enter marks for Python: "))
mathematics = float(input("Enter marks for Mathematics: "))
database = float(input("Enter marks for Database: "))
statistics = float(input("Enter marks for Statistics: "))
computer_science = float(input("Enter marks for Computer Science: "))

total = python + mathematics + database + statistics + computer_science
average = total / 5
percentage = (total / 500) * 100

print(f"Total marks: {total}")
print(f"Average marks: {average}")
print(f"Percentage: {percentage}")