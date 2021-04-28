from tkinter import *
from tkinter.ttk import *
from component_filters.frame_menu_options import FrameOptionMenu
from component_filters.constants import DEFAULT_FILTER_LABELS, DEFAULT_FONT_SIZE, DEFAULT_FONT_STYLE, \
    DEFAULT_TOOLTIP_PLACEHOLDER, DEFAULT_BACKGROUND_COLOR, CATEGORY_LABEL
from component_filters.frame_tooltip import CreateToolTip
from components.metro_ui.recipe_entry_metro_ui import Metro_Entry, Metro_Button

from component_filters.tk_utils import TkUtils
from component_filters.frame_tag_label import FrameTagLabel

DEFAULT_FRAME_PADY = 35

class FrameMultiOptionMenu(object):
    def __init__(self, widget, root, output_frame):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0
        self.frame_select = None
        self.root = root
        self.root.bind("<Configure>", self.sync_window)
        self.output_frame = output_frame
        self.opt_menu_filter_types = None
        self.opt_menu_filters = None
        self.filter_category = None
        self.add_filter_button = None
        self.cancel_filter_button = None
        self.filter_label = None

    def show(self, root_value_selection):
        "Display text in tooltip window"
        if self.tipwindow:
            return

        self.tipwindow = tw = Toplevel(self.widget)
        TkUtils.sync_window(self.widget, self.tipwindow, 0, DEFAULT_FRAME_PADY)

        # Error al asignarle color, no tiene sentido he tocado algun orden de definicion o algo asim
        # relacion con el seteo de este frame, porque si no pongo bg fuca
        self.frame_select = Frame(tw, width=200, height=150, relief=FLAT)


        self.frame_select.pack(ipadx=2, fill=BOTH)
        self.frame_select.bind("<Button-3>", lambda event: self.close(event))

        self.filter_category = root_value_selection
        self.opt_menu_filter_types = \
            FrameOptionMenu(self.frame_select, 'Filter-Opt-Type',
                             *DEFAULT_FILTER_LABELS['Category'][self.filter_category]['opt'])

        # trace: < Option Menu Var Modifiaction >
        self.opt_menu_filter_types.var.trace('w', self.update_options)
        self.opt_menu_filter_types.pack(expand=True, fill=X, padx=10, pady=10)
        self.opt_menu_filter_types.bind("<Button-3>", lambda event: self.close(event))

        # disabled: until opt_menu_filter_types selects something
        self.opt_menu_filters = FrameOptionMenu(self.frame_select, '', '')
        self.opt_menu_filters.pack(expand=True, fill=X, padx=10, pady=10)
        self.opt_menu_filters.option_menu['state'] = 'disabled'
        self.opt_menu_filters.bind("<Button-3>", lambda event: self.close(event))

        # disabled: until opt_menu_filter_types selects something
        self.add_filter_button = Metro_Button(self.frame_select, text='  Add Filter  ', background=DEFAULT_BACKGROUND_COLOR, command=self.add_filter_label)

        self.add_filter_button.pack(fill=X, padx=10, pady=5, side=LEFT)
        self.add_filter_button.bind("<Button-3>", lambda event: self.close(event))
        self.add_filter_button['state'] = 'disabled'

        self.cancel_filter_button = Metro_Button(self.frame_select, text='    Cancel    ',
                                                 background=DEFAULT_BACKGROUND_COLOR,
                                                 command=self.close)
        self.cancel_filter_button.pack(fill=X, padx=10, pady=5, side=LEFT)
        self.cancel_filter_button.bind("<Button-3>", lambda event: self.close(event))

    def add_filter_label(self):
        opt_filter_type = self.opt_menu_filter_types.get()

        if opt_filter_type in [*DEFAULT_FILTER_LABELS['Category'][self.filter_category]['opt']]:
            tooltip_text = DEFAULT_FILTER_LABELS['Category'][self.filter_category]['opt'][opt_filter_type]
            print(tooltip_text)
            opt_filter = self.opt_menu_filters.get()
            self.add_opt_filter(self.output_frame, opt_filter, 'tooltip_text')
            print(f'< Add Filter: {opt_filter_type}, {opt_filter} >')
            self.close()

    def sync_window(self, event=None):
        # tracks: < Configure Event >
        TkUtils.sync_window(self.widget, self.tipwindow, 0, DEFAULT_FRAME_PADY)

    def add_opt_filter(self, output_frame, filter_text, filter_tooltip_text):
        tag = FrameTagLabel(output_frame, filter_text, filter_tooltip_text)
        tag.pack(side=LEFT, padx=4)

    def clear_opt_filter(self):
        pass

    def close(self, event=None):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()
            self.root.focus_set()

    def update_options(self, *args):
        print('< Update Menu Selector >')
        self.opt_menu_filters.option_menu['state'] = 'active'
        opt_filter_type = self.opt_menu_filter_types.get()
        opt_filter_type_list = DEFAULT_FILTER_LABELS['Category'][self.filter_category]['opt'][opt_filter_type]
        self.opt_menu_filters.set(opt_filter_type_list[0])
        menu = self.opt_menu_filters.option_menu['menu']
        menu.delete(0, "end")

        for items in opt_filter_type_list:
            menu.add_command(label=items, command=lambda data=items: self.opt_menu_filters.set(data))

        self.add_filter_button['state'] = 'active'


def create_menu_selector(widget, root, output_frame, root_selection=None):
    filter_menu_frame = FrameMultiOptionMenu(widget, root, output_frame)

    def enter(event):
        selection = root_selection()
        print(event, selection)
        if selection is not None and selection != CATEGORY_LABEL:
            filter_menu_frame.show(selection)

    def leave(event):
        filter_menu_frame.close(event)

    widget.bind("<Button-1>", enter)
    widget.bind("<Button-3>", leave)

    root.bind("<Button-3>", leave)
    root.bind('<Escape>', leave)

