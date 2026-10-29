#SET

#Common students

#sets,union,intersection,difference.

student_python = {"Alia", "Belly", "Charmi", "Dolly"}
student_data_science = {"Charmi", "Dolly", "Emili", "Foram"}

#both

both = student_python.intersection(student_data_science)

#only python
only_python = student_python.difference(student_data_science)

#only data science
only_data_science = student_data_science.difference(student_python)

# All unique students
all_students = student_python.union(student_data_science)

print("Students enrolled in both Python and Data Science:", both)
print("Students enrolled only in Python:", only_python)
print("Students enrolled only in Data Science:", only_data_science)
print("All unique students:", all_students)

