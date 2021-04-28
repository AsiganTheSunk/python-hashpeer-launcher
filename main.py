from component_filters.tk_utils import TkUtils
from search_block import SearchBlock
from search_result_block import SearchResultBlock
from custom_title_bar import CustomTitleBar
from tkinter import *
from metro_tile_bar.tile_bar import MetroTileBar

if __name__ == '__main__':
    scale_x: float = 2.0
    scale_y: float = 1.62
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
    SearchBlock(root)
    SearchResultBlock(root)
    root.mainloop()
