#You are going to write a program that calculates the average student height from a List of heights.
#e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
#The average height can be calculated by adding all the heights together and dividing by the total number of heights.
#e.g.
#180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
#There are a total of 7 heights in student_heights
#1146 ÷ 7 = 163.71428571428572
#Average height rounded to the nearest whole number = 164
#Important You should not use the sum() or len() functions in your answer. 
#You should try to replicate their functionality using what you have learnt about for loops.
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_height = 0
counter = 0

for height in student_heights:
    total_height = total_height + height
    counter += 1
    average_height = round(total_height / counter, 0)
    
print(average_height)

#ex 2 - highest score
#You are going to write a program that calculates the highest score from a List of scores.
#e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
#Important you are not allowed to use the max or min functions. The output words must match the example.
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score
    else:
        highest_score= highest_score
        
print(f"The highest score in the class is: {highest_score}")

#ex 3 - calculate even numbers
#You are going to write a program that calculates the sum of all the even numbers from 1 to 100. 
#Thus, the first even number would be 2 and the last one is 100
#Write your code below this row 👇
total = 0
for even_number in range(2, 101, 2):
    total += even_number

print(total)

#ex 4 - fizzbuzz
#You are going to write a program that automatically prints the solution to the FizzBuzz game.
#Your program should print each number from 1 to 100 in turn.
#When the number is divisible by 3 then instead of printing the number it should print "Fizz".
#When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
#And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
#Write your code below this row 👇
for number in range(1, 101):
    if ((number % 3 == 0) and (number % 5 == 0)):
        print("Fizzbuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# Project day 5: Password generator
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for letter in range(1, nr_letters + 1):
	password += random.choice(letters)

for symbol in range(1, nr_symbols + 1):
	password += random.choice(symbols)

for number in range(1, nr_numbers + 1):
	password += random.choice(numbers)

print(f"Your easy to crack password is {password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = []
for letter in range(1, nr_letters + 1):
	password_list += random.choice(letters)

for symbol in range(1, nr_symbols + 1):
	password_list += random.choice(symbols)

for number in range(1, nr_numbers + 1):
	password_list += random.choice(numbers)

random.shuffle(password_list)

password_hard = ""
for char in password_list:
	password_hard += char

print(f"Your hard to crack password is {password_hard}")
