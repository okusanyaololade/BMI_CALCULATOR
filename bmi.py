
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))



height2 = height**2
BMI = weight/height2
(round(BMI))
if 18.5 > BMI:
    print(f"Your BMI is {round(BMI)}, you are underweight.")
elif BMI<25:
    print(f"Your BMI is {round(BMI)}, you have a normal weight.")
elif BMI<30:
    print(f"Your BMI is {round(BMI)}, you are slightly overweight.")
elif BMI<35:
    print(f"Your BMI is {round(BMI)}, you are obese.")
else:
    print(f"Your BMI is {round(BMI)}, you are clinically obese.")


