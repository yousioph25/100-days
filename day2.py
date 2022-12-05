print("Welcome to the tip calculator")
total = int(input("What was the total bill? "))
people = int(input("How many people to split the bill? "))
percentage = int(input("What percentage would you like to give? 10, 12 0r 15? "))
individual_payment = (total + (percentage/100*total))/ people
print(f"Each person should pay:  {individual_payment}")
