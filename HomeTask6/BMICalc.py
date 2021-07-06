# 1. WAF: bmi() that takes the weight in kg and height in cm of a person, calculates and returns the
# BMI.
# Write code that calls this function after taking height and weight as inputs and then prints
# underweight, normal, overweight or obese depending on the value of BMI.
# Refer this link for the ranges:
# https://en.wikipedia.org/wiki/Body_mass_index
# BMI = weight / (height/100)**2


def calculateBmi(w, h):
    BMI = w / (h / 100) ** 2
    print(BMI)
    if BMI <= 18.4:
        print("You are underweight.")
    elif 18.5 <= BMI <= 24.9:
        print("You are healthy.")
    elif 25 <= BMI <= 29.9:
        print("You are over weight.")
    elif 30 <= BMI <= 34.9:
        print("You are severely over weight.")
    elif 35 <= BMI <= 39.9:
        print("You are obese.")
    else:
        print("You are severely obese.")


w = float(input('Enter your weight in kg: '))
h = float(input('Enter your height in cm: '))
calculateBmi(w, h)
