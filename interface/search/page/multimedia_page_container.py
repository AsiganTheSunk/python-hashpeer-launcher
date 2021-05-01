from interface.components.multi_column.multicolumn_list_container import MultiColumnListBox
from interface.search.page.multimedia_poster_container import MultimediaPosterContainer
from interface.search.page.multimedia_magnet_information_container import MultimediaMagnetInformationContainer
from interface.component_filters.tk_common_widgets import TkCommonWidgets
from interface.components.metro_ui.metro_quote_container import MetroQuoteContainer
from interface.components.metro_ui.metro_label_containter import MetroLabelContainer
from interface.search.page.multimedia_download_container import MultimediaDownloadContainer
from interface.search.page.multimedia_information_container import MultimediaInformationContainer
from interface.component_filters.constants import (
    DEFAULT_TEXT_COLOR, DEFAULT_BACKGROUND_COLOR, DEFAULT_DARK_BACKGROUND_COLOR,
    DEFAULT_FONT_STYLE, DEFAULT_FONT_SIZE, DEFAULT_SELECTED_UNDER_SCORE_TAB,
    DEFAULT_SELECTED_AND_NOT_ACTIVE_UNDER_SCORE_TAB
)
from tkinter import (
    Frame, Label, NW, BOTH, LEFT, RIGHT, SUNKEN, BOTTOM, X, TOP
)


class MultimediaPageContainer(Frame):
    def __init__(self, root_container):
        Frame.__init__(self, root_container)
        self.pack(side=TOP, fill=X)
        self.root_container = root_container

    @staticmethod
    def on_select_entry(magnet_data):
        name, seed, leech, size = magnet_data
        print(f'clicked: {name}, {seed}, {leech}, {size}')
        return name, seed, leech, size

    def add_entry(self, magnet_data):
        self.magnet_list_box.insert_row([*magnet_data])

    @staticmethod
    def init_metro_text_label(root_container, text):
        for _text in text:
            metro_text_label = Label(root_container, text=_text)
            metro_text_label.pack(anchor=NW)

    @staticmethod
    def init_directors_quote_frame(container_body, directors=''):
        metro_quote_container = MetroQuoteContainer(container_body, text=f'Director: {directors}')
        metro_quote_container.pack(anchor=NW)

    @staticmethod
    def init_actors_quote_frame(container_frame, actors=''):
        metro_actors_quote_frame = MetroQuoteContainer(container_frame, text=f'Actors: {actors}')
        metro_actors_quote_frame.pack(anchor=NW)

    @staticmethod
    def init_title_label_frame(container_frame, title=''):
        metro_labelframe_container = MetroLabelContainer(container_frame, title=title.title())
        metro_labelframe_container.pack(fill=BOTH, side=LEFT, padx=2, pady=2, expand=True)
        return metro_labelframe_container

    def init_new_notebook_tab(self, background_color):
        self.configure(bg=background_color)

        multimedia_data_container = Frame(self, bg=DEFAULT_BACKGROUND_COLOR)
        multimedia_data_container.pack(padx=2, pady=2)

        MultimediaInformationContainer(multimedia_data_container)
        MultimediaPosterContainer(multimedia_data_container)

        self.search_block_result_containter = Frame(self, bg=DEFAULT_BACKGROUND_COLOR, relief=SUNKEN, cursor="plus")
        self.search_block_result_containter.pack(fill=X, padx=2, pady=1)

        self.magnet_list_box = \
            MultiColumnListBox(self.search_block_result_containter, ["Name", "Seeders", "Leechers", "Size"],
                               command=self.on_select_entry,
                               cell_anchor="center", cell_background=DEFAULT_BACKGROUND_COLOR,
                               heading_background=DEFAULT_BACKGROUND_COLOR,
                               heading_font=(DEFAULT_FONT_STYLE, DEFAULT_FONT_SIZE),
                               cell_font=(DEFAULT_FONT_STYLE, DEFAULT_FONT_SIZE),
                               selection_background=DEFAULT_SELECTED_UNDER_SCORE_TAB,
                               cell_foreground=DEFAULT_TEXT_COLOR, selection_foreground='white',
                               heading_foreground=DEFAULT_TEXT_COLOR,
                               field_background=DEFAULT_SELECTED_AND_NOT_ACTIVE_UNDER_SCORE_TAB)

        self.magnet_list_box.interior.pack(fill=BOTH, side=LEFT, pady=3, padx=2, expand=True)
        self.magnet_list_box.insert_row(["Tiny.Creatures.S01.1080p.NF.WEBRip.DDP5.1.x265", 8, 9, 10])
        self.magnet_list_box.insert_row(["Tiny.Creatures.S01.1080p.NF.WEBRip.DDP5.1.x264-ExREN[rartv]", 2, 3, 4])
        self.magnet_list_box.insert_row(["Tiny.Creatures.Season.01.1080p", 5, 6, 7])

        MultimediaMagnetInformationContainer(self.search_block_result_containter)
        TkCommonWidgets.horizontal_separator(self)
        MultimediaDownloadContainer(self)

        self.root_container.add(self, text=background_color)
