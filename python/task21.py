#list methods practice

students = ["dulari", "diya", "dolly", "dimpal", "divya"]
print("Original list:", students)

# 1. Add a new student
students.append("drishti")
print("After adding a new student:", students)

# 2. Insert a student at a specific position
students.insert(2, "ananya")
print("After inserting a student at position 2:", students)

# 3. Remove a student
students.remove("dolly")
print("After removing a student:", students)

# 4. Remove the last student
students.pop()
print("After removing the last student:", students)

# 5. Sort the names
students.sort()
print("After sorting the names:", students)

# 6. Reverse the list
students.reverse()
print("After reversing the list:", students)