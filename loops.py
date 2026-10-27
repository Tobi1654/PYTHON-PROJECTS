# while loop = execute code WHILE some condition is true

name = input("Enter a name: ")

while name == "":
    print("This name is not valid")
    name = input("Enter a name: ")
print(f'Your name is {name}')

age = int(input("What is your age"))

while age < 16 or age > 60:
    print("You're not economically active")
    age = int(input("What is your age"))
print(f'you are {age}')


# for loop = execute a block of code a fixed number of times
#               You can iterate over range, string , sequence, etc.
# reversed = A built-in function that returns a reversed iterator of a sequence, such as a string, list, or tuple. It allows you to iterate through the elements of the sequence in reverse order.
# continue = A statement that is used to skip the current iteration of a loop and move on to the next iteration. It is often used to skip over certain conditions or to avoid executing specific code within a loop when a certain condition is met.
# break = A statement that is used to exit a loop prematurely, regardless of the loop's condition. When a break statement is encountered within a loop, the loop is immediately terminated, and the program continues with the next line of code after the loop. It is often used to exit a loop when a certain condition is met or to stop an infinite loop.
for i in range(1,20):
    if i == 2:
        continue
    elif i == 13:
        break
    print(i)


