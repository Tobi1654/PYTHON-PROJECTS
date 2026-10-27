# input() = A function that allows user input data
# returns the entered data as a string

name = input("What is your name? ")  # This will prompt the user to enter their name and return it as a string
print(f'Hello, {name}!')  # This will print a greeting message that includes the user's name

age = int(input("How old are you? "))  # This will prompt the user to enter their age and return it as a string
print(f'You are {age} years old.')  # This will print a message that


#logical operators = evaluate multiple conditions(and, or, not)
# and = Returns True if all statements are true
# or = Returns True if one of the statements is true
# not = Reverse the result, returns False if the result is true

#OR
temp1 = 48
is_raining = False

if temp1 > 30 or temp1 < 5 or is_raining:
    print("The event is cancelled ")
else:
    print("The event is still ongoing")

#AND
temp2 = 4
is_sunny = False

if temp2 >= 30 and is_sunny:
    print("It's hot, and sunny outside")
elif temp2 <= -5 and is_sunny:
    print("It's cold, and sunny outside")
elif temp2 >= 0 and temp2 < 20 and is_sunny:
    print("It's warm and sunny outside")

#NOT
elif temp2 >= 30 and  not is_sunny:
    print("It's hot, and cloudy outside")
elif temp2 <= -5 and not is_sunny:
    print("It's cold, and cloudy outside")
elif temp2 >= 0 and temp2 < 20 and not is_sunny:
    print("It's warm and cloudy outside")



# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
# Print or assign one of two values based on a condition
# FORMULA = X if condition else Y
# 
num = 5
a = 6
b = 7
age = 13
temperature = 20
user_role = "guest"
# 
# print("Positive" if num > 0 else "Negative")
# result = "EVEN" if num % 2 == 0 else "ODD"
# max_num = a if a > b else b
# min_num = a if a < b else b
# status = "Adult" if age >= 18 else "Child"
# weather = "HOT" if temperature > 20 else "COLD"
access_level = "Full Access" if user_role == "admin" else "Limited Access"

print(access_level)

# string indexing = A way to access specific characters in a string using their position (index)
# string indexing follows this pattern: [start:end:step]
credit_card_number = "1234 5678 9012 3456"
#print(credit_card_number[0])  # This will print the first digit of the credit card number
print(credit_card_number[5:9])  # This will print the digits from index 5 to 8 (inclusive)
print(credit_card_number[::2])  # This will print every other character in the credit card number, starting from the first character
print(credit_card_number[::-1])  # This will print the credit card number in reverse
