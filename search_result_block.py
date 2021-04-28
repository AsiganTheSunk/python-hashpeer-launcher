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


class SearchResultBlock(object):
    def __init__(self, root):
        self.root = root
        self.main_frame = Frame(root)
        # self.main_frame.pack(fill=BOTH, padx=1, pady=1)
        self.main_frame.pack(fill=BOTH)

        # todo: ?
        # search_frame = Frame(main_frame, height=120, width=500, bg=DEFAULT_BACKGROUND_COLOR,
        #                      relief=SUNKEN, cursor="plus")

        self.add_progress_bar()
        self.add_horizontal_separator()
        self.add_collapsable_menu()
        self.add_functionality_button('Search Results')
        self.add_functionality_button('Audio Align')
        self.add_functionality_button('File Mapper')
        self.add_horizontal_separator()

        notebook = ClosableNotebook()
        notebook.pack(side=TOP, fill=BOTH, expand=True, padx=6, pady=6)

        for color in (DEFAULT_BACKGROUND_COLOR, DEFAULT_BACKGROUND_COLOR, DEFAULT_BACKGROUND_COLOR):
            self.add_new_tab(notebook, color)

    @staticmethod
    def on_select_entry(magnet_data):
        name, seed, leech, size = magnet_data
        print(f'clicked: {name}, {seed}, {leech}, {size}')
        return name, seed, leech, size

    def add_collapsable_menu(self):
        self.collapsable_menu = Frame(self.main_frame, height=40, width=500, bg=DEFAULT_BACKGROUND_COLOR)
        self.collapsable_menu.pack(fill=X)

    def add_progress_bar(self):
        self.progressbar_frame = Frame(self.main_frame, height=20, width=500, bg=DEFAULT_BACKGROUND_COLOR,
                                  relief=SUNKEN, cursor="plus")
        self.progressbar_frame.pack(fill=X)

    def add_functionality_button(self, text):
        w = Metro_Button(self.collapsable_menu, text=text, background=DEFAULT_BACKGROUND_COLOR,
                         foreground=DEFAULT_TEXT_COLOR)
        w.pack(padx=10, pady=5, side=LEFT)

    def add_horizontal_separator(self):
        f = Frame(self.main_frame, height=1, bg='grey')
        f.pack(fill=X)

    def add_entry(self, magnet_data):
        self.magnet_list_box.insert_row([*magnet_data])

    def add_text_block(self, metro_labelframe, text):
        Label(metro_labelframe.body, text=text).pack(anchor=NW)

    def add_new_tab(self, notebook, color):
        frame = Frame(notebook, background=color)
        frame.pack(fill=BOTH)

        description_and_poster_frame = Frame(frame, height=300, bg=DEFAULT_BACKGROUND_COLOR,
                                             relief=SUNKEN, cursor="plus")
        description_and_poster_frame.pack(fill=X, padx=2, pady=2)

        metro_labelframe = Metro_LabelFrame(description_and_poster_frame, title="Tiny.Creatures (2020)")
        metro_labelframe.pack(fill=BOTH, side=LEFT, padx=2, pady=2, expand=True)
        quote = QuoteFrame(metro_labelframe.body, text="Director: Jhon Doe")
        quote.pack(anchor=NW)
        f = Frame(metro_labelframe.body, height=1, bg='grey')
        f.pack(fill=X)
        quote = QuoteFrame(metro_labelframe.body, text="Actors: Jhon Doe, Jhonas Doe")
        quote.pack(anchor=NW)

        f = Frame(metro_labelframe.body, height=1, bg='grey')
        f.pack(fill=X)

        f = Frame(metro_labelframe.body)
        f.pack(fill=X, pady=4)
        f = Frame(metro_labelframe.body, height=1, bg='grey')
        f.pack(fill=X)

        Frame(metro_labelframe.body, background=DEFAULT_BACKGROUND_COLOR, width=6).pack(side=LEFT, fill=Y)
        self.add_text_block(metro_labelframe, LORE_IPSUM0)
        self.add_text_block(metro_labelframe, LORE_IPSUM0)
        self.add_text_block(metro_labelframe, LORE_IPSUM1)
        self.add_text_block(metro_labelframe, LORE_IPSUM1)
        self.add_text_block(metro_labelframe, LORE_IPSUM2)
        self.add_text_block(metro_labelframe, LORE_IPSUM2)

        data_frame = Frame(description_and_poster_frame, width=200, height=300, bg=DEFAULT_DARK_BACKGROUND_COLOR,
                           relief=SOLID, cursor="plus", padx=2, pady=2)
        data_frame.pack(side=LEFT)

        poster = SimplePosterBox(data_frame)
        poster.pack(fill=BOTH, side=LEFT)

        f = Frame(frame, height=1, bg='grey')
        f.pack(fill=X)

        self.result_frame = Frame(frame, bg=DEFAULT_BACKGROUND_COLOR, relief=SUNKEN, cursor="plus")
        self.result_frame.pack(fill=X, padx=2, pady=2)

        self.magnet_list_box = \
            Multicolumn_Listbox(self.result_frame, ["Name", "Seeders", "Leechers", "Size"],
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

        data_frame = Frame(self.result_frame, width=460, height=300, bg=DEFAULT_BACKGROUND_COLOR,
                           relief=SUNKEN, cursor="plus")
        data_frame.pack(fill=BOTH, padx=2, pady=2)

        simple_data_box = SimpleDataBox(data_frame)
        simple_data_box.pack(fill=BOTH, side=RIGHT, pady=1)

        button_frame = Frame(frame, bg=DEFAULT_BACKGROUND_COLOR)
        button_frame.pack(fill=X, side=BOTTOM)

        w = Metro_Button(button_frame, text=' [  Download  ] ', background=DEFAULT_BACKGROUND_COLOR,
                         foreground=DEFAULT_TEXT_COLOR)
        w.pack(side=RIGHT)

        w = Metro_Button(button_frame, text='...', background=DEFAULT_BACKGROUND_COLOR,
                         foreground=DEFAULT_TEXT_COLOR)
        w.pack(side=RIGHT)

        f = Frame(frame, height=1, bg='grey')
        f.pack(fill=X)
        notebook.add(frame, text=color)