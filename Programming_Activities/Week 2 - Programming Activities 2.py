# Asking user for current_age and target_age
current_age = input("How old are you? ")
target_age = input("What age would you like to live to? ")

#converting str to int datatype and calculating years_left
years_left = eval(target_age) - int(current_age)

#printing friendly message
print("You have approximately", years_left, "years left to live.")