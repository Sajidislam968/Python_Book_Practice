num = int(input("Enter a number between 0 and 1000: "))
lenth = len(str(num))
m = 0
for i in range(lenth):
    m += num % 10
    num //= 10
print("The sum of the digits is ",m)
#fuck you bitch
print(num)