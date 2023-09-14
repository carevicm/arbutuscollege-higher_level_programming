JavaScript Web Jquery


Project badge
100%
JavaScript - Web jQuery
 Master
 By: Guillaume, CTO at Holberton School
 Weight: 1


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
<header> color is updated

  
7/7 pts
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
<header> color is updated to red

 
7/7 pts
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
<header> tag is updated when click on DIV#red_header

 
9/9 pts
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
HEADER tag has the class red when the user clicks on DIV#red_header

 
9/9 pts
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
When the user clicks on DIV#toggle_header, the class of HEADER toggles between red and green

 
7/7 pts
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
The new element is exactly <LI>Item</LI>

 
9/9 pts
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
Please review your task manually with the following checklist
The new text of HEADER is exactly “New Header!!!”

 
9/9 pts
7. Star wars character
mandatory
Write a JavaScript script that fetches the character name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json

The name must be displayed in the HTML tag DIV#character
You can’t use document.querySelector to select the HTML tag
You must use the JQuery API
Please test with this HTML file in your browser:

guillaume@ubuntu:~/$ cat 7-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      Star Wars character
    </header>
    <br />
    <div id="character"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="7-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/$ 
Repo:

GitHub repository: arbutuscollege-higher_level_programming
Directory: javascript-web_jquery
File: 7-script.js
Please review your task manually with the following checklist
The character name is assigned to the element DIV#character (after the request)

 
9/9 pts
8. Star Wars movies
mandatory
Write a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json

All movie titles must be list in the HTML tag UL#list_movies
You can’t use document.querySelector to select the HTML tag
You must use the JQuery API
Please test with this HTML file in your browser:

guillaume@ubuntu:~/$ cat 8-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      Star Wars movies
    </header>
    <br />
    <ul id="list_movies">
    </ul>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="8-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/$ 
Repo:

GitHub repository: arbutuscollege-higher_level_programming
Directory: javascript-web_jquery
File: 8-script.js
Please review your task manually with the following checklist
Each movie title is displayed in a LI element

 
9/9 pts
9. Say Hello!
mandatory
Write a JavaScript script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello.

The translation of “hello” must be displayed in the HTML tag DIV#hello
You can’t use document.querySelector to select the HTML tag
You must use the JQuery API
Your script must work when it is imported from the <head> tag
Please test with this HTML file in your browser:

guillaume@ubuntu:~/$ cat 9-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="9-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello!
    </header>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
guillaume@ubuntu:~/$ 
Repo:

GitHub repository: arbutuscollege-higher_level_programming
Directory: javascript-web_jquery
File: 9-script.js
