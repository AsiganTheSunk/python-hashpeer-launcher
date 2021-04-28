from component_filters.tk_utils import TkUtils
from tkinter import Tk, Frame, SUNKEN, BOTH, X, RIGHT, FLAT, BOTTOM, LEFT, TOP
from component_filters.category_filter_option_menu import CategoryFilterOptionMenu
from components.metro_ui.recipe_entry_metro_ui import Search_Box
from component_filters.constants import DEFAULT_TEXT_COLOR, DEFAULT_BACKGROUND_COLOR, DEFAULT_DARK_BACKGROUND_COLOR, \
    DEFAULT_MEDIUM_DARK_BACKGROUND_COLOR, DEFAULT_FONT_STYLE, DEFAULT_FONT_SIZE, DEFAULT_DIMMED_TEXT_COLOR, \
    DEFAULT_SELECTED_UNDER_SCORE_TAB, DEFAULT_SELECTED_AND_NOT_ACTIVE_UNDER_SCORE_TAB
from tkinter import *
from components.closable_notebook.recipe_closable_notebook import ClosableNotebook
from components.treeview_widget.recipe_treeview import Multicolumn_Listbox
from components.metro_ui.recipe_entry_metro_ui import Metro_LabelFrame, QuoteFrame
from components.metro_ui.recipe_entry_metro_ui import Metro_Button
from pack_testing import SimplePosterBox, SimpleDataBox
from display_box import DisplayBox

LORE_IPSUM0 = 'Lorem ipsum dolor sit amet consectetur adipiscing elit cursus arcu, lobortis elementum fusce tellus' \
             ' interdum morbi porta imperdiet facilisi, mauris sapien curabitur nullam.                  '
LORE_IPSUM1 = 'Ridiculus ultrices vehicula hac aenean parturient libero arcu erat turpis, est montes nostra ' \
              'aptent vel cum metus.'

LORE_IPSUM2 ='Vestibulum leo netus vulputate magnis interdum vel tincidunt lacinia, quam arcu praesent sed libero' \
             ' bibendum habitasse.'

SHOW_BORDER_COLOR = "pink"
FILM_BORDER_COLOR = "lightblue"
ANIME_BORDER_COLOR = "orange"
spath = "Kong Skull Island_Film_Poster.png"


class CustomTitleBar(object):
    lastClickX = 0
    lastClickY = 0

    def __init__(self, root):
        self.root = root

        def save_last_click_pos(event):
            global lastClickX, lastClickY
            lastClickX = event.x
            lastClickY = event.y

        def dragging(event):
            x, y = event.x - lastClickX + root.winfo_x(), event.y - lastClickY + root.winfo_y()
            root.geometry("+%s+%s" % (x, y))

        # make a frame for the title bar
        title_bar = Frame(self.root, bg=DEFAULT_BACKGROUND_COLOR, relief=FLAT, highlightthickness=0)

        w = Label(title_bar, text=" # ", bg=DEFAULT_BACKGROUND_COLOR, fg=DEFAULT_TEXT_COLOR)
        w.pack(padx=2, pady=0, side=LEFT)

        w = Label(title_bar, text=' File ', bg=DEFAULT_BACKGROUND_COLOR, fg=DEFAULT_TEXT_COLOR)
        w.pack(padx=1, pady=0, side=LEFT)

        w = Label(title_bar, text=' About ', bg=DEFAULT_BACKGROUND_COLOR, fg=DEFAULT_TEXT_COLOR)
        w.pack(padx=1, pady=0, side=LEFT)

        w = Label(title_bar, text='  Hashpeer v0.1a  ', bg=DEFAULT_BACKGROUND_COLOR, fg=DEFAULT_DIMMED_TEXT_COLOR)
        w.pack(padx=1, pady=0, side=LEFT)

        close_button_metro = Metro_Button(title_bar, text='  X  ', background=DEFAULT_BACKGROUND_COLOR,
                                          command=root.destroy)
        minimize_button_metro = Metro_Button(title_bar, text='  _  ', background=DEFAULT_BACKGROUND_COLOR,
                                             command=root.iconify)
        # pack the widgets
        title_bar.pack(expand=1, fill=X)
        # close_button.pack(side=RIGHT)
        close_button_metro.pack(side=RIGHT)
        close_button_metro.config(font=(DEFAULT_FONT_STYLE, DEFAULT_FONT_SIZE))

        minimize_button_metro.pack(side=RIGHT)
        minimize_button_metro.config(font=(DEFAULT_FONT_STYLE, DEFAULT_FONT_SIZE))
        title_bar.bind('<Button-1>', save_last_click_pos)
        title_bar.bind('<B1-Motion>', dragging)
