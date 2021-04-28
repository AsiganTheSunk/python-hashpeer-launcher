try:
    import Tkinter as tk
    import ttk
except ImportError:  # Python 3
    import tkinter as tk
    from tkinter import ttk


from components.closable_notebook.style_closable_notebook import set_icon_images, set_style
from component_filters.constants import DEFAULT_TEXT_COLOR, DEFAULT_BACKGROUND_COLOR, \
    DEFAULT_FONT_STYLE, DEFAULT_FONT_SIZE


class ClosableNotebook(ttk.Notebook):
    """
    https://stackoverflow.com/questions/39458337/is-there-a-way-to-add-close-buttons-to-tabs-in-tkinter-ttk-notebook
    A ttk Notebook with close buttons on each tab
    """

    __initialized = False

    def __init__(self, *args, **kwargs):
        if not self.__initialized:
            self.images = set_icon_images()
            set_style()
            # self.__initialize_custom_style()
            self.__inititialized = True

        kwargs["style"] = "CustomNotebook"
        ttk.Notebook.__init__(self, *args, **kwargs)

        self._active = None

        self.bind("<ButtonPress-1>", self.on_close_press, True)
        self.bind("<ButtonRelease-1>", self.on_close_release)

    def on_close_press(self, event):
        """Called when the button is pressed over the close button"""

        element = self.identify(event.x, event.y)

        if "close" in element:
            index = self.index("@%d,%d" % (event.x, event.y))
            self.state(['pressed'])
            self._active = index

    def on_close_release(self, event):
        """Called when the button is released over the close button"""
        if not self.instate(['pressed']):
            return

        element = self.identify(event.x, event.y)
        index = self.index("@%d,%d" % (event.x, event.y))

        if "close" in element and self._active == index:
            self.forget(index)
            self.event_generate("<<NotebookTabClosed>>")

        self.state(["!pressed"])
        self._active = None


# if __name__ == "__main__":
#     root = tk.Tk()
#
#     notebook = ClosableNotebook(width=200, height=200)
#     notebook.pack(side="top", fill="both", expand=True)
#
#     for color in ("red", "orange", "green", "blue", "violet"):
#         frame = tk.Frame(notebook, background=color)
#         notebook.add(frame, text=color)
#
#     root.mainloop()
