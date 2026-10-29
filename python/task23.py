#filter marks

marks = [45, 67, 89, 90, 78, 56, 34, 23, 12, 99]
marks_greater_equal_70 = []
marks_below_70 = []
passing_marks = []
failing_marks = []

for mark in marks:
    if mark>=70:
        marks_greater_equal_70.append(mark)
    else:
        marks_below_70.append(mark)

#passing and failing marks

for mark in marks:
    if mark >= 40:
        passing_marks.append(mark)
    else:
        failing_marks.append(mark)

print("Marks greater than or equal to 70:", marks_greater_equal_70)
print("Marks below 70:", marks_below_70)
print("Passing marks:", passing_marks)
print("Failing marks:", failing_marks)
