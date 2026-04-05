#entry widget is a tool for user input in window 
from tkinter import *    
window=Tk()
entry= Entry(window ,show='*')
entry.pack(side='left')

def display():
    username=entry.get()#this is used to return the text
    print(f"hello {username} good morning")
    
def delete():
    entry.delete(0,END)
    
def backspace():
    entry.delete(len(entry.get())-1,END)
 
#making a program where a user inputs him name in GUI and computer says hello
button = Button(window,text='submit',command=display)
#we can also add a delete and a backspace button
delete = Button(window,text='delete',command=delete)
backspace = Button(window,text='backspace',command=backspace)

button.pack(side='right')
delete.pack(side='right')
backspace.pack(side='right')
label=Label(window,text='enter your name')
label.pack(side='top')
#we can also use the option known as show to hide and show some other character
#eg if we type in password
window.geometry('300x300')
window.mainloop()


