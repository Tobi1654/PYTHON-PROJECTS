weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds (kg or lbs): ")

if unit == "kg":
    weight = weight  * 2.205
    unit = "Lbs"
    print(f"Your weight is: {round(weight,2)}{unit}")

elif unit == "lbs":
    weight = weight / 2.205
    unit = "kg"
    print(f"Your weight is: {round(weight,2)}{unit}")

else:
    print(f"{unit} is not an identified value")
