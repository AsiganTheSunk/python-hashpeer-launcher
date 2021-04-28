from tkinter import *
from PIL import ImageTk, Image
from component_filters.constants import DEFAULT_TEXT_COLOR, DEFAULT_BACKGROUND_COLOR, DEFAULT_DARK_BACKGROUND_COLOR, \
    DEFAULT_MEDIUM_DARK_BACKGROUND_COLOR, DEFAULT_FONT_STYLE, DEFAULT_FONT_SIZE, DEFAULT_DIMMED_TEXT_COLOR, \
    DEFAULT_SELECTED_UNDER_SCORE_TAB, DEFAULT_SELECTED_AND_NOT_ACTIVE_UNDER_SCORE_TAB

display_placeholder = './interface/resources/placeholders/display_placeholder.png'


class DisplayBox(Frame):
    def __init__(self, master, width, height, background='red'):
        Frame.__init__(self, master, width=width, height=height, background=background)
        self.channels_label = None
        self.acodec_label = None
        self.bit_label = None
        self.vcodec_label = None
        self.resolution_label = None

        self.main_theme = '#ADD8E6'
        self.highlight_theme = '#91B6CE'
        self.on_create()

    def on_create(self):
        self.flag_box = Frame(self)

        # Generating the Spots for the Images
        tmp_img = Image.open('./old_implementation/interface/resources/placeholders/display_placeholder.png')

        # Setting up image loading
        placeholder = ImageTk.PhotoImage(tmp_img)
        self.flag_box.placeholder = placeholder

        # # Generating the Spots for the Images
        # tmp_img = Image.open(display_placeholder)

        # # Setting up image loading
        # placeholder = ImageTk.PhotoImage(tmp_img)
        # flag_box.placeholder = placeholder
        # self.dummy_label = Label(self, width=2, height=2, background=self.main_theme)
        # self.dummy_label.pack(fill=BOTH, side=LEFT)

        self.resolution_label = Label(self, width=86, height=44, background=DEFAULT_BACKGROUND_COLOR,
                                      borderwidth=0, image=placeholder)
        self.resolution_label.pack(fill=X, side=LEFT, padx=3)

        self.vcodec_label = Label(self, width=86, height=44, background=DEFAULT_BACKGROUND_COLOR,
                                  borderwidth=0, image=placeholder)
        self.vcodec_label.pack(fill=X, side=LEFT, padx=3)

        self.bit_label = Label(self, width=86, height=44, background=DEFAULT_BACKGROUND_COLOR,
                               borderwidth=0, image=placeholder)
        self.bit_label.pack(fill=X, side=LEFT, padx=3)

        self.acodec_label = Label(self, width=86, height=44, background=DEFAULT_BACKGROUND_COLOR,
                                  borderwidth=0, image=placeholder)
        self.acodec_label.pack(fill=X, side=LEFT, padx=3)

        self.channels_label = Label(self, width=86, height=44, background=DEFAULT_BACKGROUND_COLOR,
                                    borderwidth=0, image=placeholder)
        self.channels_label.pack(fill=X, side=LEFT, padx=3)

    def set_image(self, quality, vcodec, bit, acodec, channels):
        aux_list = []
        aux_list.append(self.get_quality_img(quality))
        aux_list.append(self.get_vcodec_img(vcodec))
        aux_list.append(self.get_bit_img(bit))
        aux_list.append(self.get_acodec_img(acodec))
        aux_list.append(self.get_channels_img(channels))

        aux = []
        for i in range(0, 5, 1):
            if aux_list[i] != display_placeholder:
                aux.append(aux_list[i])

        for i in range(len(aux), 5, 1):
            aux.append(display_placeholder)

        img0 = Image.open(aux[0])
        img1 = Image.open(aux[1])
        img2 = Image.open(aux[2])
        img3 = Image.open(aux[3])
        img4 = Image.open(aux[4])

        # Setting up image loading
        _img0 = ImageTk.PhotoImage(img0)
        self.flag_box._img0 = _img0

        _img1 = ImageTk.PhotoImage(img1)
        self.flag_box._img1 = _img1

        _img2 = ImageTk.PhotoImage(img2)
        self.flag_box._img2 = _img2

        _img3 = ImageTk.PhotoImage(img3)
        self.flag_box._img3 = _img3

        _img4 = ImageTk.PhotoImage(img4)
        self.flag_box._img4 = _img4

        self.resolution_label.configure(image=_img4)
        self.vcodec_label.configure(image=_img3)
        self.bit_label.configure(image=_img2)
        self.acodec_label.configure(image=_img1)
        self.channels_label.configure(image=_img0)

    @staticmethod
    def get_bit_img(stream):
        if '10bit' == stream:
            return './interface/resources/60x48px/10_bit.png'
        return display_placeholder

    @staticmethod
    def get_quality_img(stream):
        if '4K' == stream:
            return './interface/resources/60x48px/4K.png'
        if '1080p' == stream:
            return './interface/resources/60x48px/1080.png'
        if '720p' == stream:
            return './interface/resources/60x48px/720.png'
        if '480p' in stream:
            return './interface/resources/60x48px/480.png'
        return display_placeholder

    @staticmethod
    def get_vcodec_img(stream):
        if 'x265' == stream:
            print(stream)
            return './interface/resources/60x48px/h265.png'
        elif 'H265' == stream:
            return './interface/resources/60x48px/h265.png'
        elif 'x264' == stream:
            print(stream)
            return './interface/resources/60x48px/x264.png'
        elif 'H264' == stream:
            print(stream)
            return './interface/resources/60x48px/x264.png'
        elif 'divx' in stream:
            return './interface/resources/60x48px/divx.png'
        return display_placeholder

    @staticmethod
    def get_channels_img(stream):
        if '5.1' == stream:
            return './interface/resources/60x48px/6.png'
        elif '6.0' == stream:
            return './interface/resources/60x48px/6.png'
        elif '6.1' == stream:
            return './interface/resources/60x48px/6.png'
        elif'6CH' == stream:
            return './interface/resources/60x48px/6.png'
        elif '7.1' == stream:
            return './interface/resources/60x48px/8.png'
        return display_placeholder

    @staticmethod
    def get_acodec_img(stream):
        if 'mp3' in stream:
            return './interface/resources/60x48px/mp3.png'
        if 'aac' == stream:
            return './interface/resources/60x48px/aac.png'
        elif 'ac3' == stream:
            return './interface/resources/60x48px/dolby.png'
        elif 'dts' in stream:
            return './interface/resources/60x48px/dts.png'
        return display_placeholder
