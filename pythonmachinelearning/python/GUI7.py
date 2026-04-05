#how to add a multi colour chooser in python 
#for multi colour choosing we need to import another submodule
from tkinter import *
from tkinter import colorchooser
window=Tk()
def set():
    color=colorchooser.askcolor()
    chex=color[1]
    window.config(bg=chex)
    print(color)
    
button=Button(window,text='set colour',command=set)
button.pack()

window.mainloop()