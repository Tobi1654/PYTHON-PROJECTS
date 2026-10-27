#Typecasting: the process of converting one datatype to another datatype is called typecasting.

name = "Tobi"
age = 16
pi = 3.14
is_handsome = True

print(type(name)) # <class 'str'>
print(type(age)) # <class 'int'>
print(type(pi)) # <class 'float'>
print(type(is_handsome)) # <class 'bool'>

#Typecasting
pi = int(pi) # converting float to int
print(pi) # 3

age = float(age) # converting int to float
print(age) # 16.0

age = str(pi) # converting float to string
print(pi) #3
print(type(pi)) # <class 'str'>

name = bool(name)
print(name) # True
print(type(name)) # <class 'bool'> 
# if the string is empty, it will return False, otherwise it will return True.

