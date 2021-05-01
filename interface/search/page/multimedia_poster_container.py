from interface.component_filters.constants import DEFAULT_BACKGROUND_COLOR
from interface.component_filters.tk_image_utils import TkImageUtils
from tkinter import (
    Frame, Label, SOLID, BOTH, LEFT
)


class MultimediaPosterContainer(Frame):
    def __init__(self, root_container, image_path=None, width=200, height=300, background='Grey'):
        Frame.__init__(self, root_container, width=width, height=height, background=background,
                       relief=SOLID, cursor="plus")
        self.pack(padx=2, pady=2, fill=BOTH, side=LEFT)
        self.image_path = image_path

        if image_path is None:
            self.poster_image = \
                TkImageUtils.load_image('./interface/resources/static/image/placeholder/poster_placeholder.png')
        else:
            self.poster_image = \
                TkImageUtils.load_image(image_path)

        self.poster_container = Label(self, width=198, height=271, relief='solid')
        self.poster_container.configure(borderwidth=1, highlightbackground=DEFAULT_BACKGROUND_COLOR,
                                        image=self.poster_image)
        self.poster_container.pack(padx=2, pady=2)

