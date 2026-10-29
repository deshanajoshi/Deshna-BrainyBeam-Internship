#student performance analysis
students = [
    {"name": "Anamika", "age": 20, "course": "Math", "marks": 85},
    {"name": "Barbie", "age": 22, "course": "Science", "marks": 78},
    {"name": "Charmi", "age": 21, "course": "History", "marks": 92},
    {"name": "Diya", "age": 23, "course": "Math", "marks": 65},
    {"name": "Eni", "age": 20, "course": "Science", "marks": 88},
    {"name": "Franky", "age": 22, "course": "History", "marks": 71},
]

def calculate_total_students():
    total_students = len(students)
    print(f"Total number of students: {total_students}")

def calculate_average_marks():
    total_marks = sum(student["marks"] for student in students)
    average_marks = total_marks / len(students) if students else 0
    print(f"Average marks: {average_marks:.2f}")

def calculate_highest_marks():
    highest_marks = max(student["marks"] for student in students)
    print(f"Highest marks: {highest_marks}")

def calculate_lowest_marks():
    lowest_marks = min(student["marks"] for student in students)
    print(f"Lowest marks: {lowest_marks}")

def count_passed_students():
    passed_students = sum(1 for student in students if student["marks"] >= 75)
    print(f"Number of students who passed: {passed_students}")

def count_failed_students():
    failed_students = sum(1 for student in students if student["marks"] < 75)
    print(f"Number of students who failed: {failed_students}")

def find_students_above_75():
    students_above_75 = [student for student in students if student["marks"] > 75]
    print("Students who scored above 75:")
    for student in students_above_75:
        print(f"Name: {student['name']}, Marks: {student['marks']}")

def find_student_with_highest_marks():
    student_with_highest_marks = max(students, key=lambda x: x["marks"])
    print(f"Student with the highest marks: {student_with_highest_marks['name']} (Marks: {student_with_highest_marks['marks']})")

def find_student_with_lowest_marks():
    student_with_lowest_marks = min(students, key=lambda x: x["marks"])
    print(f"Student with the lowest marks: {student_with_lowest_marks['name']} (Marks: {student_with_lowest_marks['marks']})")


def display_all_student_records():
    print("All Student Records:")
    for student in students:
        print(f"Name: {student['name']}, Age: {student['age']}, Course: {student['course']}, Marks: {student['marks']}")


calculate_total_students()
calculate_average_marks()
calculate_highest_marks()
calculate_lowest_marks()
count_passed_students()
count_failed_students()
find_students_above_75()
find_student_with_highest_marks()
find_student_with_lowest_marks()
display_all_student_records()

