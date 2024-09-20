M = float(input("Enter the amount of water in kilograms: "))
finalTemperature = float(input("Enter final the temperature: "))
initialTemperature = float(input("Enter the initial temperature: "))
Q = M*(finalTemperature-initialTemperature)*4184
print(f"The energy needed is {Q}")