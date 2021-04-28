from tkinter import *
from component_filters.constants import \
    DEFAULT_FONT_STYLE, DEFAULT_FONT_SIZE, DEFAULT_BACKGROUND_COLOR, DEFAULT_MOUSE_OVER_OPTION_MENU,\
    DEFAULT_DARK_BORDER, DEFAULT_TEXT_COLOR


# YEAR: self.option_menu = Combobox(self, textvariable=self.var, values=options)
class FrameOptionMenu(Frame):
    def __init__(self, root, status, *options, width=15):
        Frame.__init__(self, root, width=50, relief=FLAT, highlightcolor=DEFAULT_BACKGROUND_COLOR,
                       background=DEFAULT_BACKGROUND_COLOR, highlightbackground=DEFAULT_BACKGROUND_COLOR)
        self.selection = ''
        self.var = StringVar(root)
        self.set(status)
        self.var.trace('w', self.get)

        self.option_menu = OptionMenu(self, self.var, *options)
        self.option_menu.pack(side=LEFT, expand=True, fill=BOTH, padx=6, pady=2)
        self.option_menu.configure(font=(DEFAULT_FONT_STYLE, DEFAULT_FONT_SIZE), width=width,
                                   highlightthickness=0, relief=FLAT, justify=CENTER,
                                   bg=DEFAULT_BACKGROUND_COLOR, activebackground=DEFAULT_MOUSE_OVER_OPTION_MENU,
                                   fg=DEFAULT_TEXT_COLOR, activeforeground=DEFAULT_TEXT_COLOR)

        self.option_menu['menu'].config(font=(DEFAULT_FONT_STYLE, DEFAULT_FONT_SIZE),
                                        bg=DEFAULT_BACKGROUND_COLOR, relief=FLAT, fg=DEFAULT_TEXT_COLOR,
                                        borderwidth=0, activebackground=DEFAULT_MOUSE_OVER_OPTION_MENU,
                                        activeborderwidth=4, activeforeground=DEFAULT_TEXT_COLOR)

        # todo: fix the container frame color when selected the option_menu widget
        # bug: it works, but it produces a visual glitch sometimes, other widget with
        #  similar behaviour might be interfering
        # todo: change this for style so it's active and not event of enter or leaving
        #self.bind("<Enter>", self.on_enter)
        # print('Menu Options:', self.option_menu['menu'].keys())
        # self.option_menu.bind("<Enter>", self.on_enter)
        # self.bind("<Leave>", self.on_leave())
        # self.option_menu.bind("<Leave>", self.on_leave)
        #self.option_menu.bind("<FocusOut>", self.on_leave)

    def on_enter(self, *args):
        self.configure(background=DEFAULT_MOUSE_OVER_OPTION_MENU)
        # self.option_menu.configure(background=DEFAULT_MOUSE_OVER_OPTION_MENU)

    def on_leave(self, *args):
        self.configure(background=DEFAULT_BACKGROUND_COLOR)
        self.option_menu.configure(background=DEFAULT_BACKGROUND_COLOR)

    def get(self, *args):
        print(f'< Get Option Menu: {self.var.get()} >')
        self.on_leave()
        return self.var.get()

    def set(self, text):
        print(f'< Set Option Menu: {text} >')
        self.var.set(text)
