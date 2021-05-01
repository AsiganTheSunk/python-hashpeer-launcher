from PIL import ImageTk, Image


class TkImageUtils:
    @staticmethod
    def load_image(image_path):
        _open_image = Image.open(image_path)
        return ImageTk.PhotoImage(_open_image)