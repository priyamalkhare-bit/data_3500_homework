# Ask the user for their birth year
birth_year = int(input("Enter the year you were born: "))

# Check generation based on birth year
if birth_year >= 1997:
    print("You belong to the Zoomer generation.")
elif birth_year >= 1981:
    print("You belong to the Millennial generation.")
elif birth_year >= 1965:
    print("You belong to Gen X.")
elif birth_year >= 1946:
    print("You belong to the Baby Boomer generation.")
else:
    print("You were born before the Baby Boomer generation.")