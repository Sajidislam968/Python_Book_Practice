weight = float(input("Enter your weight in pounds: "))*0.45359237
height = float(input("Enter your height in inches: "))*0.0254
BMI = (weight/(height**2))
print(f"Your BMI is {BMI:.2f}")