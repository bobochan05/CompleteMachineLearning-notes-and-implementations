# Checkboxes and radioboxes in GUI window
from tkinter import *


i = int(input("Enter 1 for checkboxes and 2 for radioboxes: "))
window=Tk()

match i:
    case 1:
        def run():
            if x.get() == 1:
                print("u agreed")
            else:
                print("u didnt agree")

        x = IntVar()
        button = Button(window, text='submit', command=run)
        button.pack(side='right')

        check = Checkbutton(window, text='click me', variable=x, font=('Arial', 20))
        check.pack(side='left')
        
        window.mainloop()

    case 2:
        # Radio buttons like MCQs (only one can be selected)
        food = ["pizza", "pasta", "biriyani"]
        x = IntVar()
        for index in range(len(food)):
            radiobutton = Radiobutton(
                window,
                text=food[index],
                variable=x,
                value=index,
                font=('Arial', 30)
            )
            radiobutton.pack(anchor=W)
        window.mainloop()