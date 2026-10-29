#student Grading System

per=float(input("Enter your percentage: "))
if per<0 or per>100:
    print("Invalid percentage. Please enter a value between 0 and 100.")
else:
    if per >= 90:
        grade = "A+"
    elif per >= 80:
        grade = "A"
    elif per >= 70:
        grade = "B"
    elif per >= 60:
        grade = "C"
    elif per >= 50:
        grade = "D"
    elif per >= 40:
        grade = "E"
    else:
        grade = "Fail"
    print(f"Your grade is: {grade}")
