#how to add a text area in python 
from tkinter import *
window=Tk()
text=Text(window )
text.pack()
def submit():
    input=text.get('1. 0',END)
    print(input)
button=Button(window,text='submit',command=submit)
button.pack()
window.mainloop() 