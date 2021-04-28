from tkinter import *
root = Tk()
def clicked(event):
    print("pressed")
canvas1 = Canvas(root, relief = FLAT, background = "#D2D2D2")
canvas1.pack()
buttonBG = canvas1.create_rectangle(0, 0, 100, 30, fill="grey40", outline="grey60")
buttonTXT = canvas1.create_text(50, 15, text="click")
canvas1.tag_bind(buttonBG, "<Button-1>", clicked) ## when the square is clicked runs function "clicked".
canvas1.tag_bind(buttonTXT, "<Button-1>", clicked) ## same, but for the text.
root.mainloop()