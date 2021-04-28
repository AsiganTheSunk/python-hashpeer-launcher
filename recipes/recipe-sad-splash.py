#ImportLibrarHere

from tkinter import *

from tkinter import ttk

import time

import datetime

from PIL import ImageTk,Image

import os

import sqlite3

from tkinter import messagebox

#SplashScreen

sroot = Tk()

sroot.minsize(height=200,width=300)

sroot.title("Splash window")

sroot.configure()

spath = "../Kong Skull Island_Film_Poster.png"

simg = ImageTk.PhotoImage(Image.open(spath))

my = Label(sroot,image=simg)

my.image = simg

my.place(x=0,y=0)

Frame(sroot,height=516,width=5,bg='black').place(x=520,y=0)

lbl1 = Label(sroot,text="Welcome to Codersarts",font='Timesnewroman 20 ',fg='blue')

lbl1.config(anchor=CENTER)

lbl1.pack(padx = 100, pady = 100)

#MainScreen

def mainroot():
    root = Tk()

    root.geometry('1080x500')

    root.minsize(width=1080, height=550)

    root.maxsize(width=1080, height=550)

    root.configure(bg='white')

    root.title("main window")


#AddWindowFunctionalityHere(like widgets, etc)

#EndOfMainWindow

# After this call the main window here

def call_mainroot():

	sroot.destroy()

	mainroot()

sroot.after(3000,call_mainroot)         #TimeOfSplashScreen

mainloop()