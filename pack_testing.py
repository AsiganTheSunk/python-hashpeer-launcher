"""
Author : ITVoyagers (itvoyagers.in)

Date : 2nd April 2020

Description : Program to show use of Frame widget

"""
from components.closable_notebook.recipe_closable_notebook import ClosableNotebook
from components.treeview_widget.recipe_treeview import Multicolumn_Listbox
from components.metro_ui.recipe_entry_metro_ui import Metro_LabelFrame, QuoteFrame
from tkinter import *
from PIL import ImageTk, Image

LORE_IPSUM0 = 'Lorem ipsum dolor sit amet consectetur adipiscing elit cursus arcu, lobortis elementum fusce tellus' \
             ' interdum morbi porta imperdiet facilisi, mauris sapien curabitur nullam.                  '
LORE_IPSUM1 = 'Ridiculus ultrices vehicula hac aenean parturient libero arcu erat turpis, est montes nostra ' \
              'aptent vel cum metus.'

LORE_IPSUM2 ='Vestibulum leo netus vulputate magnis interdum vel tincidunt lacinia, quam arcu praesent sed libero' \
             ' bibendum habitasse.'


spath = "Kong Skull Island_Film_Poster.png"

HASH_TEXT = 'Hash'
SIZE_TEXT = 'Size'
SEED_TEXT = 'Seeds'
LEECH_TEXT = 'Leechs'
LANGUAGE_TEXT = 'Language'
ANNOUNCE_LIST_TEXT = 'AnnounceList'

from display_box import DisplayBox
from component_filters.constants import DEFAULT_TEXT_COLOR, DEFAULT_BACKGROUND_COLOR, DEFAULT_DARK_BACKGROUND_COLOR, \
    DEFAULT_MEDIUM_DARK_BACKGROUND_COLOR, DEFAULT_FONT_STYLE, DEFAULT_FONT_SIZE, DEFAULT_DIMMED_TEXT_COLOR, \
    DEFAULT_SELECTED_UNDER_SCORE_TAB, DEFAULT_SELECTED_AND_NOT_ACTIVE_UNDER_SCORE_TAB


class SimplePosterBox(Frame):
    def __init__(self, master, width=200, height=300, background='grey'):
        Frame.__init__(self, master, width=width, height=height, background=background)
        self.poster_container = None
        self.image_path = ''

        self.on_create()

    def on_create(self):
        aux = Image.open('./old_implementation/interface/resources/placeholders/poster_placeholder.png')
        poster_image = ImageTk.PhotoImage(aux)
        self.poster_image = poster_image

        poster_container = Label(self, width=198, height=271, relief='solid')
        poster_container.configure(borderwidth=0, highlightbackground='#848482', image=poster_image)
        poster_container.grid(row=0, column=1, padx=2, pady=2)
        self.poster_container = poster_container


class SimpleDataBox(Frame):
    def __init__(self, master, background=DEFAULT_BACKGROUND_COLOR):
        Frame.__init__(self, master, width=456, height=300, background=background)
        self.data = None
        self.on_create()

    def on_create(self):
        data_box = Frame(self, width=456, height=250, background='#848482', highlightthickness=2,
                         highlightbackground=DEFAULT_MEDIUM_DARK_BACKGROUND_COLOR, highlightcolor=DEFAULT_MEDIUM_DARK_BACKGROUND_COLOR)
        data_box.pack(fill=X)

        # f = Frame(self, height=1, bg=DEFAULT_MEDIUM_DARK_BACKGROUND_COLOR)
        # f.pack(fill=X, pady=2)

        data_box2 = DisplayBox(self, width=456, height=50, background=DEFAULT_BACKGROUND_COLOR)
        data_box2.pack(fill=X, pady=3)

        T2 = Text(data_box, bg=DEFAULT_BACKGROUND_COLOR, width=68, height=16, foreground=DEFAULT_TEXT_COLOR)
        self.data = T2
        T2.pack(pady=2, padx=2)
        T2.configure(font=('calibri', (10)), relief='flat')
        quote = f'[ {HASH_TEXT} ]: ---' \
                f'\n------------------------------------------------------------------------------------' \
                f'\n[ {ANNOUNCE_LIST_TEXT} ]:' \
                f'\n\t[ HTTPS ]: --' \
                f'\n------------------------------------------------------------------------------------' \
                f'\n\t[ HTTP ]: --' \
                f'\n------------------------------------------------------------------------------------' \
                f'\n\t[ UDP ]: --'  \
                f'\n------------------------------------------------------------------------------------' \

        T2.insert(END, quote)
        T2.config(state=DISABLED)

    def set_data(self, info_data):
        self.data.configure(state=NORMAL)
        self.data.delete('1.0', END)
        self.data.insert(END, info_data)
        self.data.configure(state=DISABLED)


