#message box in python 
from tkinter import *
from tkinter import messagebox 

window=Tk()
def run():
     # messagebox.showinfo(title='error 404',message='error 404') shows error 404 message
     # messagebox.showwarning(title='scam',message='can hack your device') shows a exclamation sign and displays the message
     # messagebox.showerror(title='scam',message='can hack your device')
     #if messagebox.askokcancel(title='ask ok canel',message='do u want to do it?'):
     #    print("yes u did it")
     #else :
     #   print("u didnt do it")
     
     #there are similar messages like askretrycancel
     answer=messagebox.askyesnocancel(title='yes no cancel',message='do u want to continue')
     if answer==True:
      print("u continued")
     elif answer== False:
         print("u did not continue")
     else:
         print("u didnt answer")
button=Button(window,text='click me',command=run)
button.pack()
window.mainloop() 
 