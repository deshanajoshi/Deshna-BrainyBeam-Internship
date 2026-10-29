#sum of Numbers 
end_no = int(input("Enter the ending number: "))
sum = 0
for i in range(1, end_no + 1):
    sum += i
print("The sum of numbers from 1 to", end_no, "is:", sum)