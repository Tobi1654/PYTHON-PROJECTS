import math
# This program calculates the circumference of a circle given its radius.
# formula: C=2* pi* r

radius1 = float(input("Enter the radius of your circle: "))

circumference = 2 * math.pi * radius1

# Print the result rounded to 2 decimal places
print(f"The circumference is {round(circumference, 2)}")


# Area of a circle
# formula: A= pi* r^2

radius2 = float(input("Enter the radius of your circle: "))

# pow() function is used to calculate the power of a value.
area = math.pi * pow(radius2, 2)

print(f'The area of your circle is {round(area,2)}')


# Hypotenuse of a right triangle
# formula: c= sqrt(a^2 + b^2)

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))

c = math.sqrt(pow(a,2) + pow(b,2))

print(f"The hypotenuse is equal to {c}")