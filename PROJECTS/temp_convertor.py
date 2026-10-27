unit = input("Enter your unit(C/F): ")
temp = float(input("What is your temperature: "))

if unit == "C":
    temp = (temp * 1.8) + 32
    unit = "F"
    print(f"Your new temperature is: {round(temp,2)}{unit}")
elif unit == "F":
    temp = (temp - 32) * 5/9
    unit = "C"
    print(f"Your new temperature is: {round(temp,2)}{unit}")
else:
    print(f"{unit} is not an identified temperature unit") 

