Grading System (Conditionals):
• Create a variable score and assign an integer value between 0 and 100.

score = 85   


• Write an if-elif-else block to print the grade according to this scale:
o 90 - 100 : Grade A
o 80 - 89 : Grade B
o 70 - 79 : Grade C
o 60 - 69 : Grade D
o 0 - 59 : Grade F
o For any value not in 0-100, print "Invalid score".

students_scores = [95, 82, 74, 68, 50]
for student_score in students_scores:
    print(f"Student Score: {student_score}")
    if 90 <= student_score <= 100:
        print("Grade: A")
    elif 80 <= student_score <= 89:
        print("Grade: B")
    elif 70 <= student_score <= 79:
        print("Grade: C")
    elif 60 <= student_score <= 69:
        print("Grade: D")
    elif 0 <= student_score <= 59:
        print("Grade: F")
    else:
        print("Invalid score")



Loop through a List of Students (For Loop):
• Create a list students_scores that contains 5 student scores (integers).

students_scores = [95, 82, 74, 68, 50]

• Use a for loop to:
o Print each student's score.
o Print each student's corresponding grade (use the same grading logic as
above).

for student_score in students_scores:
    print(f"Student Score: {student_score}")
    if 90 <= student_score <= 100:
        print("Grade: A")
    elif 80 <= student_score <= 89:
        print("Grade: B")
    elif 70 <= student_score <= 79:
        print("Grade: C")
    elif 60 <= student_score <= 69:
        print("Grade: D")
    elif 0 <= student_score <= 59:
        print("Grade: F")
    else:
        print("Invalid score")



While Loop for User Input:
• Use a while loop to repeatedly ask the user to enter a score.
• For each entered score:
o Print the corresponding grade.
o The loop should stop when the user types "exit".

while True:
    user_input = input("Enter a score (or type 'exit' to stop): ")

    if user_input.lower() == "exit":
        print("Exiting the grading system.")
        break

    try:
        score = int(user_input)
    except ValueError:
        print("Please enter a valid number or 'exit'.")
        continue

    if 90 <= score <= 100:
        print("Grade: A")
    elif 80 <= score <= 89:
        print("Grade: B")
    elif 70 <= score <= 79:
        print("Grade: C")
    elif 60 <= score <= 69:
        print("Grade: D")
    elif 0 <= score <= 59:
        print("Grade: F")
    else:
        print("Invalid score. Please enter a score between 0 and 100.")



Bonus Task — Use break and continue:
• Inside the while loop:
o If the user enters a negative number, print "Negative score not allowed"
and use continue to skip the rest of the loop.
o If the user enters "exit", use break to stop the loop.

while True:
    score_input = input("Enter a score (or type 'exit' to stop): ")

    if score_input.lower() == "exit":
        print("Exiting the program.")
        break  

    try:
        score = int(score_input)
    except ValueError:
        print("Invalid input. Please enter a number or 'exit'.")
        continue  
    if score < 0:
        print("Negative score not allowed.")
        continue  

    if 90 <= score <= 100:
        print("Grade: A")
    elif 80 <= score <= 89:
        print("Grade: B")
    elif 70 <= score <= 79:
        print("Grade: C")
    elif 60 <= score <= 69:
        print("Grade: D")
    elif 0 <= score <= 59:
        print("Grade: F")
    else:
        print("Invalid score. Please enter a score between 0 and 100.")

        
