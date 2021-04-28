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

spath = "Kong Skull Island_Film_Poster.png"


class SearchBlock(object):
    def __init__(self, root):
        self.root = root
        f = Frame(self.root, height=1, bg='grey', relief=FLAT)
        f.pack(fill=X)

        self.filter_search_block = Frame(self.root, relief=FLAT, background=DEFAULT_BACKGROUND_COLOR)
        self.filter_search_block.pack(side=TOP, fill=X)

        self.category_menu = CategoryFilterOptionMenu(root=self.filter_search_block)


