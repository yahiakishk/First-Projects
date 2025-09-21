P = float(input("Please enter amount borrowed (in $) : "))
while P <= 0:
    P = float(input("Amount borrowed invalid. Please enter amount borrowed: "))

r = float(input("Please enter interest rate (without %): "))
while r <= 0:
    r = float(input("Intrest amount invalid. Please enter interest rate (without %): "))

n = int(input("Please enter number of compounding periods per year: "))
while n <= 0:
    n = float(input("Amount invalid. Please enter number of compounding periods per year: "))

t = int(input("Please enter elapsed time (in years): "))
while t <= 0:
    t = float(input("Amount invalid. Please enter elapsed time (in years): "))

print(f"Your principal is ${P}")
print(f"Your interest rate is %{r}")
print(f"Your number of compounding periods per year is {n}")
print(f"Your elapsed time is {t} years")

r = r * 0.01
amount_owed = P * (1 + r/n) ** (n*t)

print(f"Amount owed: ${amount_owed:.2f}")

