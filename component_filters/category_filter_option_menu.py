from component_filters.frame_multi_option_menu import create_menu_selector
from component_filters.frame_menu_options import FrameOptionMenu
from component_filters.frame_input_box import FrameInputBox
from typing import Any, Callable, List, Tuple
from tkinter import *
from component_filters.constants import DEFAULT_FILTER_LABELS, CATEGORY_LABEL, DEFAULT_FONT_SIZE, DEFAULT_FONT_STYLE, \
    DEFAULT_BACKGROUND_COLOR, DEFAULT_MEDIUM_DARK_BACKGROUND_COLOR, DEFAULT_TEXT_COLOR
from components.metro_ui.recipe_entry_metro_ui import Metro_Button

from component_filters.tk_utils import TkUtils
from component_filters.entry_filter_list import EntryFilterList
from components.metro_ui.recipe_entry_metro_ui import Search_Box

CATEGORY_FILTER_TAGS = '  [  SEARCH FILTER TAGS  ]  '


class CategoryFilterOptionMenu(Frame):
    def __init__(self, root):
        self.root = root
        Frame.__init__(self, root, relief=FLAT, background=DEFAULT_BACKGROUND_COLOR)
        self.pack(fill=X)
        self.entry_items = None
        f = Frame(self.root, height=1, bg='grey', relief=FLAT)
        f.pack(fill=X)
        # note: < Container Frames >
        #  UpperBoxRoot: This box will contain category_root, search_input_root
        #  LowerBoxRoot: This box will contain the filter_output
        self.upper_box_root = Frame(self, root, relief=FLAT)
        self.upper_box_root.pack(anchor=N, expand=True, fill=X)
        self.lower_box_root = Frame(self, root, relief=FLAT)
        self.lower_box_root.pack(anchor=S, expand=True, fill=X)

        # note: CategoryRoot:
        self.category_root = Frame(self.upper_box_root, bg=DEFAULT_BACKGROUND_COLOR)
        self.category_root.pack(side=LEFT, anchor=NW)

        # note: SearchInputRoot:
        self.search_input_root = Frame(self.upper_box_root, bg=DEFAULT_BACKGROUND_COLOR)
        self.search_input_root.pack(side=RIGHT, anchor=NE)

        # note: FilterRoot:
        self.filler = Frame(self.lower_box_root, height=1, bg='grey', relief=FLAT)
        self.filler.pack(fill=X)
        self.filter_root = Frame(self.lower_box_root, height=30, bg=DEFAULT_MEDIUM_DARK_BACKGROUND_COLOR)
        self.filter_root.pack(side=BOTTOM, fill=X)

        # note: FillerFrame:
        self.filler_frame = Frame(self.filter_root, height=30, bg=DEFAULT_BACKGROUND_COLOR, borderwidth=2, relief=SOLID)
        self.filler_frame.pack(padx=8, pady=5, side=LEFT)

        label = Label(self.filler_frame, text=CATEGORY_FILTER_TAGS, justify='center', bg=DEFAULT_BACKGROUND_COLOR,
                      font=(DEFAULT_FONT_STYLE, DEFAULT_FONT_SIZE), fg=DEFAULT_TEXT_COLOR)
        label.pack(pady=4)

        # note: CategoryMenuOption, AddFilterButton:
        self.category_menu_option = \
            FrameOptionMenu(self.category_root, CATEGORY_LABEL, *DEFAULT_FILTER_LABELS['Category'])
        self.category_menu_option.pack(side=LEFT, padx=2, pady=2)

        self.add_filter_button = Metro_Button(self.category_root, text='  +  ', background=DEFAULT_BACKGROUND_COLOR)
        self.add_filter_button.config(font=(DEFAULT_FONT_STYLE, DEFAULT_FONT_SIZE))
        self.add_filter_button.pack(side=LEFT, padx=4, pady=10)
        self.add_filter_button['state'] = 'disabled'

        self.input_filter_root = Frame(self.category_root, height=30, bg=DEFAULT_BACKGROUND_COLOR)
        self.input_filter_root.pack(side=LEFT)

        self.search_box = Search_Box(self.search_input_root, command=self.compose_entry_data, placeholder="Search")
        self.search_box.pack(pady=10, padx=8, side=LEFT)

        create_menu_selector(self.add_filter_button, root=self.root, output_frame=self.filter_root,
                             root_selection=self.category_menu_option.get)

        # note: Trace: < Option Menu Var Modification >
        self.category_menu_option.var.trace('w', self.update_options)

    def reset_entry_items(self):
        self.entry_items = []

    def update_options(self, *args):
        if self.add_filter_button['state'] == 'active':
            return

        print('< Update Filter Button Add >')
        self.add_filter_button['state'] = 'active'
        if self.entry_items is None:
            self.entry_items = EntryFilterList(root=self.input_filter_root,
                                               root_selection_var=self.category_menu_option.var,
                                               root_output=self.filter_root)

    # note: The info from search comes from here, so create WebSearchInstance:
    #  a input type needs to be added to the input, so it can be constructed properly.
    def compose_entry_data(self, title):
        number_str_filter: Callable[[str], str] = \
            lambda str_number: f'{str_number.lstrip("0")}' if int(str_number) >= 10 else f'0{str_number.lstrip("0")}'
        season_filter: Callable[[str], str] = \
            lambda _season: f'S{number_str_filter(_season)}' if _season != '' else f''
        episode_filter: Callable[[str], str] = \
            lambda _episode: f'E{number_str_filter(_episode)}' if _episode != '' else f''
        # note: year_validator: Callable[[str], bool] = lambda _year: True if int(_year) >= 1950 else False

        compose_result: Callable[[str, str, str], str] = \
            lambda affix, _title, entry_type: f'{affix} {_title}' if entry_type != 'Year' else f'{_title} {affix}'

        result = ''
        if self.entry_items is not None:
            for element in self.entry_items.input_box_list:
                if element.entry_type == 'Season' and element.get() != '':
                    result += season_filter(element.get())
                elif element.entry_type == 'Episode' and element.get() != '':
                    result += episode_filter(element.get())
                elif element.entry_type == 'Year' and element.get() != '':
                    result += element.get()

            print(f'{compose_result(result, title, self.entry_items.input_box_list[0].entry_type)}')

