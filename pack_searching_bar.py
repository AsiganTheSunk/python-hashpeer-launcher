"""
Author : ITVoyagers (itvoyagers.in)

Date : 2nd April 2020

Description : Program to show use of Frame widget

"""
from tkinter import *
from components.closable_notebook.recipe_closable_notebook import ClosableNotebook
from components.treeview_widget.recipe_treeview import Multicolumn_Listbox
from components.metro_ui.recipe_entry_metro_ui import Metro_LabelFrame, QuoteFrame
from components.metro_ui.recipe_entry_metro_ui import Search_Box

LORE_IPSUM0 = 'Lorem ipsum dolor sit amet consectetur adipiscing elit cursus arcu, lobortis elementum fusce tellus' \
             ' interdum morbi porta imperdiet facilisi, mauris sapien curabitur nullam.                  '
LORE_IPSUM1 = 'Ridiculus ultrices vehicula hac aenean parturient libero arcu erat turpis, est montes nostra ' \
              'aptent vel cum metus.'

LORE_IPSUM2 ='Vestibulum leo netus vulputate magnis interdum vel tincidunt lacinia, quam arcu praesent sed libero' \
             ' bibendum habitasse.'


spath = "Kong Skull Island_Film_Poster.png"


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


    def command(text):
        print("search command", "searching:%s" % text)

    searchbox = Search_Box(search_frame, command=command, placeholder="Type and press enter", entry_highlightthickness=0)
    searchbox.pack(side=RIGHT)

    root.mainloop()