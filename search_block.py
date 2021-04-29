from component_filters.category_filter_option_menu import CategoryFilterOptionMenu
from component_filters.constants import DEFAULT_BACKGROUND_COLOR
from tkinter import *


class SearchBlock(object):
    def __init__(self, root):
        self.root = root
        f = Frame(self.root, height=1, bg='grey', relief=FLAT)
        f.pack(fill=X)

        self.filter_search_block = Frame(self.root, relief=FLAT, background=DEFAULT_BACKGROUND_COLOR)
        self.filter_search_block.pack(side=TOP, fill=X)

        self.category_menu = CategoryFilterOptionMenu(root=self.filter_search_block)


