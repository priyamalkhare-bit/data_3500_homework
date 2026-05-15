#2.3
print("\n")
print("Question 2.3")
#Check if the grade is 90 or higher
grade = int(input("Enter your grade: "))

#check if grad is grade is greater than equal to 90
if grade >= 90:
    print("Congratulations! Your grade of", grade, "earns you an A in this course")


#2.4
print("\n")
print("Question 2.4")
# Do arithmetic using 27.5 and 2
left = 27.5
right = 2

#calculation and prints
print("Addition:", left + right)
print("Subtraction:", left - right)
print("Multiplication:", left * right)
print("Division:", left / right)
print("Floor Division:", left // right)
print("Exponent:", left ** right)


#2.5
print("\n")
print("Question  2.5")
#Find the diameter, circumference, and area of a circle
radius = 2
pi = 3.14159

#calculations
diameter = 2 * radius
circumference = 2 * pi * radius
area = pi * (radius ** 2)

#prints
print("Diameter:", diameter)
print("Circumference:", circumference)
print("Area:", area)

#2.6
print("\n")
print("Question  2.6")
# Check if a number is odd or even
number = int(input("Enter an integer: "))

#modalus to check even or odd
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

#2.7
print("\n")
print("Question 2.7")
# Check if numbers are multiples using mod operator
if 1024 % 4 == 0:
    print("1024 is a multiple of 4")
else:
    print("1024 is not a multiple of 4")

if 2 % 10 == 0:
    print("2 is a multiple of 10")
else:
    print("2 is not a multiple of 10")


#2.8
print("\n")
print("Question 2.8")
#Print numbers, squares, and cubes in a table using tab \t
print("number\tsquare\tcube")

#loop through from 0 to 5
for number in range(6):
    print(number, "\t", number ** 2, "\t", number ** 3)