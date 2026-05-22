# Activity 1
# create initial variables
is_palidrome = int(input("Enter a three digit number: "))

first_digit = is_palidrome // 100
third_digit = is_palidrome % 10

# check if palindrome
if first_digit == third_digit:
    print("palindrome!!!")
else:
    print("not palindrome!")
    
# Activity 2
# create initial variables
num = 2
total = 0

# run loop to sum up total
for i in range(1, 1001):
    total += 1/num
    num *= 2
    
print("total:", total)

# Acvitity 3
# create variables and get user input
age = eval(input("Enter your child's age: "))
weight = eval(input("Enter your child's weight: "))

# first try
# if age >= 12:
#     print("Your child can sit in the front seat")
# elif age == 11 and weight > 90:
#     print("Your child can sit in the front seat")
# elif age < 11 and weight > 100:
#     print("Your child can sit in the front seat")
# else:
#     print("Your child cannot sit in the front seat")

# second try using boolean variables    
criteria_1 = age >= 12
criteria_2 = age == 11 and weight > 90
criteria_3 = age < 11 and weight > 100

if criteria_1 or criteria_2 or criteria_3:
    print("Your child can sit in the front seat")
else:
    print("Your child cannot sit in the front seat")

# Activity 4
def welcome_fctn(name):
    print("Welcome", name)
    
welcome_fctn("Priya")

# Activity 5
def welcome_fctn(name):
    welcome_message = "Welcome " + name
    return welcome_message
    
print(welcome_fctn("Priya"))

# Activity 6
def welcome_fctn(name, age, favorite_color):
    welcome_message = "Welcome " + name + " you are " + str(age) + " years old, and " + favorite_color + " is your favorite color"
    return welcome_message
    
print(welcome_fctn("Priya", 35, "Pink"))
