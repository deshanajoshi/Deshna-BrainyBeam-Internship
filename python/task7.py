#Pass or Fail

percentage = float(input("Enter your percentage: "))

if percentage < 0 or percentage > 100:
    print("Invalid percentage. Please enter a value between 0 and 100.")
elif percentage >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")