from tkinter import (
    Frame, BOTH, Label, W, LEFT, Y
)


class MetroQuoteContainer(Frame):
    CONTENT_BACKGROUND = "#eeeeee"
    CONTENT_PADDING = 10
    LEFT_BORDER_COLOR = "#555555"
    LEFT_BORDER_WIDTH = 6

    def __init__(self, master=None, text=None):
        Frame.__init__(self, master, background=self.CONTENT_BACKGROUND)
        Frame(self, background=self.LEFT_BORDER_COLOR, width=self.LEFT_BORDER_WIDTH).pack(side=LEFT, fill=Y)

        self.body = Frame(self, background=self.CONTENT_BACKGROUND, padx=self.CONTENT_PADDING, pady=self.CONTENT_PADDING)
        self.body.pack(expand=True, fill=BOTH)

        if text is not None:
            Label(self.body, text=text).pack(anchor=W)
