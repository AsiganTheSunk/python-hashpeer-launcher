from interface.component_filters.tk_common_widgets import TkCommonWidgets
from interface.search.page.constants.description_information_constants import DESCRIPTION_TEXT
from interface.components.metro_ui.metro_quote_container import MetroQuoteContainer
from interface.components.metro_ui.metro_label_containter import MetroLabelContainer
from interface.component_filters.constants import DEFAULT_BACKGROUND_COLOR

import textwrap

from tkinter import (
    Frame, Label, NW, BOTH, LEFT, SUNKEN
)


class MultimediaInformationContainer(Frame):
    def __init__(self, root_container, title='Dummy Title (0000)', directors='Dummy Director', actors='Dummy Actor', summary=DESCRIPTION_TEXT):
        Frame.__init__(self, root_container, height=300, bg=DEFAULT_BACKGROUND_COLOR, relief=SUNKEN, cursor="plus")
        self.pack(side=LEFT, fill=BOTH)

        # note: MetroDescriptionContainer
        self.description_container = self.set_title(title)

        # note: MetroDirectorQuoteFrame, MetroActorsQuoteFrame
        self.set_directors(directors)
        TkCommonWidgets.horizontal_separator(self.description_container.body)
        self.set_actors(actors)

        # note: SeparatorBlock within Multimedia: Film, Show, Anime Description
        TkCommonWidgets.horizontal_separator(self.description_container.body)
        TkCommonWidgets.horizontal_separator(self.description_container.body, background_color=None, height=0, pady=4)
        TkCommonWidgets.horizontal_separator(self.description_container.body)

        # note: VerticalSeparator: Description Container
        TkCommonWidgets.vertical_separator(self.description_container.body)
        self.set_summary(summary)

    def set_title(self, title=''):
        metro_labelframe_container = MetroLabelContainer(self, title=title.title())
        metro_labelframe_container.pack(fill=BOTH, side=LEFT, padx=2, pady=2, expand=True)
        return metro_labelframe_container

    def set_directors(self, directors=''):
        metro_quote_container = MetroQuoteContainer(self.description_container.body, text=f'Director: {directors}')
        metro_quote_container.pack(anchor=NW)

    def set_actors(self, actors=''):
        metro_actors_quote_frame = MetroQuoteContainer(self.description_container.body, text=f'Actors: {actors}')
        metro_actors_quote_frame.pack(anchor=NW)

    def set_summary(self, summary):
        for summary_lines in textwrap.fill(summary, 190).splitlines():
            metro_text_label = Label(self.description_container.body, text=summary_lines)
            metro_text_label.pack(anchor=NW)

