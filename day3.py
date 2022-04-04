#Exercise 1: Even or odd numbers
#Write a program that works out whether if a given number is an odd or even number.
#Even numbers can be divided by 2 with no remainder.
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
    
#Exercise 2: BMI 2.0
#It should tell them the interpretation of their BMI based on the BMI value.
#Under 18.5 they are underweight
#Over 18.5 but below 25 they have a normal weight
#Over 25 but below 30 they are slightly overweight
#Over 30 but below 35 they are obese
#Above 35 they are clinically obese.
#Try to use the exponent operator in your code.
#Remember to round your result to the nearest whole number.
#Make sure you include the words in bold from the interpretations.
bmi = round(weight / height ** 2)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else: 
    print(f"Your BMI is {bmi}, you are clinically obese.")
