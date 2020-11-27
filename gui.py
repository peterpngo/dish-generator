import tkinter
from tkinter import *
from tkinter import ttk

import random
import dgitemlist

import os
os.system('cls')

root = Tk()
colFrame = ttk.Frame(root, width=150)
colFrame1 = ttk.Frame(root, width=150)
colFrame2 = ttk.Frame(root, width=150)
colFrame3 = ttk.Frame(root, width=150)
colFrame4 = ttk.Frame(root, width=150)
height = ttk.Frame(root, height=100)
spacer = ttk.Frame(root, height=30)
titlelbl = ttk.Label(root, text="Dish Generator")

item = ttk.Label(root, text='Protein')
item1 = ttk.Label(root, text='Vegetable')
item2 = ttk.Label(root, text='Starch')
item3 = ttk.Label(root, text='Sauce')
item4 = ttk.Label(root, text='Garnish/Accent')

protein = tkinter.StringVar()
vegetable = tkinter.StringVar()
starch = tkinter.StringVar()
sauce = tkinter.StringVar()
garnish = tkinter.StringVar()
protein.set("  ")
vegetable.set("  ")
starch.set("  ")
sauce.set("  ")
garnish.set("  ")

def generate():
    protein.set(random.choice(dgitemlist.protein))
    vegetable.set(random.choice(dgitemlist.vegetable))
    starch.set(random.choice(dgitemlist.starch))
    sauce.set(random.choice(dgitemlist.starch))
    garnish.set(random.choice(dgitemlist.garnish))    

proteinSlot = ttk.Label(root, textvariable = protein)
vegetableSlot = ttk.Label(root, textvariable = vegetable)
starchSlot = ttk.Label(root, textvariable = starch)
sauceSlot = ttk.Label(root, textvariable = sauce)
garnishSlot = ttk.Label(root, textvariable = garnish)

genButton = ttk.Button(text="  Generate  ", command=generate)

titlelbl.grid(column=2, row=1)

height.grid(column=6)
colFrame.grid(column=0, row=0)
colFrame1.grid(column=1, row=0)
colFrame2.grid(column=2, row=0)
colFrame3.grid(column=3, row=0)
colFrame4.grid(column=4, row=0)

item.grid(column=0, row=2,)
item1.grid(column=1, row=2,)
item2.grid(column=2, row=2,)
item3.grid(column=3, row=2,)
item4.grid(column=4, row=2,)

proteinSlot.grid(column=0, row=3)
vegetableSlot.grid(column=1, row=3)
starchSlot.grid(column=2, row=3)
sauceSlot.grid(column=3, row=3)
garnishSlot.grid(column=4, row=3)

spacer.grid(row=4)
genButton.grid(column=2, row=9)

root.mainloop()


"""
class MyGUI:
    def __init__(self):
        self.mainWindow = tkinter.Tk()
        self.mainWindow.geometry("800x250")

        self.titleFrame = tkinter.grid(row=1, column=3)
        self.centerFrame = tkinter.Frame(self.mainWindow)
        self.bottomFrame = tkinter.Frame(self.mainWindow)
        self.titleFrame.pack(side='top')
        self.centerFrame.pack()
        self.bottomFrame.pack(side='bottom')

        self.titleLabel = tkinter.Label(self.titleFrame, text='Dish Generator')
        self.titleLabel.pack()

        self.var = tkinter.StringVar()
        self.var1 = tkinter.StringVar()
        self.var2 = tkinter.StringVar()
        self.var.set("  ")
        self.var1.set("  ")
        self.var2.set("  ")  

        self.button = tkinter.Button(self.bottomFrame, text='Generate!', command=self.eng)
        self.button.pack()

        self.engLabel = tkinter.Label(self.centerFrame, textvariable = self.var)
        self.engLabel1 = tkinter.Label(self.centerFrame, textvariable = self.var1)
        self.engLabel2 = tkinter.Label(self.centerFrame, textvariable = self.var2)

        self.engLabel.pack()
        self.engLabel1.pack()
        self.engLabel2.pack()

        tkinter.mainloop()

    def eng(self):
            self.var.set("Left")
        
    def eng1(self):
            self.var1.set("Right")

    def eng2(self):
            self.var2.set("Center")


my_gui = MyGUI()
"""