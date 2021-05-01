from interface.component_filters.constants import DEFAULT_BACKGROUND_COLOR
from tkinter import Frame, TOP, BOTH
from interface.components.closable_notebook.recipe_closable_notebook import ClosableNotebook
from interface.search.page.multimedia_page_container import MultimediaPageContainer

SHOW_BORDER_COLOR = "Tomato"
FILM_BORDER_COLOR = "LightBlue"
ANIME_BORDER_COLOR = "Orange"


class SearchResultContainer(Frame):
    def __init__(self, root_container):
        Frame.__init__(self, root_container)

        # note: ClosableNotebook:
        self.closable_notebook = ClosableNotebook()
        self.closable_notebook.pack(side=TOP, fill=BOTH, expand=True, padx=6, pady=6)

        self.note_book_pages = []
        self.notebook_page_container = MultimediaPageContainer(self.closable_notebook)
        self.add_page(SHOW_BORDER_COLOR)
        # self.add_page(FILM_BORDER_COLOR)
        # self.add_page(ANIME_BORDER_COLOR)

    def add_page(self, background_color):
        self.notebook_page_container.init_new_notebook_tab(background_color)

