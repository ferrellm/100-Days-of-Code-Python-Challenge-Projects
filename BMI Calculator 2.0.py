weight = float(input("How much do you weigh? (kg)\n"))
height = float(input("How tall are you? (m)\n"))

bmi = weight / height ** 2

rounded_bmi = round(bmi)

if rounded_bmi  <= 18:
    print(f"Your BMI is {rounded_bmi}, you are underweight.")
elif rounded_bmi <= 24:
    print(f"Your BMI is {rounded_bmi}, you have a normal weight.")
elif rounded_bmi <= 29:
    print(f"Your BMI is {rounded_bmi}, you are slightly overweight.")
elif rounded_bmi <= 39:
    print(f"Your BMI is {rounded_bmi}, you are obese.")
else:
    print(f"Your BMI is {rounded_bmi}, you are clinically obese.")
