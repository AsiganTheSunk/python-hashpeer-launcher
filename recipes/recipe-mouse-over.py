from tkinter import *

root = Tk()

b = Button(root, text='foo')
b.pack()

def enterB(event):
   b.configure(text='bar', background='red')
   b.configure(activebackground='red')

def leaveB(event):
    b.configure(text="foo", background="SystemButtonFace")


b.bind('<Enter>', enterB)
b.bind('<Leave>', leaveB)

root.mainloop()