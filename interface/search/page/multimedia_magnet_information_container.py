from interface.search.page.multimedia_banner_container import MultimediaBannerContainer
from interface.search.page.constants.magnet_information_constants import DEFAULT_MAGNET_INFORMATION
from interface.component_filters.constants import (
    DEFAULT_TEXT_COLOR, DEFAULT_BACKGROUND_COLOR, DEFAULT_MEDIUM_DARK_BACKGROUND_COLOR
)
from tkinter import (
    Frame, Text, DISABLED, NORMAL, END, X, SUNKEN, RIGHT, BOTH
)


class MultimediaMagnetInformationContainer(Frame):
    def __init__(self, root_container):
        Frame.__init__(self, root_container, width=456, height=300, bg=DEFAULT_BACKGROUND_COLOR,
                       relief=SUNKEN, cursor="plus")
        self.pack(fill=BOTH, side=RIGHT, pady=1)

        # note: MagnetInformationBoxContainer
        self.magnet_information_box_container = \
            Frame(self, width=456, height=250, background='#848482', highlightthickness=2,
                  highlightbackground=DEFAULT_MEDIUM_DARK_BACKGROUND_COLOR,
                  highlightcolor=DEFAULT_MEDIUM_DARK_BACKGROUND_COLOR)
        self.magnet_information_box_container.pack(fill=X)

        # note: BannerDisplayBoxContainer
        self.banner_display_box_container = MultimediaBannerContainer(self, width=456, height=50,
                                                                      background=DEFAULT_BACKGROUND_COLOR)
        self.banner_display_box_container.pack(fill=X, pady=3)

        # note: TextBoxContainer
        self.text_box_container = Text(self.magnet_information_box_container, bg=DEFAULT_BACKGROUND_COLOR,
                                       width=68, height=16, foreground=DEFAULT_TEXT_COLOR)
        self.text_box_container.pack(pady=2, padx=2)
        self.text_box_container.configure(font=('calibri', 10), relief='flat')

        self.init_magnet_information()

    def init_magnet_information(self):
        self.text_box_container.insert(END, DEFAULT_MAGNET_INFORMATION)
        self.text_box_container.config(state=DISABLED)

    def set_magnet_information(self, magnet_information):
        self.text_box_container.configure(state=NORMAL)
        self.text_box_container.delete('1.0', END)
        self.text_box_container.insert(END, magnet_information)
        self.text_box_container.configure(state=DISABLED)
