from tkinter import *


class Placeholder_State(object):
    __slots__ = 'normal_color', 'normal_font', 'placeholder_text', 'placeholder_color', 'placeholder_font', 'contains_placeholder'


def add_placeholder_to(entry, placeholder, color="grey", font=None):
    normal_color = entry.cget("fg")
    normal_font = entry.cget("font")

    if font is None:
        font = normal_font

    state = Placeholder_State()
    state.normal_color = normal_color
    state.normal_font = normal_font
    state.placeholder_color = color
    state.placeholder_font = font
    state.placeholder_text = placeholder
    state.contains_placeholder = True

    def on_focusin(event, entry=entry, state=state):
        if state.contains_placeholder:
            entry.delete(0, "end")
            entry.config(fg=state.normal_color, font=state.normal_font)

            state.contains_placeholder = False

    def on_focusout(event, entry=entry, state=state):
        if entry.get() == '':
            entry.insert(0, state.placeholder_text)
            entry.config(fg=state.placeholder_color, font=state.placeholder_font)

            state.contains_placeholder = True

    entry.insert(0, placeholder)
    entry.config(fg=color, font=font)

    entry.bind('<FocusIn>', on_focusin, add="+")
    entry.bind('<FocusOut>', on_focusout, add="+")

    entry.placeholder_state = state

    return state


class Metro_Entry(Frame):
    BORDER_COLOR = "#999999"
    ACTIVE_BORDERCOLOR = "#787878"

    BACKGROUND = "white"

    DISABLED_BACKGROUND = "#EBEBE4"
    DISABLED_FOREGROUND = "#545454"

    BORDER_WIDTH = 1

    def __init__(self, master, width=None, placeholder=None, placeholder_font=None, placeholder_color="grey",
                 highlightthickness=1, state=NORMAL, font=None, ID=None, default_message='Text'):

        Frame.__init__(self, master, ID=ID, bd=0, background=Metro_Entry.BACKGROUND,
                       highlightbackground=Metro_Entry.BORDER_COLOR, highlightcolor=Metro_Entry.BORDER_COLOR,
                       highlightthickness=Metro_Entry.BORDER_WIDTH)

        self._entry = Entry(self, background=Metro_Entry.BACKGROUND, disabledbackground=Metro_Entry.DISABLED_BACKGROUND,
                            disabledforeground=Metro_Entry.DISABLED_FOREGROUND, highlightthickness=0, bd=0,
                            )
        self._entry.pack(expand=True, fill=BOTH, padx=5, pady=5)

        if placeholder:
            add_placeholder_to(self._entry, placeholder, color=placeholder_color, font=placeholder_font)

        if font:
            self._entry.configure(font=font)

        if width:
            self._entry.configure(width=width)

        self._highlightthickness = highlightthickness

        self._entry.bind("<Escape>", lambda event: self._entry.nametowidget(".").focus())

        self._entry.bind('<FocusIn>', self._on_focusin, add="+")
        self._entry.bind('<FocusOut>', self._on_focusout, add="+")

        self.delete = self._entry.delete
        self.get = self._entry.get
        self.icursor = self._entry.icursor
        self.insert = self._entry.insert
        self.insert = self._entry.insert
        self.scan_dragto = self._entry.scan_dragto
        self.scan_dragto = self._entry.scan_dragto
        self.scan_mark = self._entry.scan_mark
        self.select_adjust = self._entry.select_adjust
        self.select_clear = self._entry.select_clear
        self.select_from = self._entry.select_from
        self.select_present = self._entry.select_present
        self.select_range = self._entry.select_range
        self.select_to = self._entry.select_to
        self.selection_adjust = self._entry.selection_adjust
        self.selection_clear = self._entry.selection_clear
        self.selection_from = self._entry.selection_from
        self.selection_present = self._entry.selection_present
        self.selection_range = self._entry.selection_range
        self.selection_range = self._entry.selection_range
        self.selection_to = self._entry.selection_to
        self.xview = self._entry.xview
        self.xview_moveto = self._entry.xview_moveto
        self.xview_scroll = self._entry.xview_scroll

    def _on_focusin(self, event):
        if self._highlightthickness == 0:
            self.configure(highlightbackground=Metro_Entry.BORDER_COLOR, highlightcolor=Metro_Entry.BORDER_COLOR,
                           highlightthickness=Metro_Entry.BORDER_WIDTH)
        else:
            self.configure(highlightbackground=Metro_Entry.ACTIVE_BORDERCOLOR,
                           highlightcolor=Metro_Entry.ACTIVE_BORDERCOLOR, highlightthickness=self._highlightthickness)

    def _on_focusout(self, event):
        self.configure(highlightbackground=Metro_Entry.BORDER_COLOR, highlightcolor=Metro_Entry.BORDER_COLOR,
                       highlightthickness=Metro_Entry.BORDER_WIDTH)

    def get_state(self):
        return self._entry.cget("state")

    def set_state(self, state):
        if state == NORMAL:
            self.configure(background="white")
        else:
            self.configure(background=Metro_Entry.DISABLED_BACKGROUND)

        self._entry.configure(state=state)

    def get_font(self):
        return self._entry.cget("font")

    def set_font(self, font):
        self._entry.configure(font=font)

    def bind_entry(self, event, handler):
        self._entry.bind(event, handler)