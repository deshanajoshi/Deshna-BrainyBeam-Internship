#Mini Project: Number Analysis Program

print("Welcome to the Number Analysis Program!")
num_count = int(input("How many numbers would you like to enter? "))
numbers = []
for _ in range(num_count):
    num = float(input("Enter a number: "))
    numbers.append(num)

total = sum(numbers)
average = total / num_count if num_count > 0 else 0
maximum = max(numbers) if numbers else 0
minimum = min(numbers) if numbers else 0

even_count = sum(1 for n in numbers if n % 2 == 0)
odd_count = sum(1 for n in numbers if n % 2 != 0)
positive_count = sum(1 for n in numbers if n > 0)
negative_count = sum(1 for n in numbers if n < 0)

print("\nResults:")
print(f"Total: {total}")
print(f"Average: {average}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")
print(f"Number of even values: {even_count}")
print(f"Number of odd values: {odd_count}")
print(f"Number of positive values: {positive_count}")
print(f"Number of negative values: {negative_count}")