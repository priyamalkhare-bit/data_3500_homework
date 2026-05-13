#Programming Activity 1

 #1. make a variable called apple_price (set it to whatever you want)
apple_price = 0.33
print("apple_price -", apple_price)

 #2. make a variable called number_purchased (set it to whatever you want)
number_purchased = 6
print("number_purchased -", number_purchased)
 
 #3. make a variable called tax and set it equal to 1.07
tax = 1.07
print("tax -", tax)

 #4. make a variable, total_bill and calculate it by: total_bill = apple_price * number_purchased * tax
total_bill = apple_price * number_purchased * tax
print("total_bill -", total_bill)

 #5. print clearly and cleanly how many apples were purchased and the total_bill
print("You bought", number_purchased, "apples for", apple_price, "per apple. Your total bill was", total_bill, "\n")

 #6. add a check before the final print statement to see if total_bill is equal to 0.  If so, print a message to the user to check their inputs.
if total_bill == 0:
    print("Please check your input")

# WHAT DOES THIS CODE DO? Create the variables x = 2 and y = 3, then determine what each of the following statements displays:
x = 2
y = 3
print('x =', x)
print('Value of', x, '+', x, 'is', (x + x))
print('x =')
print((x + y), 'x =', (y + x))