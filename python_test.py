Section A: Multiple Choice Questions
Choose the correct answer:

1. What will be the output of print(5 // 2)?
a) 2.5
b) 2
c) 3
d) 2.0
Ans- b) 2

2. Which of the following is used to define a block of code in Python?
a) Curly braces {}
b) Square brackets []
c) Indentation
d) Parentheses ()
Ans- c) Indentation

3. What does list.append(x) do?
a) Adds x to the beginning of the list
b) Adds x to the end of the list
c) Removes x from the list
d) Replaces the first element with x
Ans- b) Adds x to the end of the list

4. Which of the following is an immutable data type in Python?
a) List
b) Set
c) Dictionary
d) Tuple
Ans- d) Tuple

5. What is the correct syntax to open a file in Python for reading?
a) open('file.txt', 'r')
b) open('file.txt', 'w')
c) open('file.txt', 'a')
d) open('file.txt', 'x')
Ans- a) open('file.txt', 'r')

6. What will be the output of print(2 * 3 ** 2)?
a) 36
b) 18
c) 12
d) 9
Ans- b) 18

7. Which operator is used to compare two values in Python?
a) =
b) ==
c) !=
d) Both b and c
Ans- d) Both b and c

8. What is the purpose of try and except in Python?
a) To define a function
b) To handle exceptions (errors)
c) To create loops
d) To check conditions
Ans- b) To handle exceptions (errors)

9. What is the correct way to create a dictionary in Python?
a) d = {}
b) d = []
c) d = ()
d) d = set()
Ans- a) d = {}

10. Which of the following functions converts a string into a list of words?
a) split()
b) join()
c) replace()
d) find()
Ans- a) split()

Section B: Short Answer Questions
Answer in 1-2 sentences:
11. What is the difference between remove() and pop() methods in lists?
Ans- remove() deletes the first occurrence of a specified value
     pop() removes an element by index and returns it.

12. What is the purpose of the pass statement in Python?
Ans- pass is a placeholder that does nothing; it is used when a statement is syntactically required but no action is needed.

13. Explain how the range() function works with an example.
Ans- range() generates a sequence of numbers. 
     Example: range(1, 5) gives 1, 2, 3, 4.

14. What is the difference between deep copy and shallow copy in Python?
Ans- A shallow copy copies only the outer object
     a deep copy copies the object and all nested objects.

15. How do you check if a given key exists in a dictionary?
Ans- we can use if key in dict: to check if a key exists.

Section C: Coding Questions
Write Python code for the following: 
16. Write a Python program to check whether a number is positive, negative, or
zero.
Ans-
     num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


17. Write a Python program to print all the even numbers between 1 and 50.
Ans- 
      for num in range(1, 51):
    if num % 2 == 0:
        print(num, end=' ')


18. Write a Python function to find the factorial of a given number using recursion.
Ans-
    def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Enter a number: "))
print("Factorial is:", factorial(number))
