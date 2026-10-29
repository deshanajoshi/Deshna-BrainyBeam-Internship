#mini project: Student Result Calculator

student_name = input("Enter student name: ")
roll_number = input("Enter roll number: ")

sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))
sub4 = float(input("Enter marks for Subject 4: "))
sub5 = float(input("Enter marks for Subject 5: "))


total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total / 5

if sub1 >= 33 and sub2 >= 33 and sub3 >= 33 and sub4 >= 33 and sub5 >= 33:
    result = "PASS"

   
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "E"
else:
    result = "FAIL"
    grade = "F"


print("\n" + "=" * 40)
print("             STUDENT RESULT")
print("=" * 40)

print("Student Name :", student_name)
print("Roll Number  :", roll_number)
print("-" * 40)
print("Subject 1    :", sub1)
print("Subject 2    :", sub2)
print("Subject 3    :", sub3)
print("Subject 4    :", sub4)
print("Subject 5    :", sub5)
print("-" * 40)
print("Total Marks  :", total, "/ 500")
print("Percentage   :", percentage, "%")
print("Grade        :", grade)
print("Result       :", result)
print("=" * 40)
