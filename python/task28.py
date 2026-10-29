# Multiple Students Records

students = [
    {"name": "Alia", "age": 20, "course": "Python Programming", "marks": 85.5},
    {"name": "Belly", "age": 22, "course": "Data Science", "marks": 92.0},
    {"name": "Charmi", "age": 21, "course": "Web Development", "marks": 78.5},
    {"name": "Dolly", "age": 23, "course": "Machine Learning", "marks": 95.0},
    {"name": "Emili", "age": 20, "course": "Mobile App Development", "marks": 88.5}
]

print("All Students:")
for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, Course: {student['course']}, Marks: {student['marks']}")

highest_student = max(students, key=lambda x: x["marks"])
lowest_student = min(students, key=lambda x: x["marks"])

print(f"\nStudent with Highest Marks: {highest_student['name']} ({highest_student['marks']})")
print(f"Student with Lowest Marks: {lowest_student['name']} ({lowest_student['marks']})")

average_marks = sum(student["marks"] for student in students) / len(students)
print(f"Average Marks: {average_marks}")