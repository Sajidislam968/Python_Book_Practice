min = int(input("Enter the number of minutes: "))
day = min//1440
year = day//365
a = day%365
print(f"{min} minutes is approximately {year} years and {a} days")