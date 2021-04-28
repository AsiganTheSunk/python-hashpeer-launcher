from tkinter.ttk import Progressbar
from tkinter import Frame, Canvas, HORIZONTAL, NW, FLAT, BOTH, Tk


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        value_progress = 300
        self.parent.title("Progressbar Thingymawhatsit")
        self.config(bg='#F0F0F0')
        self.pack(fill=BOTH, expand=1)
        # new canvas
        canvas = Canvas(self, relief=FLAT, background="#D2D2D2",
                        width=400, height=10)

        progressbar = Progressbar(canvas, orient=HORIZONTAL,
                                  length=400, mode="indeterminate",
                                  variable=value_progress,

                                  )
        # The first 2 new window argvs control where the progress bar is placed
        canvas.create_window(1, 1, anchor=NW, window=progressbar)
        canvas.grid()


def main():
    root = Tk()
    root.geometry('500x50+10+50')
    app = Example(root)
    app.mainloop()


if __name__ == '__main__':
    main()
