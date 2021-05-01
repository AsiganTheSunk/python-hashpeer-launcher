from tkinter import Frame, SUNKEN, X
from interface.component_filters.constants import DEFAULT_BACKGROUND_COLOR


class SearchProgressBarContainer(Frame):
    def __init__(self, root_container):
        Frame.__init__(self, root_container, height=20, width=500, bg=DEFAULT_BACKGROUND_COLOR, relief=SUNKEN,
                       cursor="plus")
        self.pack(fill=X)
