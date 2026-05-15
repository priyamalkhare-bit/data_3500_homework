# Ask the user for their age
age = int(input("Enter your age: "))

# Set the current year
current_year = 2026

# Loop while age is greater than 1
while age > 1:
    print("You were alive in year:", current_year)
    age = age - 1
    current_year = current_year - 1
else:
    print("You were born in year:", current_year)