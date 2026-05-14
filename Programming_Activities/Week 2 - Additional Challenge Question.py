# Input 3 numbers from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# Find the smallest and largest numbers
smallest = min(num1, num2, num3)
largest = max(num1, num2, num3)

# Print smallest and largest numbers
print("Smallest number is:", smallest)
print("Largest number is:", largest)


 # Check if the largest number is divisible by 2
if largest % 2 == 0:
    print("Range between smallest and largest:")

    # Print all numbers from smallest to largest
    for number in range(smallest, largest + 1):
        print(number)

# If largest number is not divisible by 2
else:
    # Check if smallest number is between 0 and 10
    if 0 <= smallest and smallest <= 10:
        print("The smallest number is within the range of 0 to 10.")
    else:
        print("The smallest number is not within the range of 0 to 10.")