if __name__ == '__main__':
    root = Tk()
    # show no frame
    # root.overrideredirect(True)
    _width = root.winfo_screenwidth()
    _height = root.winfo_screenheight()

    width = _width / 2.0
    height = _height / 1.5
    print(_width, _height)
    print(width * 0.8, height * 0.8, _width * 0.415, _height * 0.15)

    root.geometry('%dx%d+%d+%d' % (width, height, _width * 0.42, _height * 0.15))
    root.configure(bg='lightblue')
    main_frame = Frame(root, height=height - 33, width=width, bg='lightblue', highlightthickness=0,
                       highlightbackground="pink",
                       relief=SUNKEN, cursor="plus")
    main_frame.pack(fill=BOTH, padx=1, pady=1)
    f = Frame(main_frame, height=10, width=500, bg='grey', highlightthickness=2, highlightbackground="pink",
              relief=SUNKEN,
              cursor="plus")
    f.pack(fill=X)

    search_frame = Frame(main_frame, height=120, width=500, bg='lightgrey', relief=SUNKEN, cursor="plus")
    search_frame.pack(fill=X)
    f = Frame(main_frame, height=10, width=500, bg='grey', highlightthickness=2, highlightbackground="pink",
              relief=SUNKEN,
              cursor="plus")
    f.pack(fill=X, padx=1)

    progressbar_frame = Frame(main_frame, height=20, width=500, bg='lightgrey', relief=SUNKEN, cursor="plus")
    progressbar_frame.pack(fill=X)

    f = Frame(main_frame, height=10, width=500, bg='grey', highlightthickness=2, highlightbackground="pink",
              relief=SUNKEN,
              cursor="plus")
    f.pack(fill=X)

    collapsable_menu = Frame(main_frame, height=40, width=500, bg='lightgrey', relief=SUNKEN, cursor="plus")
    collapsable_menu.pack(fill=X)

    w = Label(collapsable_menu, width=25, text="itv6", bg="green", fg="black")
    w.pack(padx=10, pady=5, side=LEFT)

    notebook = ClosableNotebook()
    notebook.pack(side="top", fill="both", expand=True, padx=2)

    for color in ("pink", "orange", "lightgreen", "lightblue", "violet"):
        frame = Frame(notebook, background=color)
        frame.pack(fill=BOTH)

        description_and_poster_frame = Frame(frame, height=300, bg='lightgrey', relief=SUNKEN, cursor="plus")
        description_and_poster_frame.pack(fill=X, padx=2, pady=2)

        metro_labelframe = Metro_LabelFrame(description_and_poster_frame, title="Tiny.Creatures")
        metro_labelframe.pack(fill=BOTH, side=LEFT, padx=6, pady=2, expand=True)
        quote = QuoteFrame(metro_labelframe.body, text="Year: 2020")
        quote.pack()
        quote = QuoteFrame(metro_labelframe.body, text="Director: Jhon Doe")
        quote.pack()
        quote = QuoteFrame(metro_labelframe.body, text="Actors: Jhon Doe, Jhonas Doe")
        quote.pack()
        Label(metro_labelframe.body, text=LORE_IPSUM0).pack(anchor=W)
        Label(metro_labelframe.body, text=LORE_IPSUM1).pack(anchor=W)
        Label(metro_labelframe.body, text=LORE_IPSUM2).pack(anchor=W)

        data_frame = Frame(description_and_poster_frame, width=200,
                           height=300, bg='yellow', relief=SUNKEN, cursor="plus")
        data_frame.pack(padx=2, pady=2, side=LEFT)

        poster = SimplePosterBox(data_frame, 0, 0)

        f = Frame(frame, height=10, bg='grey', highlightthickness=2,
                  highlightbackground="pink", relief=SUNKEN, cursor="plus")
        f.pack(fill=X)

        result_frame = Frame(frame, bg='violet', relief=SUNKEN, cursor="plus")
        result_frame.pack(fill=X, padx=2, pady=2)

        def on_select(data):
            print("called command when row is selected")
            print(data)
            print("\n")

        mcListbox = Multicolumn_Listbox(result_frame, ["Name", "Seeders", "Leechers", "Size"], command=on_select, cell_anchor="center")
        mcListbox.interior.pack(fill=BOTH, side=LEFT, pady=2, padx=2, expand=True)

        mcListbox.insert_row(["Tiny.Creatures.S01.1080p.NF.WEBRip.DDP5.1.x264-ExREN[rartv]", 2, 3, 4])
        mcListbox.insert_row(["Tiny.Creatures.Season.01.1080p", 5, 6, 7])
        mcListbox.insert_row(["Tiny.Creatures.S01.1080p.NF.WEBRip.DDP5.1.x265", 8, 9, 10])
        mcListbox.insert_row(["Tiny.Creatures.S01.1080p.NF.WEBRip.DDP5.1.x265", 8, 9, 10])
        mcListbox.insert_row(["Tiny.Creatures.S01.1080p.NF.WEBRip.DDP5.1.x265", 8, 9, 10])
        mcListbox.insert_row(["Tiny.Creatures.S01.1080p.NF.WEBRip.DDP5.1.x265", 8, 9, 10])
        mcListbox.insert_row(["Tiny.Creatures.S01.1080p.NF.WEBRip.DDP5.1.x265", 8, 9, 10])
        mcListbox.insert_row(["Tiny.Creatures.S01.1080p.NF.WEBRip.DDP5.1.x265", 8, 9, 10])
        mcListbox.insert_row(["Tiny.Creatures.S01.1080p.NF.WEBRip.DDP5.1.x265", 8, 9, 10])
        mcListbox.insert_row(["Tiny.Creatures.S01.1080p.NF.WEBRip.DDP5.1.x265", 8, 9, 10])
        mcListbox.insert_row(["Tiny.Creatures.S01.1080p.NF.WEBRip.DDP5.1.x265", 8, 9, 10])

        data_frame = Frame(result_frame, width=460, height=300, bg='lightgreen', relief=SUNKEN, cursor="plus")
        data_frame.pack(fill=BOTH, padx=2, pady=2)

        simple_data_box = SimpleDataBox(data_frame)

        f = Frame(frame, height=10, bg='grey', highlightthickness=2, highlightbackground="pink",
                  relief=SUNKEN, cursor="plus")
        f.pack(fill=X)

        button_frame = Frame(frame, height=50, bg='lightgrey', relief=SUNKEN, cursor="plus")
        button_frame.pack(fill=X, padx=2, pady=2)

        w = Label(button_frame, width=25, text="itv6", bg="green", fg="black")
        w.pack(padx=10, pady=5, side=RIGHT)
        notebook.add(frame, text=color)

    root.mainloop()
