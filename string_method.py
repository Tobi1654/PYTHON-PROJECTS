name = input("Enter your full name: ")

# len(): Will give us the length of a string
    #result = len(name)

#find(): finds the first occurrence of the input character
#rfind(): 'r' meaning reverse finds the last occurrence of input character
#if character is not found python returns '-1'
    #result = name.find("t")
    #result = name.rfind("t")

#capitalize(): capitalizes first letter
#upper(): capitalizes the whole string
#lower(): makes string all lowercase
    #name = name.capitalize()/name.upper()/name.lower()

#isdigit(): returns TRUE is the string only contains digits
#isalpha(): returns TRUE is the string only contains alphabet * excluding spaces *
    #result = name.isdigit()/name.isalpha()

#count(): counts the number of characters in a string
    #result = name.count("e")

#replace(): replaces a character with another
    #name = name.replace("o", "O")
print(name)


### USE THIS CODE 'print(help(str))' TO SEE ALL STRING METHODS

print(help(str))
