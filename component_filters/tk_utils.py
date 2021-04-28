from re import search, IGNORECASE
from component_filters.constants import DEFAULT_BACKGROUND_COLOR, DEFAULT_MEDIUM_DARK_BACKGROUND_COLOR
from tkinter import FLAT

class TkUtils(object):
    def is_valid_digit(self, text, pattern):
        try:
            if text.isdigit():
                search(pattern, text, IGNORECASE).group(0)
                return True
            return False
        except AttributeError:
            return False

    @staticmethod
    def is_digit_season(text):
        try:
            if text.isdigit():
                search(r'[0-9]{1,2}', text, IGNORECASE).group(0)
                return True
            return False
        except AttributeError:
            return False

    @staticmethod
    def is_digit_episode(text):
        try:
            if text.isdigit():
                search(r'[0-9]{1,3}', text, IGNORECASE).group(0)
                return True
            return False
        except AttributeError:
            return False

    @staticmethod
    def is_year(text):
        try:
            if text.isdigit():
                search(r'[0-9]{4}', text, IGNORECASE).group(0)
                return True
            return False
        except AttributeError:
            return False

    @staticmethod
    def get_displacement_from_root(widget, padx, pady):
        x, y, cx, cy = widget.bbox("insert")
        x = x + widget.winfo_rootx() + padx
        y = y + cy + widget.winfo_rooty() + pady
        return x, y

    @staticmethod
    def sync_window(widget, root, padx, pady):
        if root is not None:
            root.wm_overrideredirect(1)
            root.wm_geometry("+%d+%d" % TkUtils.get_displacement_from_root(widget, padx, pady))
            # root.attributes('-topmost', 1)
            # root.attributes('-topmost', 0)
            # root.focus_set()
            print('< Configure Event: Sync >')

    @staticmethod
    def get_monitor_resolution(root):
        return root.winfo_screenwidth(), root.winfo_screenheight()

    @staticmethod
    def scale_root_resolution(root, scale_x, scale_y):
        _width, _height = TkUtils.get_monitor_resolution(root)
        root.geometry('%dx%d+%d+%d' % (_width / scale_x, _height / scale_y, _width * 0.42, _height * 0.15))
        root.configure(bg=DEFAULT_BACKGROUND_COLOR, highlightbackground='grey', highlightcolor='grey', relief=FLAT, highlightthickness=1)
        return root
