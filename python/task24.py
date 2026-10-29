# List comprehension
squares = [x**2 for x in range(1, 11)]
even_numbers = [x for x in range(1, 51) if x % 2 == 0]
numbers_greater_than_50 = [x for x in [60, 70, 80, 90, 100] if x > 50]
names_starting_with_A = [name for name in ["Anamika", "Brengi", "Charmi", "Duli", "Emili"] if name.startswith("A")]

print("Squares of numbers from 1 to 10:", squares)
print("Even numbers from 1 to 50:", even_numbers)
print("Numbers greater than 50:", numbers_greater_than_50)
print("Names starting with A:", names_starting_with_A)
