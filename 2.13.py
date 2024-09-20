num = int(input("Enter a number: "))
c =1000
for i in range(0,4):
    a = num//c
    print(a)
    num = num%c
    c //= 10
