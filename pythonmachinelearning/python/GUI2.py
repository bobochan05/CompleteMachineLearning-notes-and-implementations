#how to add button in your window 
from tkinter import *
window = Tk()
def click():
    for n in range(11):
      print( f"the table of 4 is :{4*n} ")

icon=PhotoImage(file='click.png')
window.iconphoto(True,icon)

#to add a button in window you use the Button keyword 
button=Button(window,text="click me",command=click)#the first argument is the window in which you will display the button
button.pack()
#we can also change the font n other things in the argumnt 
#we can also add image to a button 
button.config(image=icon,compound='top')
window.geometry('1000x1000')


window.mainloop()

