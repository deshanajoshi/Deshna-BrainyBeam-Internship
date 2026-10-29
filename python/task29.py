#Mini Project: Student Data Management

print("Welcome to the Student Data Management System")


students = []
def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course = input("Enter student course: ")
    marks = float(input("Enter student marks: "))
    student = {"name": name, "age": age, "course": course, "marks": marks}
    students.append(student)
    print(f"Student {name} added successfully!")

def view_students():
    if not students:
        print("No students found.")
        return
    print("All Students:")
    for student in students:
        print(f"Name: {student['name']}, Age: {student['age']}, Course: {student['course']}, Marks: {student['marks']}")

def search_student():
    name = input("Enter student name to search: ")
    for student in students:
        if student["name"].lower() == name.lower():
            print(f"Student found: Name: {student['name']}, Age: {student['age']}, Course: {student['course']}, Marks: {student['marks']}")
            return
    print(f"Student {name} not found.")

def update_student_marks():
    name = input("Enter student name to update marks: ")
    for student in students:
        if student["name"].lower() == name.lower():
            new_marks = float(input(f"Enter new marks for {name}: "))
            student["marks"] = new_marks
            print(f"Marks for {name} updated to {new_marks}.")
            return
    print(f"Student {name} not found.")

def delete_student():
    name = input("Enter student name to delete: ")
    for student in students:
        if student["name"].lower() == name.lower():
            students.remove(student)
            print(f"Student {name} deleted successfully.")
            return
    print(f"Student {name} not found.")

def find_highest_marks():
    if not students:
        print("No students found.")
        return
    highest_student = max(students, key=lambda x: x["marks"])
    print(f"Student with Highest Marks: {highest_student['name']} ({highest_student['marks']})")

def calculate_average_marks():
    if not students:
        print("No students found.")
        return
    average_marks = sum(student["marks"] for student in students) / len(students)
    print(f"Average Marks: {average_marks}")

# Main menu
while True:
    print("\nMenu:")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search for a Student")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Find Student with Highest Marks")
    print("7. Calculate Average Marks")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student_marks()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        find_highest_marks()
    elif choice == "7":
        calculate_average_marks()
    elif choice == "8":
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")


