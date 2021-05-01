from interface.components.metro_ui.metro_button_container import MetroButtonContainer
from interface.component_filters.constants import (
    DEFAULT_TEXT_COLOR, DEFAULT_BACKGROUND_COLOR, DEFAULT_DARK_BACKGROUND_COLOR,
    DEFAULT_FONT_STYLE, DEFAULT_FONT_SIZE, DEFAULT_SELECTED_UNDER_SCORE_TAB,
    DEFAULT_SELECTED_AND_NOT_ACTIVE_UNDER_SCORE_TAB
)
from tkinter import (
    Frame, RIGHT, X, SE
)


class MultimediaDownloadContainer(Frame):
    def __init__(self, root_container):
        Frame.__init__(self, root_container, bg=DEFAULT_BACKGROUND_COLOR)
        self.pack(expand=True, anchor=SE, fill=X, padx=2)
        self.download_button = MetroButtonContainer(self, text=' [  Download  ] ',
                                                    background=DEFAULT_BACKGROUND_COLOR, foreground=DEFAULT_TEXT_COLOR)
        self.download_button.pack(side=RIGHT)

        self.settings_button = MetroButtonContainer(self, text='...',
                                                    background=DEFAULT_BACKGROUND_COLOR, foreground=DEFAULT_TEXT_COLOR)
        self.settings_button.pack(side=RIGHT)
