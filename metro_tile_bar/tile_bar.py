# region Imports

from tkinter import (
    Frame, PhotoImage, Button, Tk, Label, LEFT, X, FLAT, NE, RIGHT, N
)
from os.path import abspath

from component_filters.constants import DEFAULT_TEXT_COLOR, DEFAULT_BACKGROUND_COLOR, DEFAULT_DARK_BACKGROUND_COLOR, \
    DEFAULT_MEDIUM_DARK_BACKGROUND_COLOR, DEFAULT_FONT_STYLE, DEFAULT_FONT_SIZE, DEFAULT_DIMMED_TEXT_COLOR, \
    DEFAULT_SELECTED_UNDER_SCORE_TAB, DEFAULT_SELECTED_AND_NOT_ACTIVE_UNDER_SCORE_TAB, DEFAULT_TITLE_BAR


class MetroTileBar:
    def __init__(self, root):
        self.root = root

        self.close_img = PhotoImage(file='./metro_tile_bar/static/image/close.png')
        self.close_mouse = PhotoImage(file='./metro_tile_bar/static/image/close_mouse.png')
        self.minimize_img = PhotoImage(file='./metro_tile_bar/static/image/minimize.png')
        self.minimize_mouse = PhotoImage(file='./metro_tile_bar/static/image/minimize_mouse.png')
        self.restore = PhotoImage(file='./metro_tile_bar/static/image/restore.png')
        self.restore_mouse = PhotoImage(file='./metro_tile_bar/static/image/restore_mouse.png')
        self.maximize = PhotoImage(file='./metro_tile_bar/static/image/maximize.png')
        self.maximize_mouse = PhotoImage(file='./metro_tile_bar/static/image/maximize_mouse.png')

        self.title_bar = Frame(self.root, bg=DEFAULT_TITLE_BAR, highlightthickness=0)
        self.title_bar.pack(fill=X, anchor=N)

        self.title_bar.bind('<Button-1>', self.update_last_click_pos)
        self.title_bar.bind('<B1-Motion>', self.drag)
        self.title_bar.bind("<Button-3>", self.show_screen)
        self.title_bar.bind("<Map>", self.screen_appear)

        # w = Label(self.title_bar, text=" # ", bg=DEFAULT_BACKGROUND_COLOR, fg=DEFAULT_TEXT_COLOR)
        # w.pack(padx=2, pady=0, side=LEFT)
        #
        # w = Label(self.title_bar, text=' File ', bg=DEFAULT_BACKGROUND_COLOR, fg=DEFAULT_TEXT_COLOR)
        # w.pack(padx=1, pady=0, side=LEFT)
        #
        # w = Label(self.title_bar, text=' About ', bg=DEFAULT_BACKGROUND_COLOR, fg=DEFAULT_TEXT_COLOR)
        # w.pack(padx=1, pady=0, side=LEFT)

        w = Label(self.title_bar, text='  Hashpeer v0.2a  ', bg=DEFAULT_BACKGROUND_COLOR, fg=DEFAULT_DIMMED_TEXT_COLOR)
        w.pack(padx=1, pady=0, side=LEFT)

        self.close_button = Button(self.title_bar, image=self.close_img, bd=0, bg=color2,
                                   activebackground=color2, command=self.root.destroy)
        self.close_button.pack(side=RIGHT)
        self.close_button.bind("<Enter>", self.close_h)
        self.close_button.bind("<Leave>", self.close_l)

        self.maximize_button = Button(self.title_bar, image=self.maximize, bd=0, bg=color2,
                                      activebackground=color2, command=self.maximize)
        self.maximize_button.bind("<Enter>", self.maximize_h)
        self.maximize_button.bind("<Leave>", self.maximize_l)

        self.restore_button = Button(self.title_bar, image=self.restore, bd=0, bg=color2,
                                     activebackground=color2, command=self.restore)
        self.restore_button.pack(side=RIGHT)
        self.restore_button.bind("<Enter>", self.restore_h)
        self.restore_button.bind("<Leave>", self.restore_l)

        self.minimize_button = Button(self.title_bar, image=self.minimize_img, bd=0, bg=color2,
                                      activebackground=color2, command=self.hide_screen)
        self.minimize_button.pack(side=RIGHT)
        self.minimize_button.bind("<Enter>", self.minimize_h)
        self.minimize_button.bind("<Leave>", self.minimize_l)

        self.last_click_y = 0
        self.last_click_x = 0

    def update_last_click_pos(self, event):
        self.last_click_x = event.x
        self.last_click_y = event.y

    def drag(self, event):
        x, y = event.x - self.last_click_x + self.root.winfo_x(), event.y - self.last_click_y + self.root.winfo_y()
        self.root.geometry("+%s+%s" % (x, y))

    def close_h(self, event):
        self.close_button.config(image=self.close_mouse)

    def close_l(self, event):
        self.close_button.config(image=self.close_img)

    def maximize(self):
        pass
        # self.root.geometry("1366x728+0+0")
        # self.title_bar.config(width=1366)
        # self.maximize_button.place_forget()
        # self.close_button.place(x=1320, y=0)
        # self.minimize_button.place(x=1228, y=0)

    def maximize_h(self, event):
        self.maximize_button.config(image=self.maximize_mouse)

    def maximize_l(self, event):
        self.maximize_button.config(image=self.maximize)

    def restore(self):
        pass
        # self.root.geometry("1100x696+90+25")
        # self.title_bar.config(width=1100)
        # self.close_button.place(x=1054, y=0)
        # self.maximize_button.place(x=1008, y=0)
        # self.minimize_button.place(x=962, y=0)

    def restore_h(self, event):
        self.restore_button.config(image=self.restore_mouse)

    def restore_l(self, event):
        self.restore_button.config(image=self.restore)

    def show_screen(self, event):
        self.root.overrideredirect(True)
        self.root.deiconify()

    def hide_screen(self):
        self.root.overrideredirect(False)
        self.root.iconify()

    def screen_appear(self, event):
        self.root.overrideredirect(True)

    def minimize_h(self, event):
        self.minimize_button.config(image=self.minimize_mouse)

    def minimize_l(self, event):
        self.minimize_button.config(image=self.minimize_img)


color1 = '#252526'
color2 = '#3c3c3c'
color3 = '#1e1e1e'
color4 = '#cccccc'
color5 = '#333333'
color6 = '#2A2D2E'

# win = Tk()
# win.overrideredirect(1)
# win.config(bg=color3)
# win.config(highlightbackground=color2)
# win.geometry("1366x728+0+0")
# win.title("Calculator")
# win.iconbitmap('./metro_tile_bar/static/image/wd.ico')
# #
# custom_tile_bar = MetroTileBar(win)
# win.mainloop()


