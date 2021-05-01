from interface.component_filters.category_filter_option_menu import CategoryFilterOptionMenu
from interface.component_filters.tk_common_widgets import TkCommonWidgets
from interface.component_filters.constants import DEFAULT_BACKGROUND_COLOR
from tkinter import Frame, TOP, FLAT, X

from interface.search.addon_menu_container import AddonMenuContainer
from interface.search.search_progress_bar_container import SearchProgressBarContainer


class SearchContainer(Frame):
    def __init__(self, root_container):
        Frame.__init__(self, root_container, relief=FLAT, background=DEFAULT_BACKGROUND_COLOR)
        self.pack(side=TOP, fill=X)

        # note: CategoryMenuContainer
        self.category_menu = CategoryFilterOptionMenu(self)

        # note: ProgressBarContainer
        self.search_progress_bar = SearchProgressBarContainer(self)

        # note: AddonMenuContainer:
        self.addon_menu = AddonMenuContainer(self)

