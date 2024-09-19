from math import pi
a,b = map(float,input("Enter the radius and length of a cylinder: ").split(","))
area = a * a * pi
volume = area * b
print(f"The area of the cylinder is {area:.2f}")
print("The volume of the cylinder is",volume)

