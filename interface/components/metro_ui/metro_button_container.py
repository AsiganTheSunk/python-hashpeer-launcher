from tkinter import (
    Button, FLAT
)


class MetroButtonContainer(Button):
    def __init__(self, master, text, background, foreground="white",
                 opacity=0.8, font=None, command=None, padx=5, pady=6):
        opacity = float(opacity)

        if background.startswith("#"):
            r, g, b = hex2rgb(background)
        else:
            # Color name
            r, g, b = master.winfo_rgb(background)

        r = int(opacity*r)
        g = int(opacity*g)
        b = int(opacity*b)

        # if r <= 255 and g <= 255 and b <=255:
        #     activebackground = '#%02x%02x%02x' % (r, g, b)
        # else:
        #     activebackground = '#%04x%04x%04x' % (r, g, b)

        Button.__init__(self, master, text=text,
                        activebackground=background, background=background,
                        activeforeground='#87939A', foreground='#87939A',
                        relief=FLAT, padx=padx, pady=pady, borderwidth=1, highlightthickness=1,
                        highlightbackground='black')
        if font:
            self.configure(font=font)

        if command:
            self.configure(command=command)

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, *args):
        DEFAULT_BUTTON_MOUSE_OVER = '#4F5254'
        self.configure(background=DEFAULT_BUTTON_MOUSE_OVER)

    def on_leave(self, *args):
        DEFAULT_BACKGROUND_COLOR = '#3C3F41'
        self.configure(background=DEFAULT_BACKGROUND_COLOR)


def hex2rgb(str_rgb):
    try:
        rgb = str_rgb[1:]

        if len(rgb) == 6:
            r, g, b = rgb[0:2], rgb[2:4], rgb[4:6]
        elif len(rgb) == 3:
            r, g, b = rgb[0] * 2, rgb[1] * 2, rgb[2] * 2
        else:
            raise ValueError()
    except:
        raise ValueError("Invalid value %r provided for rgb color."% str_rgb)

    return tuple(int(v, 16) for v in (r, g, b))