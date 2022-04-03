# Exercise 1:
# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
# Warning. Do not change the code on lines 1-3. Your program should work for different inputs. e.g. any two-digit number.

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆
####################################
#Write your code below this line 👇
digit_1 = int(two_digit_number[0])
digit_2 = int(two_digit_number[1])
print(digit_1 + digit_2)

# Exercise 2:
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
height = float(height)
weight = float(weight)
bmi = round(weight / (height * height), 2)
print(bmi)

# Exercise 3:
# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format: You have x days, y weeks, and z months left.
# Where x, y and z are replaced with the actual calculated numbers.
# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
max_age = 90
age = int(age)
years_remaining = max_age - age
num_months = round(years_remaining * 12)
num_weeks = round(years_remaining * 52)
num_days = round(years_remaining * 365)
print(f"You have {num_days} days, {num_weeks} weeks and {num_months} months left.")

# Project: Tip calculator
# If the bill was $150.00, split between 5 people, with 12% tip. 
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
# Write your code below this line 👇
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12 or 15? "))
num_people = int(input("How many people to split the bill? "))
bill_with_tip = tip / 100 * bill + bill
amount = round(bill_with_tip / num_people, 2)
# keep two decimal places even if it's e.g. 55.0
amount = "{:.2f}".format(amount)
print(f"Each person should pay: ${amount}")
