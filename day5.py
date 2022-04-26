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
