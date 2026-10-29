#Number Counter 

count_positive = 0
count_negative = 0
count_zero = 0
count_even = 0
count_odd = 0
print("Enter 10 numbers for counting positive, negative, zero, even and odd numbers:")
for i in range(10):
    num=int(input("Enter Number:"))
    if num > 0:
        count_positive += 1
    elif num < 0:
        count_negative += 1
    else:
        count_zero += 1

    if num % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print("Count of positive numbers:", count_positive)
print("Count of negative numbers:", count_negative)
print("Count of zero numbers:", count_zero)
print("Count of even numbers:", count_even)
print("Count of odd numbers:", count_odd)
