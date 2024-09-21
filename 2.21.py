amount = int(input("Enter your saving: "))
a = 0
for i in range(6):
    a = (amount+a)*(1+0.00417)
print("After the sixth month, the account value is ",a)