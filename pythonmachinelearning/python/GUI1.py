#graphical user inerface for python 
#GUI in python is a simple program to demonstrate the use of tkinter library
#tkinter is a standard GUI toolkit in python
# widgets are the elements of GUI like buttons , labels , text boxes etc 
# windows are the containers for widgets

from tkinter import * #imports whole tkinter library
window = Tk() #creates a window object
#to display the window we need to call the mainloop() method

#GUI methods 

#we can change the size of the windows using geometry method
window.geometry("500x500") #sets the size of the window to 500x500 pixels

#we can change the title of the window using title method
window.title("GUI in Python") #sets the title of the window to "GUI in Python"  

#we can also change the icon of the window using the iconphoto method
#if we want our own icon we can use the path of the icon file by photoimage method
icon= PhotoImage(file='val.png') #loads the icon file
window.iconphoto(True,icon) #sets the icon of the window to the loaded icon file

#we can change the background color of the window using the config method
window.config(bg="lightblue") #sets the background color of the window to light blue

#label is widget that is used to display text or image 
label=Label(window,text='Hi ')#the first argument is the parent window 
#the second argument is the text to be displayed
label.pack() #adds the label to the window

#we can change the cordinates of the label using the place method
label.place(x=200,y=200) #sets the position of the label to (200,200) pixels

#we can also change the font of the label using the font method
label.config(font=("Arial", 20, "bold")) #sets the font of the label to Arial, size 20, bold
#we can also change the color of the label using the fg method
label.config(fg="green") #sets the color of the label to red
#we can also change the background color of the label using the bg method
label.config(bg="yellow") #sets the background color of the label to yellow
#we can also add a border to the label using the relief method and set the border width using the bd method
label.config(relief=RAISED) #sets the border style of the label to raised
label.config(bd=5) #sets the border width of the label to 5 pixels and width to 20 characters
#we can also add a padding to the label using the padx and pady methods
label.config(padx=10, pady=10) #sets the padding of the label to 10 pixels in x and y direction
#we can also add a background image to the label using the image method



window.mainloop() 




