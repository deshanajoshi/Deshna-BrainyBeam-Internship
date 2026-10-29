#find maximum and minimum 

# Program to find the largest and smallest number from user input

# Using loops and conditions
no=[]
print("Enter 10 numbers")
for i in range(10):
    num=int(input("Enter Number:"))
    no.append(num)
largest=no[0]
smallest=no[0]

for i in no:
    if i>largest:
        largest=i
    if i<smallest:
        smallest=i
print("Largest Number:", largest)
print("Smallest Number:", smallest)

# Using Python's built-in max() and min() functions
print("Using Python's built-in functions:")

print("Largest Number (using max()):", max(no))
print("Smallest Number (using min()):", min(no))
