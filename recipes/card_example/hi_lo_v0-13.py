'''Hi-Lo, 2 card  V0.13'''
from tkinter import Tk, Button, Label, LabelFrame, PhotoImage,  \
messagebox, DISABLED, NORMAL, E, W
import random
import winsound

# Pylint rated 8.38, loads of globals used. Ouch!

# Set up Tk frame and window.
ROOT = Tk()
ROOT.title('H-Lo V0.13')
ROOT.geometry('224x181')

# Frame for the two card images.
FRAME1 = LabelFrame(ROOT)
FRAME1.grid(row=0, column=0)

# Frame for the buttons.
FRAME0 = LabelFrame(ROOT)
FRAME0.grid(row=0, column=1)

# Frame for printing messages.
FRAME2 = LabelFrame(ROOT)
FRAME2.grid(row=2, column=0, columnspan=2, sticky=W+E)

# Frame for printng the scores
FRAME3 = LabelFrame(ROOT)
FRAME3.grid(row=1, column=0, columnspan=2, sticky=W+E)

# Set initial scores globally
# but thee cant be modified inside a function
POINTS_WON = 0
HIGH_SCORE = 0


def setup_card_one():
    ''' Get card 1 randomly and display'''
    global CARD1_VAL
    get_rnd_card()
    CARD_ONE = NEW_CARD+".png" #card image filename
    CARD1_VAL = random_card #card number 1-14
    BUT1 = Button(FRAME1)
    PHOTO = PhotoImage(file='cards\\'+str(CARD_ONE))
    BUT1.config(image=PHOTO)
    BUT1.grid(row=0, column=0, padx=2, pady=2)
    BUT1.photo = PHOTO


def setup_card_two():
    '''Get rnd card for card 2. Only display back of card 2 though.'''
    global CARD2_VAL
    get_rnd_card()
    CARD2_VAL = random_card #card number 1-14
    BUT2 = Button(FRAME1)
    PHOTO2 = PhotoImage(file='cards/blank.png')
    BUT2.config(image=PHOTO2)
    BUT2.grid(row=0, column=1, padx=2, pady=2)
    BUT2.photo = PHOTO2


def show_card_two():
    '''reveal card two'''
    but_2a = Button(FRAME1)
    photo_2a = PhotoImage(file='cards\\'+str(NEW_CARD)+".png")
    but_2a.config(image=photo_2a)
    but_2a.grid(row=0, column=1, padx=2, pady=2)
    but_2a.photo = photo_2a


def get_rnd_card():
    '''Get a new random card'''
    global NEW_CARD
    global random_card
    global random_suit

    # Note: Ace=14 (highest card), Jack=11, Queen=12, King=13, joker=?
    # Joker is wild-not implemented yet
    random_card = random.randint(1, 13)
    random_suit = random.randint(1, 4)

    #make ace highest card
    if random_card == 1:
        random_card = 14

    # Only have clubs ready at the mo, so setting all suits as clubs for now.
    if random_suit == 1:
        card_suit = "clubs"
    if random_suit == 2:
        card_suit = "clubs"
    if random_suit == 3:
        card_suit = "clubs"
    if random_suit == 4:
        card_suit = "clubs"

    NEW_CARD = str(random_card)+"-"+str(card_suit)


def clicked_higher():
    '''clicked on "Higher" button'''
    global POINTS_WON #need to oassign global as going to change values
    global HIGH_SCORE

    if CARD1_VAL < CARD2_VAL or CARD1_VAL == CARD2_VAL:
        POINTS_WON = POINTS_WON +1

        #update highscore
        if POINTS_WON > HIGH_SCORE:
            HIGH_SCORE = POINTS_WON

        update_score()
        print_correct()
        NR_BUT.configure(state=NORMAL)
        HI_BUT.configure(state=DISABLED)
        LO_BUT.configure(state=DISABLED)

    else:
        print_wrong()
        show_card_two()
        game_over_man()
        return

    show_card_two()


def clicked_lower():
    '''Clicked on "Lower" button'''
    global POINTS_WON
    global HIGH_SCORE

    if CARD1_VAL > CARD2_VAL or CARD1_VAL == CARD2_VAL:
        POINTS_WON = POINTS_WON +1

        if POINTS_WON > HIGH_SCORE:
            HIGH_SCORE = POINTS_WON

        update_score()
        print_correct()
        NR_BUT.configure(state=NORMAL)
        HI_BUT.configure(state=DISABLED)
        LO_BUT.configure(state=DISABLED)
    else:
        print_wrong()
        show_card_two()
        game_over_man()
        return

    show_card_two()


def update_score():
    '''Update score'''
    LAB1 = Label(FRAME3,  \
    text='Score :'+str(POINTS_WON)+"  Best :"+str(HIGH_SCORE)+"    ")
    LAB1.grid(row=1, column=0, pady=2, sticky=W)


def print_correct():
    '''Print "Correct" message'''
    LAB1 = Label(FRAME2, fg="green", text='WELL DONE!           ')
    LAB1.grid(row=2, column=0, pady=2, sticky=W)


def print_wrong():
    '''Print "Wrong" message'''
    LAB1 = Label(FRAME2, fg="red", text='UNLUCKY!              ')
    LAB1.grid(row=2, column=0, pady=2, sticky=W)


def print_higher_or_lower():
    '''Print "Higher or Lower" message"'''
    LAB1 = Label(FRAME2, fg="blue", text='HIGHER OR LOWER?')
    LAB1.grid(row=2, column=0, pady=2, sticky=W)


def clicked_next():
    '''Clicked on "Next" button'''
    setup_card_one()
    setup_card_two()
    print_higher_or_lower()
    update_score()
    NR_BUT.configure(state=DISABLED)
    HI_BUT.configure(state=NORMAL)
    LO_BUT.configure(state=NORMAL)


def new_game():
    '''Start a new game, retaining high score'''
    global POINTS_WON
    POINTS_WON = 0
    update_score()
    print_higher_or_lower()
    setup_card_one()
    setup_card_two()


def game_over_man():
    '''Game over because guessed wrong'''
    global HIGH_SCORE

    messagebox.showinfo  \
    ('OUCH!', '   G A M E  O V E R  M A N\nClick OK to play a new game')

    if POINTS_WON > HIGH_SCORE:
        HIGH_SCORE = POINTS_WON
    new_game()

# Higher-Lower buttons
HI_BUT = Button(FRAME0, bg='skyblue', text='HIGHER', command=clicked_higher)
HI_BUT.grid(row=0, column=0, pady=3, sticky=W+E)
LO_BUT = Button(FRAME0, bg='orange', text='LOWER ', command=clicked_lower)
LO_BUT.grid(row=1, column=0, pady=3, sticky=W+E)
NR_BUT = Button(FRAME0, bg='plum', text='NEXT', command=clicked_next)
NR_BUT.grid(row=2, column=0, pady=3, sticky=W+E)
NR_BUT.configure(state=DISABLED)

# Main.
new_game()

ROOT.mainloop()
