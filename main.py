from interface.component_filters.tk_utils import TkUtils
from interface.search.search_container import SearchContainer
from interface.search.search_result_container import SearchResultContainer
from tkinter import *
from interface.metro_tile_bar.tile_bar import MetroTileBar

if __name__ == '__main__':
    scale_x: float = 2.0
    scale_y: float = 1.67
    root = Tk()
    root = TkUtils.scale_root_resolution(root=root, scale_x=scale_x, scale_y=scale_y)

    # root.overrideredirect(True)
    # root.attributes('-topmost', True)
    # win.config(bg=color3)
    #
    # win.geometry("1366x728+0+0")
    # win.title("Calculator")
    # win.iconbitmap("wd.ico")

    MetroTileBar(root)
    SearchContainer(root)
    SearchResultContainer(root)
    root.mainloop()
