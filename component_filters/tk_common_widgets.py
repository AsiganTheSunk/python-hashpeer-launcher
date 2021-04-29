from tkinter import Frame, FLAT, X, Y, LEFT
from component_filters.constants import (
    DEFAULT_TEXT_COLOR, DEFAULT_BACKGROUND_COLOR, DEFAULT_DARK_BACKGROUND_COLOR,
    DEFAULT_MEDIUM_DARK_BACKGROUND_COLOR, DEFAULT_FONT_STYLE, DEFAULT_FONT_SIZE, DEFAULT_DIMMED_TEXT_COLOR,
    DEFAULT_SELECTED_UNDER_SCORE_TAB, DEFAULT_SELECTED_AND_NOT_ACTIVE_UNDER_SCORE_TAB
)


class TkCommonWidgets:
    @staticmethod
    def horizontal_separator(root, background_color='Grey', height=1, padx=0, pady=0):
        if background_color is not None:
            horizontal_separator = Frame(root, height=height, bg=background_color, relief=FLAT)
        else:
            horizontal_separator = Frame(root, height=height, relief=FLAT)
        horizontal_separator.pack(fill=X, padx=padx, pady=pady)

    @staticmethod
    def vertical_separator(root_container, background_color=DEFAULT_BACKGROUND_COLOR, side=LEFT, fill=Y):
        metro_label_frame_container = Frame(root_container, background=background_color, width=6)
        metro_label_frame_container.pack(side=side, fill=fill)
