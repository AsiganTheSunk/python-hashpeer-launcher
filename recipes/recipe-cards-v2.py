import random
from tkinter import *
from PIL import Image, ImageTk

suits = ["Blue-Card-", "Red-Card-", "Green-Card-", "Yellow-Card-"]
values = ['A', 'B']
pics = {}

class Card(object):
    cards = [x + y for x in suits for y in values]

    def __init__(self, suit=None, value=None, up=True):
        self.down_img = None
        self.image = None

        if suit in suits:
            self.suit = suit
        else:
            self.suit = random.choice(suits)
        if value in values:
            self.value = value
        else:
            self.value = random.choice(values)
        self.up = up

    def __str__(self):
        return self.value + self.suit

    def picURL(self):
        return pics[self.suit + self.value]

    def display(self, canvas, x, y, angle):
        if self.up:
            image = pics[self.suit + self.value]
        else:
            image = self.down_img
        image = image.rotate(angle)
        self.image = ImageTk.PhotoImage(image)
        canvas.create_image(x, y, image=self.image)

    def key(self):
        # returns hash value of 20*suit + value -- guaranteed unique; sorts
        # by color.
        return 20 * ('SHCD'.find(self.suit)) + values.index(self.value)

    @staticmethod
    def create_images():
        for x in Card.cards:
            pics[x] = Image.open('./images' + x + '.png')
        Card.down_img = Image.open('images/Deck1.png')


class Deck(Card):
    deck = Card.cards[:]

    def __init__(self, suit=None, value=None, up=True):
        super().__init__(suit, value, up)
        card = str(suit) + str(value)
        if card not in Deck.deck:
            if not Deck.deck:
                raise ValueError
            card = random.choice(Deck.deck)
            suit = card[0]
            value = card[1:]
        Deck.deck.remove(card)
        self.suit = suit
        self.value = value
        self.up = up

    @staticmethod
    def shuffle():
        Deck.deck = Card.cards[:]


class BridgeRound(Frame):
    # display_data contains display info for each hand:
    # (startx, starty, dx, dy, angle of rotation)
    display_data = [(150, 50, 12, 0, 0),
                    (390, 40, 0, 15, 270),
                    (290, 220, -12, 0, 180),
                    (50, 220, 0, -15, 90)]

    def __init__(self, master):
        Frame.__init__(self, master)
        self.canvas = Canvas(self)
        # self.grid()
        self.deal()
        self.display()
        self.canvas.grid()
        self.grid()

    def deal(self):
        Deck.shuffle()
        self.hands = [[Deck() for i in range(13)] for j in range(4)]

    def display(self):
        Card.create_images()
        for i in range(4):
            hand = self.hands[i]
            hand.sort(key=lambda x: x.key())
            x, y, dx, dy, angle = BridgeRound.display_data[i]
            for j in hand:
                # print j,
                j.display(self.canvas, x, y, angle)
                x += dx
                y += dy


mainw = Tk()
mainw.f = BridgeRound(mainw)
mainw.mainloop()