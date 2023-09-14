Hello World
Project badge
100%
Python - Hello, World
 Novice
 By: Guillaume
 Weight: 1
 Your score will be updated as you progress.
Concepts
For this project, we expect you to look at this concept:

Python programming
Author’s disclaimer
Welcome to the Python world!

You'll soon find that with Python (and the majority of higher level languages), there are ten different ways to do the same thing. Some tasks will expect only one implementation, while other tasks will have multiple possible implementations.
Python has a linter / style guide, called PEP8, also now known as PyCode. At Holberton, we won't start off with using PyCode, because it's much more strict compared to PEP8. Don't worry if you see a warning when you are running PEP8, you can ignore it.

Enjoy!

- Guillaume
Resources
Read or watch:

Use this playlist as long as you are learning Python:

Learn to Program

Whetting Your Appetite

Using the Python Interpreter

An Informal Introduction to Python (Read up until “3.1.2. Strings” included)

How To Use String Formatters in Python 3

Pycodestyle – Style Guide for Python Code

Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
How to use the Python interpreter
How to print text and variables using print
How to use strings
What are indexing and slicing in Python
What is the official Python coding style and how to check your code with pycodestyle
Requirements
Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.*)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file at the root of the repo, containing a description of the repository
A README.md file, at the root of the folder of this project, is mandatory
Your code should use the pycodestyle (version 2.7.*)
All your files must be executable
The length of your files will be tested using wc
More Info
Pycodestyle
Pycodestyle is now the new standard of Python style code

Quiz questions
Great! You've completed the quiz successfully! Keep going! (Show quiz)
Tasks
0. Hello, print
mandatory
Score: 100.00% (Checks completed: 100.00%)
Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.

Use the function print
guillaume@ubuntu:~/py/$ ./2-print.py 
"Programming is like building a multilingual puzzle
guillaume@ubuntu:~/py/$
Repo:

GitHub repository: arbutuscollege-higher_level_programming
Directory: python-hello_world
File: 2-print.py
   
6/6 pts
1. Print integer
mandatory
Score: 100.00% (Checks completed: 100.00%)
Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.

You can find the source code here
The output of the script should be:
the number, followed by Battery street,
followed by a new line
You are not allowed to cast the variable number into a string
Your code must be 3 lines long
You have to use f-strings tips
guillaume@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
guillaume@ubuntu:~/py/0x00$ 
Repo:

GitHub repository: arbutuscollege-higher_level_programming
Directory: python-hello_world
File: 3-print_number.py
   
7/7 pts
2. Print float
mandatory
Score: 100.00% (Checks completed: 100.00%)
Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.

You can find the source code here
The output of the program should be:
Float:, followed by the float with only 2 digits
followed by a new line
You are not allowed to cast number to string
You have to use f-strings
guillaume@ubuntu:~/py/0x00$ ./4-print_float.py
Float: 3.14
guillaume@ubuntu:~/py/0x00$ 
Repo:

GitHub repository: arbutuscollege-higher_level_programming
Directory: python-hello_world
File: 4-print_float.py
   
10/10 pts
3. Print string
mandatory
Score: 100.00% (Checks completed: 100.00%)
Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.

You can find the source code here
The output of the program should be:
3 times the value of str
followed by a new line
followed by the 9 first characters of str
followed by a new line
You are not allowed to use any loops or conditional statement
Your program should be maximum 5 lines long
guillaume@ubuntu:~/py/$ ./5-print_string.py 
Holberton SchoolHolberton SchoolHolberton School
Holberton
guillaume@ubuntu:~/py/$ 
Repo:

GitHub repository: arbutuscollege-higher_level_programming
Directory: python-hello_world
File: 5-print_string.py
   
6/6 pts
4. Play with strings
mandatory
Score: 100.00% (Checks completed: 100.00%)
Complete this source code to print Welcome to Holberton School!

You can find the source code here
You are not allowed to use any loops or conditional statements.
You have to use the variables str1 and str2 in your new line of code
Your program should be exactly 5 lines long
guillaume@ubuntu:~/py/$ ./6-concat.py
Welcome to Holberton School!
guillaume@ubuntu:~/py/$ wc -l 6-concat.py
5 6-concat.py
guillaume@ubuntu:~/py/$ 
Repo:

GitHub repository: arbutuscollege-higher_level_programming
Directory: python-hello_world
File: 6-concat.py
   
9/9 pts
5. Copy - Cut - Paste
mandatory
Score: 100.00% (Checks completed: 100.00%)
Complete this source code

You can find the source code here
You are not allowed to use any loops or conditional statements
Your program should be exactly 8 lines long
word_first_3 should contain the first 3 letters of the variable word
word_last_2 should contain the last 2 letters of the variable word
middle_word should contain the value of the variable word without the first and last letters
guillaume@ubuntu:~/py/$ ./7-edges.py
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
guillaume@ubuntu:~/py/$ wc -l 7-edges.py
8 7-edges.py
guillaume@ubuntu:~/py/$ 
Repo:

GitHub repository: arbutuscollege-higher_level_programming
Directory: python-hello_world
File: 7-edges.py
   
9/9 pts
6. Create a new sentence
mandatory
Score: 100.00% (Checks completed: 100.00%)
Complete this source code to print object-oriented programming with Python, followed by a new line.

You can find the source code here
You are not allowed to use any loops or conditional statements
Your program should be exactly 5 lines long
You are not allowed to create new variables
You are not allowed to use string literals
guillaume@ubuntu:~/py/$ ./8-concat_edges.py
object-oriented programming with Python
guillaume@ubuntu:~/py/$ wc -l 8-concat_edges.py
5 8-concat_edges.py
guillaume@ubuntu:~/py/$ 
Repo:

GitHub repository: arbutuscollege-higher_level_programming
Directory: python-hello_world
File: 8-concat_edges.py
   
9/9 pts
7. Easter Egg
mandatory
Score: 100.00% (Checks completed: 100.00%)
Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

Your script should be maximum 98 characters long (please check with wc -m 9-easter_egg.py)
guillaume@ubuntu:~/py/$ ./9-easter_egg.py
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
guillaume@ubuntu:~/py/$
Repo:

GitHub repository: arbutuscollege-higher_level_programming
Directory: python-hello_world
File: 9-easter_egg.py
