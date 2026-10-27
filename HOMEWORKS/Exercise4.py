# validate user input
# 1. username is not more than 12 char
# 2. username must not contain spaces
# 3. username must not contain ant digits

username = input("Enter your username: ")


if len(username) > 12:
    print("Username is too long")
elif username.find(" ") != -1:
    print("Your username can't contain spaces")
elif not username.isalpha(): #'not' establishes that 'username.isalpha()' is false
    print("Your username can't contain spaces")
else:
    print(f"Welcome {username}")

