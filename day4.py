#Ex 1 - Heads or Tails
#You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
#Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.
#When you run the code, just use a random number as the seed. e.g. 67346 It doesn't matter what you chose, it's only for our testing code to check your work.
#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
 # 🚨 Don't change the code above 👆 It's only for testing your code.
	 
#Write the rest of your code below this line 👇
random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")


#Ex2: Who's paying the bill? Randomized name picker
#You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
#Important: You are not allowed to use the choice() function.
import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
paying_index = random.randint(0, len(names) - 1)
paying_name = names[paying_index]
print(f"{paying_name} is going to buy the meal today!")

#Ex3: Treasure map
#You are going to write a program that will mark a spot with an X.
#In the starting code, you will find a variable called map.
#This map contains a nested list. When map is printed this is what the nested list looks like:
#['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']
#In the starting code, we have used new lines (\n) to format the three rows into a square, like this:
#['⬜️', '⬜️', '⬜️']
#['⬜️', '⬜️', '⬜️']
#['⬜️', '⬜️', '⬜️']
#This is to try and simulate the coordinates on a real map.
#Your job is to write a program that allows you to mark a square on the map using a two-digit system. 
#The first digit is the vertical column number and the second digit is the horizontal row number.
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
position_column = int(position[0])
position_row = int(position[1])
map[position_row - 1][position_column - 1] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

#project: rock, paper, scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n")
computer_choice = str(random.randint(0, 2))
print(computer_choice)

if user_choice == "0":
	print(rock)
	if computer_choice == "0":
		print(rock)
		print("It's a draw.")
	elif computer_choice == "1":
		print(paper)
		print("The computer chose Paper. You lost.")
	elif computer_choice == "2":
		print(scissors)
		print("The computer chose Scissors. You won, congratulations!")
else:
	if user_choice == "1":
		print(paper)
		if computer_choice == "1":
			print(paper)
			print("It's a draw.")
		elif computer_choice == "2":
			print(scissors)
			print("The computer chose Scissors. You lost.")
		elif computer_choice == "0":
			print(rock)
			print("The computer chose Rock. You won, congratulations!")
	else: 
		if user_choice == "2":
			print(scissors)
			if computer_choice == "2":
				print(scissors)
				print("It's a draw.")
			elif computer_choice == "1":
				print(paper)
				print("The computer chose Paper. You won, congratulations!")
			elif computer_choice == "0":
				print(rock)
				print("The computer chose Rock. You lost, sorry.")
				
		
