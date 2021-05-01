from re import (
    compile, escape, IGNORECASE, match
)
from tkinter import (
    Frame, NORMAL, Entry, BOTH, StringVar, Listbox, FLAT, END, ACTIVE
)


class MetroEntryContainer(Frame):
    BORDER_COLOR = "#999999"
    ACTIVE_BORDERCOLOR = "#787878"

    BACKGROUND = "white"

    DISABLED_BACKGROUND = "#EBEBE4"
    DISABLED_FOREGROUND = "#545454"

    BORDER_WIDTH = 1

    def __init__(self, master, width=None, placeholder_font=None, placeholder_color="grey",
                 highlightthickness=1, state=NORMAL, font=None, autocomplete_list=None, default_message=None,
                 *args, **kwargs):

        self._frame = Frame.__init__(self, master, bd=0, background=MetroEntryContainer.BACKGROUND,
                                     highlightbackground=MetroEntryContainer.BORDER_COLOR,
                                     highlightcolor=MetroEntryContainer.BORDER_COLOR,
                                     highlightthickness=MetroEntryContainer.BORDER_WIDTH)

        # Listbox length
        if 'listboxLength' in kwargs:
            self.listboxLength = kwargs['listboxLength']
            del kwargs['listboxLength']
        else:
            self.listboxLength = 8

        # Custom matches function
        if 'matchesFunction' in kwargs:
            self.matchesFunction = kwargs['matchesFunction']
            del kwargs['matchesFunction']
        else:
            def matches(fieldValue, acListEntry):
                pattern = compile('.*' + escape(fieldValue) + '.*', IGNORECASE)
                return match(pattern, acListEntry)

            self.matchesFunction = matches

        DEFAULT_FONT_SIZE = 10
        DEFAULT_FONT_STYLE = 'calibri'
        self._entry = Entry(self, background=MetroEntryContainer.BACKGROUND,
                            disabledbackground=MetroEntryContainer.DISABLED_BACKGROUND,
                            disabledforeground=MetroEntryContainer.DISABLED_FOREGROUND, bd=0,
                            default_message=default_message, font=(DEFAULT_FONT_STYLE, DEFAULT_FONT_SIZE))
        self._entry.pack(expand=True, fill=BOTH, padx=3)

        # if placeholder:
        #     add_placeholder_to(self._entry, placeholder, color=placeholder_color, font=placeholder_font)

        # if font:
        #     self._entry.configure(font=font)

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
        self.listbox = None
        self.autocomplete_list = autocomplete_list

        self.var = self._entry["textvariable"]
        if self.var == '':
            self.var = self._entry["textvariable"] = StringVar()

        self.var.trace('w', self.changed)
        self._entry.bind("<Right>", self.selection)
        self._entry.bind("<Up>", self.moveUp)
        self._entry.bind("<Down>", self.moveDown)

        self.listbox_up = False

    def _on_focusin(self, event):
        if self._highlightthickness == 0:
            self.configure(highlightbackground=MetroEntryContainer.BORDER_COLOR,
                           highlightcolor=MetroEntryContainer.BORDER_COLOR,
                           highlightthickness=MetroEntryContainer.BORDER_WIDTH)
        else:
            self.configure(highlightbackground=MetroEntryContainer.ACTIVE_BORDERCOLOR,
                           highlightcolor=MetroEntryContainer.ACTIVE_BORDERCOLOR,
                           highlightthickness=self._highlightthickness)

    def _on_focusout(self, event):
        self.configure(highlightbackground=MetroEntryContainer.BORDER_COLOR,
                       highlightcolor=MetroEntryContainer.BORDER_COLOR,
                       highlightthickness=MetroEntryContainer.BORDER_WIDTH)

    def get_state(self):
        return self._entry.cget("state")

    def set_state(self, state):
        if state == NORMAL:
            self.configure(background="white")
        else:
            self.configure(background=MetroEntryContainer.DISABLED_BACKGROUND)

        self._entry.configure(state=state)

    def get_font(self):
        return self._entry.cget("font")

    def set_font(self, font):
        self._entry.configure(font=font)

    def bind_entry(self, event, handler):
        self._entry.bind(event, handler)

    def changed(self, name, index, mode):
        if self.var.get() == '':
            if self.listbox_up:
                self.listbox.destroy()
                self.listbox_up = False
        else:
            words = self.comparison()
            if words:
                # Todo: listbox search
                if not self.listbox_up:
                    self.listbox = Listbox(self._frame, width=71, height=self.listboxLength, relief=FLAT,
                                           highlightbackground=MetroEntryContainer.BORDER_COLOR,
                                           highlightcolor=MetroEntryContainer.BORDER_COLOR,
                                           highlightthickness=MetroEntryContainer.BORDER_WIDTH)

                    self.listbox.bind("<Button-1>", self.selection)
                    self.listbox.bind("<Right>", self.selection)
                    _width = self._entry.winfo_x()
                    _hight = self._entry.winfo_y()
                    print('search box:', _width, _hight)
                    self.listbox.place(in_=self._frame, relx=0.599, rely=0.085)
                    self.listbox_up = True

                self.listbox.delete(0, END)
                for w in words:
                    self.listbox.insert(END, w)
            else:
                if self.listbox_up:
                    self.listbox.destroy()
                    self.listbox_up = False

    def selection(self, event):
        if self.listbox_up:
            self.var.set(self.listbox.get(ACTIVE))
            self.listbox.destroy()
            self.listbox_up = False
            self.icursor(END)

    def moveUp(self, event):
        if self.listbox_up:
            if self.listbox.curselection() == ():
                index = '0'
            else:
                index = self.listbox.curselection()[0]

            if index != '0':
                self.listbox.selection_clear(first=index)
                index = str(int(index) - 1)

                self.listbox.see(index)  # Scroll!
                self.listbox.selection_set(first=index)
                self.listbox.activate(index)

    def moveDown(self, event):
        if self.listbox_up:
            if self.listbox.curselection() == ():
                index = '0'
            else:
                index = self.listbox.curselection()[0]

            if index != END:
                self.listbox.selection_clear(first=index)
                index = str(int(index) + 1)

                self.listbox.see(index)  # Scroll!
                self.listbox.selection_set(first=index)
                self.listbox.activate(index)

    def comparison(self):
        return [w for w in self.autocomplete_list if self.matchesFunction(self.var.get(), w)]