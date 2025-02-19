height = int(input("Please input your height in cm: "))
weight = int(input("Please input your weight in kg: "))

BMI = weight / (height/100)**2

if BMI < 18.5:
    print(f"{BMI} | Underweight")
elif 18.5 <= BMI < 25:
    print(f"{BMI} | Normal")
elif 25 <= BMI < 30:
    print(f"{BMI} | Overweight")
else:
    print(f"{BMI} | Obesity")
