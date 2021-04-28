from tkinter import Tk, Listbox, Frame, Scrollbar, VERTICAL


class ScrollableListbox(Listbox):
    def __init__(self, master, *arg, **key):
        self.frame = Frame(master)
        self.yscroll = Scrollbar(self.frame, orient=VERTICAL)
        Listbox.__init__(self, self.frame, yscrollcommand=self.yscroll.set, *arg, **key)
        self.yscroll['command'] = self.yview

    def grid(self, *arg, **key):
        self.frame.grid(*arg, **key)
        Listbox.grid(self, row=0, column=0, sticky='nswe')
        self.yscroll.grid(row=0, column=1, sticky='ns')


if __name__ == "__main__":
    root = Tk()
    root.geometry("930x530")
    scroll = ScrollableListbox(root)

    scroll.pack(fill="both", expand=True)
    root.mainloop()