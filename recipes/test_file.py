


from tkinter import *

root = Tk()
root.title("Calculate")

# Create a Tkinter variable
tkvar = StringVar(root)

# Dictionary with options
choices = sorted({'Good', 'Bad', 'Medium'})
tkvar.set('Good')  # set the default option

popupMenu = OptionMenu(root, tkvar, *choices)
Label(root, text="Please choose").grid(row=2, column=2)
popupMenu.grid(row=3, column=2)
b2 = Button(root, text='Close', command=root.quit)
b2.grid(row=6, column=2)

# on change dropdown value
def change_dropdown(*args):
    global dropdown
    dropdown = str(tkvar.get())
    print(dropdown)

    if tkvar.get() == 'Good':
        print(5)

    if tkvar.get() == "Bad":
        print(10)

# link function to change dropdown
tkvar.trace('w', change_dropdown)

root.mainloop()