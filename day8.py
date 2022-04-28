#Ex 1 - Painting a wall
#You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. 
#Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
#number of cans = (wall height ✖️ wall width) ÷ coverage per can.
#e.g. Height = 2, Width = 4, Coverage = 5
#number of cans = (2 ✖️ 4) ÷ 5
#                     = 1.6
#But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.
#Write your code below this line 👇
import math

def paint_calc(height, width, cover):
    number_of_cans = ((height * width) / 5)
    number_of_cans = math.ceil(number_of_cans)
    print(f"You'll need {number_of_cans} cans of paint")
#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

#Ex 2 - Prime number checker
#Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime == True:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

#Project: Caesar Cipher
#Step 3:
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(plain_text, shift_amount, cipher_direction):
	cipher_text = ""
	if cipher_direction == "decode":
		shift_amount *= -1
	for letter in plain_text:
		position = alphabet.index(letter)
		new_position = position + shift_amount
		cipher_text += alphabet[new_position]
	print(f"The {direction}d text is {cipher_text}.")

caesar(plain_text = text, shift_amount = shift, cipher_direction = direction)
