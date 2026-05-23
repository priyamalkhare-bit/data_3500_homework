# Problem 3.4
print("Problem 3.4")
#loop 2 times since 2 rows
for row in range(2):
    #loop 7 times since 7 @
    for column in range(7):
        #print on single line
        print('@', end='')
    print()

# Problem 3.9
print("Problem 3.9")
number_string = input("Enter a number 7 to 10 digits: ")
#convert string to int
number = int(number_string)

#calculate the divisor
divisor = 10 ** (len(number_string) - 1)

while divisor >= 1:
    digit = number // divisor
    #get one digit at time
    print(digit)
    #shrink the number
    number = number % divisor

    #reduce divisor by 1 zero
    divisor = divisor // 10

# Problem 3.11
print("Problem 3.11")
total_miles = 0
total_gallons = 0

gallons = float(input("\nEnter the gallons used (-1 to end): "))

#until user inputs -1
while gallons != -1:
    miles = float(input("Enter the miles driven: "))

    mpg = miles / gallons
    print("The miles/gallon for this tank was", mpg)

    total_miles += miles
    total_gallons += gallons

    gallons = float(input("\nEnter the gallons used (-1 to end): "))

#calculate overall_mpg
overall_mpg = total_miles / total_gallons
print("The overall average miles/gallon was", overall_mpg)



# Problem 3.12
print("Problem 3.12")
number = int(input("Enter a 5-digit number: "))

# Extract digits
digit1 = number // 10000
digit2 = (number % 10000) // 1000
digit3 = (number % 1000) // 100
digit4 = (number % 100) // 10
digit5 = number % 10

# Check palindrome
if digit1 == digit5 and digit2 == digit4:
    print(number, "is a palindrome")
else:
    print(number, "is not a palindrome")


# Problem 3.14
print("Problem 3.14")
pi = 0
previous_pi = pi
# needed for toggling
sign = 1

#needed to jump out of loop
found_314 = False
found_3141 = False

for i in range(1, 3001):
    #formula
    denominator = 2 * i - 1
    pi = pi + sign * (4 / denominator)
    
    # using // and checking if previous pi value also starts with 3.14, found_314 to jump out of loop
    if (pi * 100) // 1 == 314 and (previous_pi * 100) // 1 == 314 and found_314 == False:
        print("3.14 appears twice in a row at iterations ", i - 1, "and", i)
        found_314 = True
        # using // and checking if previous pi value also starts with 3.141, found_3141 to jump out of loop
    if (pi * 1000) // 1 == 3141 and (previous_pi * 1000) // 1 == 3141 and found_3141 ==False:
        print("3.141 appears twice in a row at iterations ", i - 1, "and", i)
        found_3141 = True

    #current pi becomes previous pi for next iteration
    previous_pi = pi
    sign = sign * -1