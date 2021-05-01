from tkinter import *
from PIL import ImageTk, Image
from interface.component_filters.constants import DEFAULT_TEXT_COLOR, DEFAULT_BACKGROUND_COLOR, DEFAULT_DARK_BACKGROUND_COLOR, \
    DEFAULT_MEDIUM_DARK_BACKGROUND_COLOR, DEFAULT_FONT_STYLE, DEFAULT_FONT_SIZE, DEFAULT_DIMMED_TEXT_COLOR, \
    DEFAULT_SELECTED_UNDER_SCORE_TAB, DEFAULT_SELECTED_AND_NOT_ACTIVE_UNDER_SCORE_TAB

from interface.component_filters.tk_image_utils import TkImageUtils
from interface.search.page.constants.banner_display_constants import BANNER_LABEL_PLACEHOLDER


class MultimediaBannerContainer(Frame):
    def __init__(self, master, width, height, background='red'):
        Frame.__init__(self, master, width=width, height=height, background=background)

        self.flag_box = Frame(self)
        placeholder = TkImageUtils.load_image(BANNER_LABEL_PLACEHOLDER)

        # note: ResolutionBanner, VCodecLabel, BitLabel, ACodecLabel, ChannelsLabel
        self.flag_box.placeholder = placeholder
        self.resolution_label = self.init_banner_label(placeholder)
        self.vcodec_label = self.init_banner_label(placeholder)
        self.bit_label = self.init_banner_label(placeholder)
        self.acodec_label = self.init_banner_label(placeholder)
        self.channels_label = self.init_banner_label(placeholder)

    def init_banner_label(self, image_placeholder):
        banner_label = Label(self, width=86, height=44, background=DEFAULT_BACKGROUND_COLOR,
                             borderwidth=0, image=image_placeholder)
        banner_label.pack(fill=X, side=LEFT, padx=3)
        return banner_label

    def set_image(self, quality, vcodec, bit, acodec, channels):
        aux_list = [
            self.get_quality_img(quality),
            self.get_vcodec_img(vcodec),
            self.get_bit_img(bit),
            self.get_acodec_img(acodec),
            self.get_channels_img(channels)
        ]

        aux = []
        for i in range(0, 5, 1):
            if aux_list[i] != BANNER_LABEL_PLACEHOLDER:
                aux.append(aux_list[i])

        for i in range(len(aux), 5, 1):
            aux.append(BANNER_LABEL_PLACEHOLDER)

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
        return BANNER_LABEL_PLACEHOLDER

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
        return BANNER_LABEL_PLACEHOLDER

    @staticmethod
    def get_vcodec_img(stream):
        if 'x265' == stream:
            return './interface/resources/60x48px/h265.png'
        elif 'H265' == stream:
            return './interface/resources/60x48px/h265.png'
        elif 'x264' == stream:
            return './interface/resources/60x48px/x264.png'
        elif 'H264' == stream:
            return './interface/resources/60x48px/x264.png'
        elif 'divx' in stream:
            return './interface/resources/60x48px/divx.png'
        return BANNER_LABEL_PLACEHOLDER

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
        return BANNER_LABEL_PLACEHOLDER

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
        return BANNER_LABEL_PLACEHOLDER
