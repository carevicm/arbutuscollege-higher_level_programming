JavaScript Web Jquery


Resources
Read or watch:

What is JavaScript?
Selector
Get and set content
Manipulate CSS classes
Manipulate DOM elements
API
Introduction
GET & POST request
JQuery Ajax Tutorial #1 - Using AJAX & API’s
What went wrong? Troubleshooting JavaScript
JQuery
JQuery API
JQuery Ajax
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
Why JQuery make front-end programming so easy (don’t forget to tweet today, with the hashtag #ilovejquery :))
How to select HTML elements in JavaScript
How to select HTML elements with JQuery
What are differences between ID, class and tag name selectors
How to modify an HTML element style
How to get and update an HTML element content
How to modify the DOM
How to make a GET request with JQuery Ajax
How to make a POST request with JQuery Ajax
How to listen/bind to DOM events
How to listen/bind to user events
Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted on Chrome (version 57.0)
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
Your code should be semistandard compliant with the flag --global $: semistandard *.js --global $
You must use JQuery version 3.x
You are not allowed to use var
HTML should not reload for each action: DOM manipulation, update values, fetch data…
More Info
Import JQuery
<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>


Manual QA Review
It is your responsibility to request a review for this project from a peer before the project’s deadline. If no peers have been reviewed, you should request a review from a TA or staff member.

Quiz questions
Great! You've completed the quiz successfully! Keep going! (Show quiz)
Tasks
0. No JQuery
mandatory
Write a JavaScript script that updates the text color of the <header> element to red (#FF0000):

You must use document.querySelector to select the HTML tag
You can’t use the JQuery API
Please test with this HTML file in your browser:

guillaume@ubuntu:~/$ cat 0-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="0-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/$ 
Repo:

GitHub repository: arbutuscollege-higher_level_programming
Directory: javascript-web_jquery
File: 0-script.js
Please review your task manually with the following checklist
File exists

 
0/7 pts
1. With JQuery
mandatory
Write a JavaScript script that updates the text color of the <header> element to red (#FF0000):

You can’t use document.querySelector to select the HTML tag
You must use the JQuery API
Please test with this HTML file in your browser:

guillaume@ubuntu:~/$ cat 1-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="1-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/$ 
Repo:

GitHub repository: arbutuscollege-higher_level_programming
Directory: javascript-web_jquery
File: 1-script.js
Please review your task manually with the following checklist
File exists

0/7 pts
2. Click and turn red
mandatory
Write a JavaScript script that updates the text color of the <header> element to red (#FF0000) when the user clicks on the tag DIV#red_header:

You can’t use document.querySelector to select the HTML tag
You must use the JQuery API
Please test with this HTML file in your browser:

guillaume@ubuntu:~/$ cat 2-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="2-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/$ 
Repo:

GitHub repository: arbutuscollege-higher_level_programming
Directory: javascript-web_jquery
File: 2-script.js
Please review your task manually with the following checklist
File exists

0/9 pts
3. Add `.red` class
mandatory
Write a JavaScript script that adds the class red to the <header> element when the user clicks on the tag DIV#red_header

You can’t use document.querySelector to select the HTML tag
You must use the JQuery API
Please test with this HTML file in your browser:

guillaume@ubuntu:~/$ cat 3-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <style>
      .red {
        color: #FF0000;
      }
    </style>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="3-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/$ 
Repo:

GitHub repository: arbutuscollege-higher_level_programming
Directory: javascript-web_jquery
File: 3-script.js
Please review your task manually with the following checklist
File exists

0/9 pts
4. Toggle classes
mandatory
Write a JavaScript script that toggles the class of the <header> element when the user clicks on the tag DIV#toggle_header:

The <header> element must always have one class: red or green, never both in the same time and never empty.
If the current class is red, when the user click on DIV#toggle_header, the class must be updated to green ; and the reverse.
You can’t use document.querySelector to select the HTML tag
You must use the JQuery API
Please test with this HTML file in your browser:

guillaume@ubuntu:~/$ cat 4-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <style>
      .red {
        color: #FF0000;
      }
      .green {
        color: #00FF00;
      }
    </style>
  </head>
  <body>
    <header class="green"> 
      First HTML page
    </header>
    <div id="toggle_header">Toggle header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="4-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/$ 
Repo:

GitHub repository: arbutuscollege-higher_level_programming
Directory: javascript-web_jquery
File: 4-script.js
Please review your task manually with the following checklist
File exists

0/7 pts
5. List of elements
mandatory
Write a JavaScript script that adds a <li> element to a list when the user clicks on the tag DIV#add_item:

The new element must be: <li>Item</li>
The new element must be added to UL.my_list
You can’t use document.querySelector to select the HTML tag
You must use the JQuery API
Please test with this HTML file in your browser:

guillaume@ubuntu:~/$ cat 5-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="5-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/$ 
Repo:

GitHub repository: arbutuscollege-higher_level_programming
Directory: javascript-web_jquery
File: 5-script.js
Please review your task manually with the following checklist
File exists

0/9 pts
6. Change the text
mandatory
Write a JavaScript script that updates the text of the <header> element to New Header!!! when the user clicks on DIV#update_header

You can’t use document.querySelector to select the HTML tag
You must use the JQuery API
Please test with this HTML file in your browser:

guillaume@ubuntu:~/$ cat 6-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="update_header">Update the header</div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="6-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/$ 
Repo:

GitHub repository: arbutuscollege-higher_level_programming
Directory: javascript-web_jquery
File: 6-script.js
 
