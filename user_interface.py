import Tkinter as tkinter
from Project_functions import *
from GUI_functions import *

mywindow = tkinter.Tk()
mywindow.title("Functions for text files")
mywindow.geometry("400x400")


palindrome_button = tkinter.Button(text ="Palindromes", command = display_palindromes)
palindrome_button.pack()






mywindow.mainloop()
