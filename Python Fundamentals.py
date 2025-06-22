Section A: Multiple Choice Questions
1. What will be the output of the following code?
print(type(5 / 2))
a) int
b) float
c) double
d) error
Ans- b) float
2. Which of the following is a valid variable name in Python?
a) 2variable
b) variable_name
c) variable-name
d) variable name
Ans- b) variable_name
3. How do you take user input in Python?
a) input()
b) scan()
c) cin >>
d) read()
Ans- a) input()
4. What will bool([]) return?
a) True
b) False
c) None
d) Error
Ans- b) False
5. What does len([1, 2, 3, 4]) return?
a) 3
b) 4
c) 5
d) Error
Ans-  b) 4

Section B: Short Answer Questions
6. Write a Python program to swap two numbers without using a third variable.
a = 5
b = 10
a, b = b, a
print("a =", a)
print("b =", b)

7. What is the difference between is and == in Python?
== compares values (content).
is compares object identities (memory locations)

8. Write a Python function that returns whether a number is even or odd.
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

9. Explain mutable and immutable objects in Python with an example.
Mutable: Can be changed after creation (e.g., lists)
Immutable: Cannot be changed after creation (e.g., strings, tuples)

10. Write a Python program to find the largest number in a given list.
numbers = [5, 3, 8, 2, 9]
largest = max(numbers)
print("Largest number is:", largest)


Section C: Coding Questions
11. Write a Python program to check if a string is a palindrome (same forward and
backward).
def is_palindrome(string):
    return string == string[::-1]

print(is_palindrome("madam"))  # True

12. Write a Python program to generate the Fibonacci series up to n terms.
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(5)

13. Write a function that takes a list and returns a new list with only the unique
elements.
def unique_elements(lst):
    return list(set(lst))

print(unique_elements([1, 2, 2, 3, 4, 4]))

14. Write a Python function to count the number of vowels in a given string.
def count_vowels(string):
    count = 0
    vowels = "aeiouAEIOU"
    for char in string:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Hello World"))

15. Write a Python program to find the factorial of a number using recursion.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # 120
