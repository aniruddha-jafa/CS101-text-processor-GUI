# CS101 Project - A simple GUI text-file processor

Spring 2017. My fist ever programming project – I'd started learning to code about 2-3 months before this :flushed:

1. Description

This Python project uses graphical user interface (through Python's Tkinter package) to let users perform 
three word-related functions on a .txt file, assuming that the .txt file in question is saved in the same directory as the project. 

The name of the file the user wants to perform the functions on (for example, abc.txt ) is entered through the entry widget present in the window titled ‘Welcome’. Once the button ‘Confirm' is clicked, a new window called ‘Functions for text files’ opens, which provides widgets (buttons or entry widgets, depending on the function) for three functions: a palindrome function, a word count function and a word search function. Executing any of these functions creates a new window that displays the output of the respective function.

The palindrome function – which the user can access via the button 'Palindromes' –  lists all the palindromes present in the .txt file in alphabetical order.

The word count function – which the user can access via the button ‘Display all Words’ – lists all the words present in the file (in alphabetical order) along with the number of times they appear.

The word search function lets the user search for the number of times a certain word appears in a file. The word that the user wants to search for is entered in an entry widget, and clicking on the button 'Search' displays the results of the search in a new window. 

2. Key learning goals 
- read & process a text file
- use the Tkinter to create a simple GUI

3. Running the project code

- The file ‘user_interface.py’ should be executed by anyone trying to run the project. 
- The user should make sure that the text file on which the operations will be performed is in the same directory as the project.  
- In the entry widget present in the window ‘Welcome’, the file name should be entered as  filename.txt. For example, if I have a file called EnglishWords.txt in the same directory as the project code, I will enter EnglishWords.txt in the entry widget.
- Once this is done, click on the button ‘Confirm’. A new window called ‘Functions for text files’ will open, which gives access to three functions
- For a description of what the functions do and how to use them, refer to part 1. Description of the Project.  

4. Development details

 Python 2.7
