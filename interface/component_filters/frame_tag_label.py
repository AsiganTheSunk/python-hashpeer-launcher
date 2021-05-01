from tkinter import Label, LEFT, Frame, BOTH
from interface.component_filters.constants import DEFAULT_FONT_SIZE, DEFAULT_FONT_STYLE, DEFAULT_BACKGROUND_COLOR, \
    DEFAULT_TOOLTIP_PLACEHOLDER
from interface.component_filters.frame_tooltip import CreateToolTip


class FrameTagLabel(Frame):
    def __init__(self, root, text, tooltip_text=DEFAULT_TOOLTIP_PLACEHOLDER):
        self.root = root
        self.text = text
        self.tooltip_text = tooltip_text

        Frame.__init__(self, root, bd=0, bg=DEFAULT_BACKGROUND_COLOR,
                       highlightbackground='white', highlightcolor='white', highlightthickness=1)
        self.filter_tag_label = \
            Label(self, width=15, text=text, fg='white', bg=DEFAULT_BACKGROUND_COLOR, disabledforeground='white')
        self.filter_tag_label.config(font=(DEFAULT_FONT_STYLE, DEFAULT_FONT_SIZE, 'bold'))
        self.filter_tag_label.pack(side=LEFT, expand=True, fill=BOTH, padx=4, pady=2)
        self.filter_tag_label.bind("<Button-3>", lambda event: self.close(event))

        # add tooltip
        self.tooltip = CreateToolTip(self.filter_tag_label, text=tooltip_text)

    def close(self, event=None):
        self.destroy()

