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
#Step 2:
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(cipher_text, shift_amount):
	decrypted_text = ""
  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
	for letter in cipher_text_text:
		position = alphabet.index(letter)
		new_position = position - shift_amount
		decrypted_text += alphabet[new_position]
	print(f"The decrypted text is {decrypted_text}")


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == "encode":
	encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
	decrypt(cipher_text = text, shift_amount = shift)
