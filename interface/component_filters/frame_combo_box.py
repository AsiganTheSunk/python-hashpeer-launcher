from tkinter import *
from tkinter.ttk import Combobox
from component_filters.constants import \
    DEFAULT_FONT_STYLE, DEFAULT_FONT_SIZE, DEFAULT_BUTTON_COLOR


# YEAR: self.option_menu = Combobox(self, textvariable=self.var, values=options)
class FrameCombobox(Frame):
    def __init__(self, root, status, *options, width=12):
        Frame.__init__(self, root, width=30, relief=SOLID, borderwidth=1, background=DEFAULT_BUTTON_COLOR)
        self.selection = ''
        self.var = StringVar(root)
        self.set(status)
        self.var.trace('w', self.get)

        self.option_menu = Combobox(self, self.var, options)
        self.option_menu.pack(side=LEFT, expand=True, fill=BOTH, padx=6, pady=2)
        self.option_menu.configure(font=(DEFAULT_FONT_STYLE, DEFAULT_FONT_SIZE, 'bold'), width=width,
                                   highlightthickness=0, relief=FLAT, justify=CENTER,
                                   bg=DEFAULT_BUTTON_COLOR, activebackground=DEFAULT_BUTTON_COLOR,
                                   fg='white', activeforeground='white')

        self.option_menu['menu'].config(font=(DEFAULT_FONT_STYLE, DEFAULT_FONT_SIZE, 'bold'),
                                        bg='white', relief=FLAT, bd=0,
                                        borderwidth=0, activebackground=DEFAULT_BUTTON_COLOR,
                                        activeborderwidth=4, activeforeground='white')

    def get(self, *args):
        print(f'< Get Option Menu: {self.var.get()} >')
        return self.var.get()

    def set(self, text):
        print(f'< Set Option Menu: {text} >')
        self.var.set(text)