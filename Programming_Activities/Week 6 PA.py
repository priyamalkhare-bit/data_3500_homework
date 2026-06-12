#PA 1
# create a list with 3 favorite colors
colors = ["blue", "white", "red"]

# create a string with value "My favorite colors are: "
message = "My favorite colors are: "

# convert list to a comma separated string using join()
color_string = ", ".join(colors)

# concatenate the two strings and print the message
print(message + color_string)

#PA 2
# ask the user to enter their address
address = input("Enter your address: ")

# remove all whitespace from the string
address_no_spaces = address.replace(" ", "")

# verify that all remaining characters are letters or numbers
if address_no_spaces.isalnum():
    print("Valid address")
else:
    print("Invalid address")

#PA - 3
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

twoDList = []

for i in range(num1):
    twoDList.append([])

# nested for loop to loop through 2D list
for i in range(1, num1+1):
    for j in range(1, num2+1):
        twoDList[i-1].append(i * j)
        
# nested for loop to print out 2D list   
for i in range(num1):
    for j in range(num2):
        print(twoDList[i][j], end="   ")
    print()

#PA - 4
# create dictionary
dictionary = {}

# create dictionary keys and assign them to values
dictionary["age"] = int(input("What is your age: "))
dictionary["favorite_color"] = input("What is your favorite color: ")
dictionary["multiplication_table"] = twoDList

# print out all keys in dictionary and the values
for key in dictionary.keys():
    print(key, dictionary[key])

#PA - 5
import json
with open("person-1-1.json") as file:
    person = json.load(file)

# update information about person
print(person["age"])
person["age"] += 1
print(person["age"])

with open("person.json", "w") as file:
	json.dump(person, file, indent=4)

#PA - 6
# get user input 
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
try:
    num1/num2
except: # exception handling
    print("Cannot divide by zero")