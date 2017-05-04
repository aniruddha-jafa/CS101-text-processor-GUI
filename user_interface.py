"""
This is the file that anyone exploring this project should run.

"""

import Tkinter as tkinter
from Textfile_functions import *

#creating a new window, where the user can enter the name of the file on which the function will be performed
mywindow = tkinter.Tk()
mywindow.title("Welcome")
mywindow.geometry("400x400")

prompt_user = tkinter.Label(mywindow, text= "Enter file name: ")
prompt_user.pack()

# Entry widget for user to enter a file name
user_file_name = tkinter.Entry(mywindow)
user_file_name.pack()

# this function goes through the dictionary of palindromes created from the text file and
def display_palindromes(dic_palindromes):

    list_keys = dic_palindromes.keys()
    list_keys.sort

    palindrome_window = tkinter.Tk()
    palindrome_window.title("Palindromes")
    palindrome_window.geometry("300x300")

    #putting a scrollbar on the right side, making it fill up the y-axis
    scrollbar = tkinter.Scrollbar(palindrome_window)
    scrollbar.pack(side = "right", fill = tkinter.Y)

    # using the widget listbox, since it allows for easy implimentation of the scrollbar functionality
    listbox = tkinter.Listbox(palindrome_window, borderwidth = 0, yscrollcommand = scrollbar.set)

    for key in list_keys:
        listbox.insert(tkinter.END, key)

    listbox.pack(side ="left" , fill = tkinter.BOTH)
    scrollbar.config(command = listbox.yview)

    palindrome_window.mainloop()

def display_all_words(dic_words):

    list_keys = dic_words.keys()
    list_keys.sort()

    all_words_window = tkinter.Tk()
    all_words_window.title("Frequency of all words")
    all_words_window.geometry("300x300")

    scrollbar = tkinter.Scrollbar(all_words_window)
    scrollbar.pack(side = "right", fill = tkinter.Y)

    #When the widget view is modified, the widget notifies the scrollbar by calling the set method.
    listbox = tkinter.Listbox(all_words_window, borderwidth = 0, yscrollcommand = scrollbar.set)

    for key in list_keys:

        value = str(dic_words[key])
        y = "%s   : %s "  %(key, value)
        listbox.insert(tkinter.END, y)

    # the listbox appears to the left, and expands along both the x and y axis.
    listbox.pack(side ="left" , fill = tkinter.BOTH)

    # when the user manipulates the scrollbar, the wdiget's yview method is called, along wi th the appropratie arguments
    scrollbar.config(command = listbox.yview)

    all_words_window.mainloop()

# defining the variable "current word" outside the function word_search
current_word = ""

def word_search(user_word_entry, dic_words, actual_file):

    current_word = user_word_entry.get()
    key = current_word.lower()

    #creating a wndow to display the wor search results
    word_search_window = tkinter.Tk()
    word_search_window.title("Word search results")
    word_search_window.geometry("300x300")

    # if the word inputted by the user (represented by the variable "key") is in the dictionary of words,
    # we find how many times it appears (represented the variable "count")
    if key in dic_words:
         count = str(dic_words[key])
         search_results =  "The word %s appears in the textfile %s a total of %s times"  %(key, actual_file, count)

         # search results displayed using the label widget.
         word_search_results = tkinter.Label (word_search_window, text = search_results)
         word_search_results.pack()


    else:
         search_results = "The word %s does not appear in the textfile %s" %(key, actual_file)
         word_search_results = tkinter.Label(word_search_window, text = search_results)
         word_search_results.pack()


# defining the variable "actual file" outside the funtion assign_file.
actual_file = ""

# the function assign_file takes the user input as the name of the file, and performs functions on it, creating new variables in the process.
# the function also creates a new window titled 'Functions for text files', which contains the widgets that give the user access
# to the 3 functions (display_palindromes, word_search, display_all_words)
def assign_file():

    actual_file = user_file_name.get()

    # the following functions are performed on on the textfile specified by the user:
    list_lines = file_to_list_strings(actual_file)

    list_words = list_strings_to_list_words(list_lines)

    dic_words = list_words_to_dic_words(list_words)

    dic_palindromes = find_palindromes(dic_words)


    new_window = tkinter.Tk()
    new_window.title("Functions for text files")
    new_window.geometry("300x300")

    # creating a button that lets the user access the display_palindromes function and its output
    # Note: using a lambda, otherwise just command = display_palindromes(dic_palindromes) just calls the function immediately
    # instead of allowing the arguments to be passed to the function once the button in clicked.
    palindrome_button = tkinter.Button( new_window, text ="Palindromes", command = lambda: display_palindromes(dic_palindromes) )
    palindrome_button.pack(pady = 10)

    # creating a button which allows the user access to the display_all _words funtion and its output.
    display_all_words_button = tkinter.Button( new_window, text = "Display all words", command = lambda: display_all_words(dic_words) )
    display_all_words_button.pack(pady=10)

    prompt_user = tkinter.Label(new_window, text= "Enter word to search for: ")
    prompt_user.pack()

    # creating an entry bar so that the user can enter what word to search for, which is then passed on to the word_search function.
    user_word_entry = tkinter.Entry(new_window)
    user_word_entry.pack()

    # creatin a button which allows the user to access the word_search function and its output
    word_search_button = tkinter.Button (new_window, text = "Search", command = lambda: word_search(user_word_entry, dic_words, actual_file) )
    word_search_button.pack()

    new_window.mainloop()


my_button = tkinter.Button(mywindow, text='Confirm', command = assign_file)
my_button.pack()

mywindow.mainloop()
