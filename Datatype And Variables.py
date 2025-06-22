Create Variables:
• Create a variable name and assign your name as a string.
Ans- name = "Nidhi"

• Create a variable age and assign your age as an integer.
Ans- age = 21

• Create a variable height in meters as a float.
Ans- height = 1.62

• Create a variable is_student and assign a boolean value.
Ans- is_student = True


Perform Operations:
• Print a sentence using all the variables. Example:
"My name is Vijay, I am 25 years old, my height is 1.75 meters, and it is True that I
am a student."
print(f"My name is {name}, I am {age} years old, my height is {height} meters, and it is {is_student} that I am a student.")


List Practice:
• Create a list called favorite_numbers containing 5 integers of your choice.
favorite_numbers = [7, 14, 21, 28, 35]

• Print the first and last number in the list.
print("First number:", favorite_numbers[0])
print("Last number:", favorite_numbers[-1])

• Add another number to the list and print the updated list. 
favorite_numbers.append(42)
print("Updated list:", favorite_numbers)

Tuple Practice:
• Create a tuple dimensions containing 3 float values representing length, width,
and height of a box.
 dimensions = (2.5, 3.0, 4.5)

• Print the tuple.
print("Box dimensions:", dimensions)


Set Practice:
• Create a set called unique_colors with at least 4 colors.
unique_colors = {"red", "blue", "green", "yellow"}

• Add a new color to the set.
unique_colors.add("purple")

• Remove a color from the set.
unique_colors.remove("green")

• Print the updated set.
print("Updated set of colors:", unique_colors)

Dictionary Practice:
• Create a dictionary called student_info with the following keys: name, age,
courses.
o courses should be a list of 3 course names.
student_info = {
    "name": "Nidhi",
    "age": 21,
    "courses": ["Data Analytics", "Python", "SQL"]
}

• Print the value of courses from the dictionary.
print("Courses:", student_info["courses"])

• Add a new key graduated with a boolean value.
student_info["graduated"] = False


Bonus Challenge:
Write a function print_student_summary(student_dict) that takes the student_info
dictionary and prints a summary of the student in a readable format.

def print_student_summary(student_dict):
    print(f"Student Name: {student_dict['name']}")
    print(f"Age: {student_dict['age']}")
    print(f"Courses Enrolled: {', '.join(student_dict['courses'])}")
    print(f"Graduated: {student_dict['graduated']}")

To call the function
    print_student_summary(student_info)