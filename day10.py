# Ex 1: days in month
#In the starting code, you'll find the solution from the Leap Year challenge. 
#First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year." 
#it should return True if it is a leap year and return False if it is not a leap year.
#You are then going to create a function called days_in_month() which will take a year and a month as inputs, e.g.
#days_in_month(year=2022, month=2)
#And it will use this information to work out the number of days in the month, then return that as the output
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  if month > 12 or month < 1:
      return "Invalid month. Choose a number between 1 and 12."
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if is_leap(year) and month == 2:
      return 29
  return month_days[month - 1]
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

#Project: Calculator
#Step 1
#Calculator

#Add
def add(n1, n2):
	return n1 + n2

#Subtract
def subtract(n1, n2):
	return n1 - n2

#Multiply
def multiply(n1, n2):
	return n1 * n2

#Divide
def divide(n1, n2):
	return n1 / n2

math_operation = {
	"+": add,
	"-": subtract,
	"*": multiply,
	"/": divide
}

num1 = int(input("What's the first number?:\n"))
for symbol in math_operation:
	print(symbol)
operation = input("Which math operation do you want to perform? Pick a symbol from the lines above:\n")
num2 = int(input("What's the second number?:\n"))

for math_function in math_operation:
	math_function = operation
	function = math_operation[math_function]
	answer = function(num1, num2)
	
print(f"{num1} {operation} {num2} = {answer}")















