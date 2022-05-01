#Ex 1: Grading Program
#You have access to a database of student_scores in the format of a dictionary. 
#The keys in student_scores are the names of the students and the values are their exam scores.
#Write a program that converts their scores to grades.
#By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values. 
#The final version of the student_grades dictionary will be checked.
#DO NOT modify lines 1-7 to change the existing student_scores dictionary.
#DO NOT write any print statements.
#This is the scoring criteria:
#    Scores 91 - 100: Grade = "Outstanding"
#    Scores 81 - 90: Grade = "Exceeds Expectations"
#    Scores 71 - 80: Grade = "Acceptable"
#    Scores 70 or lower: Grade = "Fail"

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
#TODO-2: Write your code below to add the grades to student_grades.👇
#for key in student_grades:
for key in student_scores:
    score = student_scores[key]
    if score >= 91:
        student_grades[key] = "Outstanding"
    elif score >= 81:
        student_grades[key] = "Exceeds Expectations"
    elif score >= 71:
        student_grades[key] = "Acceptable"
    else:
        score = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)


#Ex 2 - Updating travel log via a function
#You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries.
#Write a function that will work with the following line of code on line 21 to add the entry for Russia to the travel_log.
#add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
#    You've visited Russia 2 times.
#    You've been to Moscow and Saint Petersburg.

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

