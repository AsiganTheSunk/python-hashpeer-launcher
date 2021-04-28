try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

import os

mainWindow = tkinter.Tk()

mainWindow.title("Grid Demo")
mainWindow.geometry('640x480-8-200')
mainWindow['padx'] = 8  # padding, aka spatiu liber strnga dreapta
# daca era y in loc de x, era spatiu sus/jos, axa y


label = tkinter.Label(mainWindow, text="Tkinter grid Demo")
label.grid(row=0, column=0, columnspan=3)  # se intinde pe 3 coloane

mainWindow.columnconfigure(0, weight=100)  # daca nu pui weight nu e nimic centrat etc
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1000)
mainWindow.columnconfigure(3, weight=600)
mainWindow.columnconfigure(4, weight=1000)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

fileList = tkinter.Listbox(mainWindow)
fileList.grid(row=1, column=0, rowspan=2, sticky='nsew')
fileList.config(border=2, relief='raised')  # sunken, raised
for zone in os.listdir('C:\Windows\System32'):  # asta populeaza automat lista cu valori..
    fileList.insert(tkinter.END, zone)  # #end places each entry at the end
    # of the list as they're added

# command = how actions are associated with widgets
listScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=fileList.yview)
listScroll.grid(row=1, column=1, rowspan=2, sticky='nsw')
# link the scrollbox to the listbox cu yscrollcommand
# yscroll... scrolls vertycally, pe axa y
fileList['yscrollcommand'] = listScroll.set

# frame for the radio buttons; in dreapta sus
optionFrame = tkinter.LabelFrame(mainWindow, text='File Details')  # labelFrame adauga si borderul/chenarul
optionFrame.grid(row=1, column=2, sticky='ne')  # adaug frameul la grid
# sticky = 'ne' sus si dreapta in frame


rbValue = tkinter.IntVar()
rbValue.set(3)  # 3 e optiunea default (aka ce buton radio e 'bifat' initial)
# Radio buttons
# cream 3 butoane care 'impart' aceeasi variabila, facem asta
# pt ca doar unul din ele poate fi selectat in acelasi timp
# dai click pe unul, cel selectat anterior va fi deselectat
radio1 = tkinter.Radiobutton(optionFrame, text='Filename', value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(optionFrame, text='Path', value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(optionFrame, text='Timestamp', value=3, variable=rbValue)
# in optionFrame, nu mainWindow
# dar optionFrame e atasat in mainWindow

# apoi le pui pe grid:
radio1.grid(row=0, column=0, sticky='w')  # w=la stanga
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

# widget to display the result
resultLabel = tkinter.Label(mainWindow, text='Result')
resultLabel.grid(row=2, column=2, sticky='nw')  # adaugat la grid
result = tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky='sw')

# frame for the time spinners
timeFrame = tkinter.LabelFrame(mainWindow, text='Time')  # LabelFrame adauga si borderul ca mai sus
timeFrame.grid(row=3, column=0, sticky='new')
# Time spinners
hourSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0, 24)))  # de la 0 la 23
minuteSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
secondSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
# mergea facut pt toate 3 cu values in loc de from_ to, dar asa vezi si alte posibilitati
hourSpinner.grid(row=0, column=0)
tkinter.Label(timeFrame, text=':').grid(row=0, column=1)
minuteSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=':').grid(row=0, column=3)
secondSpinner.grid(row=0, column=4)
# ultimul nu are nevoie de label cu ':'
timeFrame['padx'] = 36  # puts padding inside the left and right
# edges of a widget
# pady ar fi folosit pt sus/jos

# frame for the date spinners
dateFrame = tkinter.Frame(mainWindow)
dateFrame.grid(row=4, column=0, sticky='new')
# date labels
dayLabel = tkinter.Label(dateFrame, text='Day')
monthLabel = tkinter.Label(dateFrame, text='Month')
yearLabel = tkinter.Label(dateFrame, text='Year')
dayLabel.grid(row=0, column=0, sticky='w')
monthLabel.grid(row=0, column=1, sticky='w')
yearLabel.grid(row=0, column=2, sticky='w')
# Date Spinners
daySpin = tkinter.Spinbox(dateFrame, width=5, from_=1, to=31)
monthSpin = tkinter.Spinbox(dateFrame, width=5,
                            values=("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"))
yearSpin = tkinter.Spinbox(dateFrame, width=5, from_=2000, to=2099)
daySpin.grid(row=1, column=0)
monthSpin.grid(row=1, column=1)
yearSpin.grid(row=1, column=2)

# Buttons , ok si cancel in dreapta jos
okButton = tkinter.Button(mainWindow, text='Ok')
cancelButton = tkinter.Button(mainWindow, text='Cancel', command=mainWindow.destroy)  # NU .destroy()
# command=manWindow.destroy inchide fereastra
# the correct way to asign a function to the command property
# is to just use the function name, FARA ()
# numeFunctie() nu va merge, numeFunctie va merge
# pt ca daca punem si paranteleze, we're calling the function
# ceea ce nu vrem in cazul de fata, vrem doar sa o asignam...

okButton.grid(row=4, column=3, sticky='e')
cancelButton.grid(row=4, column=4, sticky='w')

mainWindow.mainloop()

# printeaza numarul butonului radio pe care ai dat click
# dar pt ca esti in loop, nu vei vedea printul pana nu inchizi programul
# daca selectezi Path (care e al doilea buton, dupa ce iesi din program in consola printeaza '2')
print(rbValue.get())  # .get is retriving the value of the button that has been selected

""" You can bind variables to tk widgets, so that they are updated when the value of the widget changes. 
 They can also be used to set the value of a widget.
In this example, we set the radio buttons to an integer variable called rbValue. 
Changing rbValue causes different radio buttons to be selected, and selecting the different radio buttons 
changes the value of rbValue so we can tell which button's been clicked.
You can find out more information on the tk variables at http://effbot.org/tkinterbook/variable.htm """

# the weight property is used when the window is resized
# so a weight of 3 will widen 3 times faster than with weight=1
# when the window size increasez