# PA 1
name = input("Enter your name: ")
fav_color = input("Enter your favorite color: ")

# write data to file
with open("name_color.txt", "w") as file:
    file.write(name + "'s favorite color is " + fav_color + "\n")
    print("Check the file")

#PA 2
import numpy as np
np1 = np.zeros(100)
np1 = np.random.rand(100)
print("np1:", np1)

# PA 3
# list creation
evens = [i for i in range(2, 101, 2)]
print("evens list:", evens)



# Pa 4
# list of stings
strings = ["   Priya  ", "Chetan      ","          Venkay","Manwa         ", "   :)  "]

# list comprehension to remove whitespace
new_list = [string.strip() for string in strings]
print(new_list)

# PA 5
# user input
name = input("Enter your name: ")
name = name.upper()
print("Welcome", name, "!")

# PA 6
#sentence
sentence = "dude, I just biked down that mountain and at first I was like Whoa and then I was like Whoa"
print(sentence)
sentence = sentence.capitalize()

# split words on the spaces
words = sentence.split(" ")

first_whoa = True # set up a variable to track how many times we've seen whoa
i = 0
for word in words:
    if words[i] == "whoa" and first_whoa:
        # first time - lower it
        words[i] = words[i].lower()
        # set tracker to false, first is gone
        first_whoa = False 
    elif words[i] == "whoa" and not first_whoa:
        words[i] = words[i].upper()
    else:
        pass
    i += 1

# output new sentence
new_sentence = ""
for word in words:
    new_sentence += " " + word

print(new_sentence)