"""
This is the file that anyone exploring this project should run.

"""

import Tkinter as tkinter
from Textfile_functions import *

mywindow = tkinter.Tk()
mywindow.title("Welcome")
mywindow.geometry("400x400")

prompt_user = tkinter.Label(mywindow, text= "Enter file name: ")
prompt_user.pack()

user_file_name = tkinter.Entry(mywindow)
user_file_name.pack()

def display_palindromes(dic_palindromes):

    list_keys = dic_palindromes.keys()
    list_keys.sort

    palindrome_window = tkinter.Tk()
    palindrome_window.title("Palindromes")
    palindrome_window.geometry("300x300")

    scrollbar = tkinter.Scrollbar(palindrome_window)
    scrollbar.pack(side = "right", fill = tkinter.Y)

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

    listbox = tkinter.Listbox(all_words_window, borderwidth = 0, yscrollcommand = scrollbar.set)

    for key in list_keys:

        value = str(dic_words[key])
        y = "%s   : %s "  %(key, value)
        listbox.insert(tkinter.END, y)

    listbox.pack(side ="left" , fill = tkinter.BOTH)
    scrollbar.config(command = listbox.yview)

    all_words_window.mainloop()


current_word = ""
def word_search(user_word_entry, dic_words, list_lines, actual_file):

    current_word = user_word_entry.get()
    key = current_word.lower()

    word_search_window = tkinter.Tk()
    word_search_window.title("Word search results")
    word_search_window.geometry("300x300")

    if key in dic_words:
         value = str(dic_words[key])
         search_results =  "The word %s appears in the textfile %s a total of %s times"  %(key, actual_file, value)
         word_search_results = tkinter.Label (word_search_window, text = search_results)
         word_search_results.pack()

         line_index = 0

         for line in list_lines:

             if key in line:
                 line_number = str(line_index)
                 print "The word %s appears in line %s" %(key, line_number)
         line_index += 1



    else:
         search_results = "The word %s does not appear in the textfile %s" %(key, actual_file)
         word_search_results = tkinter.Label(word_search_window, text = search_results)
         word_search_results.pack()



actual_file = ""

def assign_file():

    actual_file = user_file_name.get()

    print "The current file is: " + str(actual_file)

    list_lines = file_to_list_strings(actual_file)

    list_words = list_strings_to_list_words(list_lines)

    dic_words = list_words_to_dic_words(list_words)

    dic_letters = list_words_to_dic_letters(list_words)

    dic_palindromes = find_palindromes(dic_words)

    new_window = tkinter.Tk()
    new_window.title("Functions for text files")
    new_window.geometry("300x300")

    palindrome_button = tkinter.Button( new_window, text ="Palindromes", command = lambda: display_palindromes(dic_palindromes) )
    # Note, using a lambda otherwise just command = display_palindromes(dic_palindromes) just calls the function immediately
    palindrome_button.pack(pady = 10)

    display_all_words_button = tkinter.Button( new_window, text = "Display all words", command = lambda: display_all_words(dic_words) )
    display_all_words_button.pack(pady=10)

    prompt_user = tkinter.Label(new_window, text= "Enter word to search: ")
    prompt_user.pack()

    user_word_entry = tkinter.Entry(new_window)
    user_word_entry.pack()

    word_search_button = tkinter.Button (new_window, text = "Search", command = lambda: word_search(user_word_entry, dic_words, list_lines, actual_file) )
    word_search_button.pack()

    new_window.mainloop()


my_button = tkinter.Button(mywindow, text='Confirm', command = assign_file)
my_button.pack()

mywindow.mainloop()
