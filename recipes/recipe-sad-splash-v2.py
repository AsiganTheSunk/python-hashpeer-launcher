# new a splash screen, 80% of display screen size, centered,
# displaying a GIF image with needed info, disappearing after 5 seconds

from PIL import ImageTk, Image
from tkinter import *
from tkinter.ttk import *
from tkinter.ttk import Progressbar
from tkinter import Frame, Canvas, HORIZONTAL, NW, FLAT, BOTH, Tk

root = Tk()
# show no frame
root.overrideredirect(True)
_width = root.winfo_screenwidth()
_height = root.winfo_screenheight()

width = 400
height = 800
print(_width, _height)
print(width * 0.8, height * 0.8, _width * 0.415, _height * 0.15)

root.geometry('%dx%d+%d+%d' % (width, height, _width * 0.42, _height * 0.15))
spath = "../Kong Skull Island_Film_Poster.png"

from PIL import ImageTk, Image

simg = ImageTk.PhotoImage(Image.open(spath))
canvas = Canvas(root, height=height - 30, width=width, bg='#F0F8FF')
canvas.create_image(width / 2, height / 2, image=simg)
canvas.pack()

progressbar_canvas = Canvas(root, relief=FLAT, background="#D2D2D2")
progressbar = Progressbar(progressbar_canvas, orient=HORIZONTAL, length=width - 2, mode="indeterminate",
                          variable=width*0.8)
# The first 2 new window argvs control where the progress bar is placed
progressbar_canvas.create_window(1, 1, anchor=NW, window=progressbar)
progressbar_canvas.pack(fill=BOTH, expand=1)

frame = Frame(root, background="#D2D2D2")
frame.pack()
# show the splash screen for 5000 milliseconds then destroy


root.after(5000, root.destroy)
root.mainloop()

# your console program can start here ...
print("How did you like my informative splash screen?")
