from tkinter import *
from tkinter.ttk import *

ENTRY_CACHE = "./entry_cache.txt"


def mstore(text):
    file = open(ENTRY_CACHE, "w")            # Create file.txt
    file.write(text)                        # Write contents of mEntryname to file
    file.close()                            # Closes text file


def msearch():                              # Stores file directory that user chose
    open_file = open(ENTRY_CACHE, 'r')      # Opens file user chose
    print(open_file.read())                 # Displays contents in console
    open_file.close()                       # Closes text file

# Window Creation and Settings
window = Tk()
window.geometry('450x500')
window.title('Form Test')

# Create Widgets
mTitle = Label (window,text='Heading Text')
mDetail = Label (window,text='Flavour you can see')
mFName = Label (window,text='Barcode', )
mEntryname = Entry(window)
# Runs mstore function when pressed (passing the contents of the entry box)
mSave = Button (window,text='Save', command = lambda: mstore(mEntryname.get()))
# Runs msearch function when pressed
mSearch = Button (window,text='Search', command=lambda: msearch())

# Render Widgets
mTitle.pack()
mDetail.pack()
mFName.pack()
mEntryname.pack()
mSave.pack()
mSearch.pack()

window.mainloop()