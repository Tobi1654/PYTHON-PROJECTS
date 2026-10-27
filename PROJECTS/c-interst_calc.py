# Compound Interest calculator
# formula: A = P(1+(r/n))^t
# **n=100**

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter your principle amount: "))
    if principle <= 0:
        print("Principle cant be <= 0")

while rate <= 0:
    rate = float(input("Enter your rate: "))
    if rate <= 0:
        print("Rate cant be <= 0")

while time <= 0:
    time = int(input("Enter your time in years: "))
    if time <= 0:
        print("Time cant be <= 0")


total = principle * (1 + (rate/100)) ** time
print(f"Your total balance is £{total:.2f} after {time} year/s")




