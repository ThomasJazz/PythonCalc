from Tkinter import *
import Tkinter as tk

calculator = Tk()
calculator.title("PyCalc")
calculator.resizable(False,False)

class Pycalc(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.createButtons()

    def addToDisplay(self, text):
        self.entryText = self.display.get()
        self.textLength = len(self.entryText)

        if self.entryText == "0":
            self.replaceText(text)
        else:
            self.display.insert(self.textLength, text)

    def evalDisplay(self):
        self.userFunction = self.display.get()
        self.replaceText(eval(self.userFunction))

    def clearDisplay(self):
        self.replaceText("0")

    def replaceText(self, text):
        self.display.delete(0, END)
        self.display.insert(0, text)

    def createButtons(self):
        self.display = Entry(self, font=("Helvetica", 16), relief=RAISED, justify=RIGHT)
        self.display.insert(0, "0")
        self.display.grid(row=0, column=0, columnspan=4)

        self.clearButton = Button(self, font=("Helvetica", 12), text="C", borderwidth=1, command=lambda: self.clearDisplay())
        self.clearButton.grid(row=1, column=0, sticky="NWNESWSE")

        self.expButton = Button(self, font=("Helvetica", 12), text="^", borderwidth=1, command=lambda: self.addToDisplay("**"))
        self.expButton.grid(row=1, column=1, sticky="NWNESWSE")

        self.modButton = Button(self, font=("Helvetica", 12), text="%", borderwidth=1, command=lambda: self.addToDisplay("%"))
        self.modButton.grid(row=1, column=2, sticky="NWNESWSE")

        self.divideButton = Button(self, font=("Helvetica", 12), text="/", borderwidth=1, command=lambda: self.addToDisplay("/"))
        self.divideButton.grid(row=1, column=3, sticky="NWNESWSE")

        self.sevenButton = Button(self, font=("Helvetica", 12), text="7", borderwidth=1, command=lambda: self.addToDisplay("7"))
        self.sevenButton.grid(row=2, column=0, sticky="NWNESWSE")

        self.eightButton = Button(self, font=("Helvetica", 12), text="8", borderwidth=1, command=lambda: self.addToDisplay("8"))
        self.eightButton.grid(row=2, column=1, sticky="NWNESWSE")

        self.nineButton = Button(self, font=("Helvetica", 12), text="9", borderwidth=1, command=lambda: self.addToDisplay("9"))
        self.nineButton.grid(row=2, column=2, sticky="NWNESWSE")

        self.multButton = Button(self, font=("Helvetica", 12), text="*", borderwidth=1, command=lambda: self.addToDisplay("*"))
        self.multButton.grid(row=2, column=3, sticky="NWNESWSE")
        #
        self.fourButton = Button(self, font=("Helvetica", 12), text="4", borderwidth=1, command=lambda: self.addToDisplay("4"))
        self.fourButton.grid(row=3, column=0, sticky="NWNESWSE")

        self.fiveButton = Button(self, font=("Helvetica", 12), text="5", borderwidth=1, command=lambda: self.addToDisplay("5"))
        self.fiveButton.grid(row=3, column=1, sticky="NWNESWSE")

        self.sixButton = Button(self, font=("Helvetica", 12), text="6", borderwidth=1, command=lambda: self.addToDisplay("6"))
        self.sixButton.grid(row=3, column=2, sticky="NWNESWSE")

        self.minButton = Button(self, font=("Helvetica", 12), text="-", borderwidth=1, command=lambda: self.addToDisplay("-"))
        self.minButton.grid(row=3, column=3, sticky="NWNESWSE")

        self.oneButton = Button(self, font=("Helvetica", 12), text="1", borderwidth=1, command=lambda: self.addToDisplay("1"))
        self.oneButton.grid(row=4, column=0, sticky="NWNESWSE")

        self.twoButton = Button(self, font=("Helvetica", 12), text="2", borderwidth=1, command=lambda: self.addToDisplay("2"))
        self.twoButton.grid(row=4, column=1, sticky="NWNESWSE")

        self.threeButton = Button(self, font=("Helvetica", 12), text="3", borderwidth=1, command=lambda: self.addToDisplay("3"))
        self.threeButton.grid(row=4, column=2, sticky="NWNESWSE")

        self.addButton = Button(self, font=("Helvetica", 12), text="+", borderwidth=1, command=lambda: self.addToDisplay("+"))
        self.addButton.grid(row=4, column=3, sticky="NWNESWSE")

        self.zeroButton = Button(self, font=("Helvetica", 12), text="0", borderwidth=1, command=lambda: self.addToDisplay("0"))
        self.zeroButton.grid(row=5, column=0, sticky="NWNESWSE", columnspan=2)

        self.decButton = Button(self, font=("Helvetica", 12), text=".", borderwidth=1, command=lambda: self.addToDisplay("."))
        self.decButton.grid(row=5, column=2, sticky="NWNESWSE")

        self.equalsButton = Button(self, font=("Helvetica", 12), text="=", borderwidth=1, command=lambda: self.evalDisplay())
        self.equalsButton.grid(row=5, column=3, sticky="NWNESWSE")


calc = Pycalc(calculator).grid()

calculator.mainloop()
