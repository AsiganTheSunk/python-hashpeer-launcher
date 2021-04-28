import tkinter as tk


class Example:
    def __init__(self):
        self.root = tk.Tk()
        label = tk.Label(self.root, text="Move me around...")
        label.pack(side="top", fill="both", expand=True, padx=20, pady=20)

        self.top = tk.Toplevel()
        label = tk.Label(self.top, text="... and I will follow!")
        label.pack(side="top", fill="both", expand=True, padx=20, pady=20)

        self.root.bind("<Configure>", self.sync_windows)

    def start(self):
        self.root.mainloop()

    def sync_windows(self, event=None):
        x = self.root.winfo_x() + self.root.winfo_width() + 4
        y = self.root.winfo_y()
        self.top.geometry("+%d+%d" % (x, y))


Example().start()
