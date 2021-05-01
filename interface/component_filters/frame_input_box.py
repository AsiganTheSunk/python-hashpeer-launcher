from tkinter import *
from interface.component_filters.constants import DEFAULT_BACKGROUND_COLOR, DEFAULT_MOUSE_OVER_TAB, DEFAULT_FONT_STYLE, \
    DEFAULT_FONT_SIZE, DEFAULT_SELECTED_UNDER_SCORE_TAB, DEFAULT_TEXT_COLOR, DEFAULT_DIMMED_TEXT_COLOR

from interface.component_filters.frame_tag_label import FrameTagLabel
from interface.component_filters.tk_utils import TkUtils


class FrameInputBox(Frame):
    BORDER_COLOR = "#999999"
    ACTIVE_BORDERCOLOR = "#787878"

    BACKGROUND = "white"

    DISABLED_BACKGROUND = "#EBEBE4"
    DISABLED_FOREGROUND = "#545454"

    BORDER_WIDTH = 1

    def __init__(self, root, default_text='', width=10, output_frame=None, entry_type=''):
        self.root = root
        Frame.__init__(self, root, bd=0, background=FrameInputBox.BACKGROUND,
                       highlightbackground=DEFAULT_TEXT_COLOR, highlightcolor=DEFAULT_DIMMED_TEXT_COLOR,
                       highlightthickness=1)
        self.input_box = Entry(self, width=width, relief=FLAT, foreground=DEFAULT_BACKGROUND_COLOR,
                               font=(DEFAULT_FONT_STYLE, DEFAULT_FONT_SIZE), justify=CENTER,
                               insertbackground=DEFAULT_BACKGROUND_COLOR, insertwidth=2,
                               selectborderwidth=0, selectforeground=DEFAULT_MOUSE_OVER_TAB,
                               selectbackground=DEFAULT_BACKGROUND_COLOR)
        self.input_box.pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=6)

        self.default_text = default_text
        self.entry_type = entry_type
        self.input_box.insert(END, default_text)
        self.output_frame = output_frame
        self.bind('<FocusIn>', self.on_focus_in)
        self.bind('<FocusOut>', self.on_focus_out)
        self.input_box.bind('<Escape>', self.on_focus_out)
        self.tag = None

        self.var = StringVar(root)
        self.var.set(default_text)
        self.var.trace('w', self.update)
        self.previous_input = None

    def close(self):
        self.clear_filter_tag()
        self.destroy()

    def clear_filter_tag(self):
        if self.output_frame is not None and self.tag is not None:
            self.tag.close()
            self.tag = None

    def clear_and_reset(self, event):
        self.reset_text()
        self.tag.close()
        self.validate()

    def show_filter_tag(self, text, tooltip_text):
        if self.output_frame is not None and self.tag is None:
            self.tag = FrameTagLabel(self.output_frame, self.var.get(), tooltip_text)
            self.tag.pack(side=LEFT, padx=4)
        self.tag.filter_tag_label.bind('<Button-3>', lambda event: self.clear_and_reset(event))

    def update(self, *args):
        if self.previous_input is None:
            self.previous_input = self.var.get()

        if self.previous_input != self.input_box.get():
            print('update', self.previous_input, self.input_box.get())
            self.clear_filter_tag()
            self.validate()

    def validate(self):
        text = self.get()
        is_valid_input = TkUtils.is_digit_season(text)

        if is_valid_input:
            self.configure(bg=DEFAULT_SELECTED_UNDER_SCORE_TAB)
            self.input_box.configure(bg=DEFAULT_SELECTED_UNDER_SCORE_TAB,
                                     font=(DEFAULT_FONT_STYLE, DEFAULT_FONT_SIZE, 'bold'))
            self.show_filter_tag(text, 'Tooltip Text:\n This obj does something.')

        elif not is_valid_input:
            if text == self.default_text or text == '':
                self.configure(bg='white')
                self.input_box.configure(bg='white', fg=DEFAULT_BACKGROUND_COLOR,
                                         font=(DEFAULT_FONT_STYLE, DEFAULT_FONT_SIZE))
            else:
                self.configure(bg='light coral')
                self.input_box.configure(bg='light coral', font=(DEFAULT_FONT_STYLE, DEFAULT_FONT_SIZE, 'bold'))
            self.clear_filter_tag()

    def on_focus_out(self, *args):
        if self.input_box.get() == '':
            self.reset_text()

        self.var.set(self.input_box.get())
        self.validate()

    def on_focus_in(self, *args):
        if self.input_box.get() == self.default_text:
            self.input_box.delete(0, "end")  # delete all the text in the entry
            self.input_box.configure(foreground='black')
            self.input_box.insert(0, '')  # Insert blank for user input
            self.input_box.focus_set()

    def reset_text(self):
        self.input_box.delete(0, 'end')
        self.input_box.insert(END, self.default_text)

    def disable(self):
        self.input_box['state'] = 'disable'

    def enable(self):
        self.input_box['state'] = 'normal'

    def get(self):
        input_text = self.input_box.get()
        if input_text != self.default_text and input_text != '':
            return input_text
        return ''
