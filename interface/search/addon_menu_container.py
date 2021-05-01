from interface.component_filters.constants import DEFAULT_TEXT_COLOR, DEFAULT_BACKGROUND_COLOR
from interface.components.metro_ui.metro_button_container import MetroButtonContainer
from interface.component_filters.tk_common_widgets import TkCommonWidgets
from tkinter import Frame, X, LEFT


class AddonMenuContainer:
    def __init__(self, root_container):
        TkCommonWidgets.horizontal_separator(root_container)
        addon_menu_container = Frame(root_container, height=40, width=500, bg=DEFAULT_BACKGROUND_COLOR)
        addon_menu_container.pack(fill=X)
        self.search_result_button = \
            self.init_addon_metro_button(addon_menu_container, 'Search Results')
        self.audio_align_button = \
            self.init_addon_metro_button(addon_menu_container, 'Audio Align')
        self.multimedia_file_mapper_button = \
            self.init_addon_metro_button(addon_menu_container, 'Multimedia File Mapper')
        TkCommonWidgets.horizontal_separator(root_container)

    @staticmethod
    def init_addon_metro_button(root_container, text):
        metro_functionality_button = \
            MetroButtonContainer(root_container, text=text,
                                 background=DEFAULT_BACKGROUND_COLOR, foreground=DEFAULT_TEXT_COLOR)
        metro_functionality_button.pack(padx=10, pady=5, side=LEFT)
        return metro_functionality_button
