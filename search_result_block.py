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

from component_filters.tk_common_widgets import TkCommonWidgets
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


class SearchResultBlock(object):
    def __init__(self, root):
        self.root = root
        self.root_container_frame = Frame(root)
        self.root_container_frame.pack(fill=BOTH)

        # note: ProgressBarFrameContainer
        self.progressbar_frame_container = Frame(self.root_container_frame, height=20, width=500,
                                                 bg=DEFAULT_BACKGROUND_COLOR, relief=SUNKEN, cursor="plus")
        self.progressbar_frame_container.pack(fill=X)

        # note: AddonMenuContainer:
        TkCommonWidgets.horizontal_separator(self.root_container_frame)
        self.addon_menu_container = Frame(self.root_container_frame, height=40, width=500, bg=DEFAULT_BACKGROUND_COLOR)
        self.addon_menu_container.pack(fill=X)
        self.init_addon_metro_button(self.addon_menu_container, 'Search Results')
        self.init_addon_metro_button(self.addon_menu_container, 'Audio Align')
        self.init_addon_metro_button(self.addon_menu_container, 'File Mapper')
        TkCommonWidgets.horizontal_separator(self.root_container_frame)

        # note: ClosableNotebook:
        notebook = ClosableNotebook()
        notebook.pack(side=TOP, fill=BOTH, expand=True, padx=6, pady=6)

        for color in (DEFAULT_BACKGROUND_COLOR, DEFAULT_BACKGROUND_COLOR, DEFAULT_BACKGROUND_COLOR):
            self.init_new_notebook_tab(notebook, color)

    @staticmethod
    def on_select_entry(magnet_data):
        name, seed, leech, size = magnet_data
        print(f'clicked: {name}, {seed}, {leech}, {size}')
        return name, seed, leech, size

    @staticmethod
    def init_addon_metro_button(root_container, text):
        metro_functionality_button = Metro_Button(root_container, text=text, background=DEFAULT_BACKGROUND_COLOR,
                                                  foreground=DEFAULT_TEXT_COLOR)
        metro_functionality_button.pack(padx=10, pady=5, side=LEFT)

    def add_entry(self, magnet_data):
        self.magnet_list_box.insert_row([*magnet_data])

    @staticmethod
    def init_metro_text_label(root_container, text):
        for _text in text:
            metro_text_label = Label(root_container, text=_text)
            metro_text_label.pack(anchor=NW)

    @staticmethod
    def init_directors_quote_frame(container_body, directors=''):
        metro_directors_quote_frame = QuoteFrame(container_body, text=f'Director: {directors}')
        metro_directors_quote_frame.pack(anchor=NW)

    @staticmethod
    def init_actors_quote_frame(container_frame, actors=''):
        metro_actors_quote_frame = QuoteFrame(container_frame, text=f'Actors: {actors}')
        metro_actors_quote_frame.pack(anchor=NW)

    @staticmethod
    def init_title_label_frame(container_frame, title=''):
        metro_labelframe_container = Metro_LabelFrame(container_frame, title=title.title())
        metro_labelframe_container.pack(fill=BOTH, side=LEFT, padx=2, pady=2, expand=True)
        return metro_labelframe_container

    @staticmethod
    def add_settings_and_download_buttons(root_container):
        metro_download_button = Metro_Button(root_container, text=' [  Download  ] ',
                                             background=DEFAULT_BACKGROUND_COLOR, foreground=DEFAULT_TEXT_COLOR)
        metro_download_button.pack(side=RIGHT)

        metro_settings_button = Metro_Button(root_container, text='...',
                                             background=DEFAULT_BACKGROUND_COLOR, foreground=DEFAULT_TEXT_COLOR)
        metro_settings_button.pack(side=RIGHT)

    def init_new_notebook_tab(self, notebook, color):
        notebook_frame_container = Frame(notebook, background=color)
        notebook_frame_container.pack(fill=BOTH)

        description_and_poster_frame_container = Frame(notebook_frame_container, height=300,
                                                       bg=DEFAULT_BACKGROUND_COLOR, relief=SUNKEN, cursor="plus")
        description_and_poster_frame_container.pack(fill=X, padx=2, pady=2)

        # note: MetroDescriptionContainer
        metro_description_container = self.init_title_label_frame(description_and_poster_frame_container, 'Tiny Creatures (2020)')

        # note: MetroDirectorQuoteFrame, MetroActorsQuoteFrame
        self.init_directors_quote_frame(metro_description_container.body)
        TkCommonWidgets.horizontal_separator(metro_description_container.body)
        self.init_actors_quote_frame(metro_description_container.body)

        # note: SeparatorBlock within Multimedia: Film, Show, Anime Description
        TkCommonWidgets.horizontal_separator(metro_description_container.body)
        TkCommonWidgets.horizontal_separator(metro_description_container.body, background_color=None, height=0, pady=4)
        TkCommonWidgets.horizontal_separator(metro_description_container.body)
        # note: VerticalSeparator: Description Container
        TkCommonWidgets.vertical_separator(metro_description_container.body)
        DESCRIPTION_TEXT = [LORE_IPSUM0, LORE_IPSUM0, LORE_IPSUM1, LORE_IPSUM1, LORE_IPSUM2, LORE_IPSUM2]
        self.init_metro_text_label(metro_description_container.body, DESCRIPTION_TEXT)

        data_frame = Frame(description_and_poster_frame_container, width=200, height=300, bg=DEFAULT_DARK_BACKGROUND_COLOR,
                           relief=SOLID, cursor="plus", padx=2, pady=2)
        data_frame.pack(side=LEFT)

        poster = SimplePosterBox(data_frame)
        poster.pack(fill=BOTH, side=LEFT)

        TkCommonWidgets.horizontal_separator(metro_description_container.body)
        self.search_block_result_containter = Frame(notebook_frame_container, bg=DEFAULT_BACKGROUND_COLOR,
                                                    relief=SUNKEN, cursor="plus")
        self.search_block_result_containter.pack(fill=X, padx=2, pady=2)

        self.magnet_list_box = \
            Multicolumn_Listbox(self.search_block_result_containter, ["Name", "Seeders", "Leechers", "Size"],
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

        data_frame = Frame(self.search_block_result_containter, width=460, height=300, bg=DEFAULT_BACKGROUND_COLOR,
                           relief=SUNKEN, cursor="plus")
        data_frame.pack(fill=BOTH, padx=2, pady=2)

        simple_data_box = SimpleDataBox(data_frame)
        simple_data_box.pack(fill=BOTH, side=RIGHT, pady=1)

        # note: RightLowerButtonFrameContainer: MetroDownloadButton, MetroSettingsButton
        right_lower_button_frame_container = Frame(notebook_frame_container, bg=DEFAULT_BACKGROUND_COLOR)
        right_lower_button_frame_container.pack(fill=X, side=BOTTOM)
        self.add_settings_and_download_buttons(right_lower_button_frame_container)
        TkCommonWidgets.horizontal_separator(notebook_frame_container)

        notebook.add(notebook_frame_container, text=color)
