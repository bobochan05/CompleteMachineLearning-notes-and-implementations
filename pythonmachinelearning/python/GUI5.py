#how to create a sliding scale in python 
from tkinter import *
window=Tk()
def submit():
    print(f"the current temp is : {scale.get()} degree celcius")
scale=Scale(window , 
            from_=1000,
            to=-273 ,
            length=1273,
            orient='horizontal',#the orient keyword allows us to orient the scale
            font=('arial',10,'bold',),
            tickinterval=50,#it creates a gap of 20 units
            troughcolor='black', #the slide colour is now black 
            fg='red'
            )
scale.pack(side='left')
button = Button(window, text='submit',command=submit )
button.pack(side='right')
window.mainloop()

