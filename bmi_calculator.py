# Python Beginner Projects

## BMI Calculator

This program calculates BMI using user input.

weight=int(input("Welcome to the BMI calculator. Can I have your weight in kg please? "))
height=float(input("Thanks. Now can I have your height in meters please? "))
BMI=weight/height**2
print(f"Your BMI is {BMI:.2f}")
if BMI >=18 and BMI <=25:
    print("Normal weight")
elif BMI <18:
    print("Underweight. Eat some food!")
else:
    print("Overweight")
