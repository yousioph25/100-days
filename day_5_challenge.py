# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])

# for height in student_scores:

# print(student_scores)
print("SECOND CHALLENGE")
total = 0
for even in range(0, 101, 2):
    total += even
print(total)

print("THIRD CHALLENGE")
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    if number % 3 == 0:
        print("Fizz")
    if number % 5 == 0:
        print("Buzz")
    print(number)