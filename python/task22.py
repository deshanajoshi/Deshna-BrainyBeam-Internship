#calculate marks from a list.

marks = [45, 67, 89, 90, 78, 56, 34, 23, 12, 99]

# Using a loop
total_marks = 0
for mark in marks:
    total_marks += mark

number_of_subjects = len(marks)
average_marks = total_marks / number_of_subjects
highest_mark = max(marks)
lowest_mark = min(marks)

print("Total marks:", total_marks)
print("Number of subjects:", number_of_subjects)
print("Average marks:", average_marks)
print("Highest mark:", highest_mark)
print("Lowest mark:", lowest_mark)