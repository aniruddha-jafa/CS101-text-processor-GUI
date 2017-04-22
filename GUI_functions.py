import Tkinter as tkinter

from Project_functions import *


def display_palindromes():

    global dic_palindromes

    list_keys = dic_palindromes.keys()
    list_keys.sort
    print list_keys
    
    palindrome_window = tkinter.Tk()
    palindrome_window.title("Palindromes")
    palindrome_window.geometry("300x300")

    test_label = tkinter.Label(palindrome_window, text = "testing")
    test_label.pack()



    for key in list_keys:

        label_key = tkinter.Label(palindrome_window, text = key)
        label_key.pack()

    palindrome_window.mainloop()
