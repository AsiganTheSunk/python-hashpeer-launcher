from tkinter import (
    Frame, BOTH, W, Label, X
)


class MetroLabelContainer(Frame):
    HEADER_BACKGROUND = "#1ba1e2"
    HEADER_FOREGROUND = "white"
    CONTENT_BACKGROUND = "#e8f1f4"
    INNER_PADDING = 8

    FONT_HEADER = "TkDefaultFont"

    def __init__(self, root_container, title):
        Frame.__init__(self, root_container)

        header = Frame(self, background=self.HEADER_BACKGROUND, padx=self.INNER_PADDING, pady=self.INNER_PADDING)
        header.pack(fill=X)

        self._title = title
        self._title_label = Label(header, text=title, foreground=self.HEADER_FOREGROUND,
                                  background=self.HEADER_BACKGROUND, font=self.FONT_HEADER)
        self._title_label.pack(anchor=W)

        self.body = Frame(self, padx=self.INNER_PADDING, pady=self.INNER_PADDING, background=self.CONTENT_BACKGROUND)
        self.body.pack(expand=True, fill=BOTH)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title
        self._title_label.configure(text=title)
