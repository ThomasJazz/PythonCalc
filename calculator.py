from Tkinter import *
import math

# github pls
class Pycalc(Frame):
    lastEntry = 0
    concatEntries = False
    needDisplayUpdate = False

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.parent = master
        self.initialize()


    def initialize(self):
        self.grid()
        self.createButtons()


    def addToDisplay(self, text):
        self.entryText = self.display.get()
        self.textLength = len(self.entryText)

        if self.needDisplayUpdate and text in "**/-+" and not(self.entryText == "0"):
            self.replacePrev(self.entryText)
            self.needDisplayUpdate = False
            self.replaceText("Ans" + text + "")
        elif self.entryText == "0":
            self.replaceText(text)
        else:
            self.display.insert(self.textLength, text)
            self.needDisplayUpdate = False


    def evalDisplay(self):
        self.userFunction = self.display.get()
        if 'Ans' in self.userFunction:
            self.userFunction = self.userFunction.replace('Ans', self.prevAns.get())
        if 'sin(' in self.userFunction:
            self.userFunction = self.userFunction.replace('sin(', 'math.sin(')
        if 'cos(' in self.userFunction:
            self.userFunction = self.userFunction.replace('cos(', 'math.cos(')
        if 'tan(' in self.userFunction:
            self.userFunction = self.userFunction.replace('tan(', 'math.tan(')
        if 'log(' in self.userFunction:
            self.userFunction = self.userFunction.replace('log(', 'math.log10(')
        if 'sqrt(' in self.userFunction:
            self.userFunction = self.userFunction.replace('sqrt(', 'math.sqrt(')
        if 'pi' in self.userFunction:
            self.userFunction = self.userFunction.replace('pi', 'math.pi')


        self.replaceText(eval(self.userFunction))

        self.needDisplayUpdate = True

    def clearDisplay(self):
        self.replaceText("0")

    def replaceText(self, text):
        self.display.delete(0, END)
        self.display.insert(0, text)

    def replacePrev(self, text):
        self.prevAns.delete(0,END)
        self.prevAns.insert(0,text)

    def clearAll(self):
        self.clearDisplay()
        self.replacePrev("")

    def deleteLast(self):
        self.entryLen = len(self.display.get())
        if self.entryLen >= 1:
            self.display.delete(self.entryLen-1,END)
            if self.entryLen == 1:
                self.replaceText("0")


    def createButtons(self):
        self.prevAns = Entry(self, font=("Helvetica", 12), relief=RAISED, justify=RIGHT)
        self.prevAns.insert(0,"")
        self.prevAns.grid(row=0, column=0, columnspan=5, sticky="nsew")
        self.display = Entry(self, font=("Helvetica", 24), relief=RAISED, justify=RIGHT)
        self.display.insert(0, "0")
        self.display.grid(row=1, column=0, columnspan=5, sticky="nsew")

        # First row of buttons
        self.sinButton = Button(self, font=("Helvetica", 12), text="sin", borderwidth=1,
                                command=lambda: self.addToDisplay("sin("))
        self.sinButton.grid(row=2, column=0, sticky="nsew")

        self.cosButton = Button(self, font=("Helvetica", 12), text="cos", borderwidth=1,
                                command=lambda: self.addToDisplay("cos("))
        self.cosButton.grid(row=2, column=1, sticky="nsew")

        self.tanButton = Button(self, font=("Helvetica", 12), text="tan", borderwidth=1,
                                command=lambda: self.addToDisplay("tan("))
        self.tanButton.grid(row=2, column=2, sticky="nsew")

        self.logButton = Button(self, font=("Helvetica", 12), text="log", borderwidth=1,
                                command=lambda: self.addToDisplay("log("))
        self.logButton.grid(row=2, column=3, sticky="nsew")

        self.piButton = Button(self, font=("Helvetica", 12), text="Pi", borderwidth=1,
                                command=lambda: self.addToDisplay("pi"))
        self.piButton.grid(row=2, column=4, sticky="nsew")

        # Second row of buttons
        self.sinButton = Button(self, font=("Helvetica", 12), text="sqrt", borderwidth=1,
                                command=lambda: self.addToDisplay("sqrt("))
        self.sinButton.grid(row=3, column=0, sticky="nsew")

        self.cosButton = Button(self, font=("Helvetica", 12), text="Mod", borderwidth=1,
                                command=lambda: self.addToDisplay("%"))
        self.cosButton.grid(row=3, column=1, sticky="nsew")

        self.tanButton = Button(self, font=("Helvetica", 12), text="x^2", borderwidth=1,
                                command=lambda: self.addToDisplay("**2"))
        self.tanButton.grid(row=3, column=2, sticky="nsew")

        self.logButton = Button(self, font=("Helvetica", 12), text="x^3", borderwidth=1,
                                command=lambda: self.addToDisplay("**3"))
        self.logButton.grid(row=3, column=3, sticky="nsew")

        self.piButton = Button(self, font=("Helvetica", 12), text="^", borderwidth=1,
                               command=lambda: self.addToDisplay("**("))
        self.piButton.grid(row=3, column=4, sticky="nsew")

        # Third row of buttons
        self.inverseButton = Button(self, font=("Helvetica", 12), text="1/x", borderwidth=1,
                                command=lambda: self.addToDisplay("1/("))
        self.inverseButton.grid(row=4, column=0, sticky="nsew")

        self.ceButton = Button(self, font=("Helvetica", 12), text="CE", borderwidth=1,
                                command=lambda:self.clearDisplay())
        self.ceButton.grid(row=4, column=1, sticky="nsew")

        self.clearButton = Button(self, font=("Helvetica", 12), text="C", borderwidth=1,
                                command=lambda: self.clearAll())
        self.clearButton.grid(row=4, column=2, sticky="nsew")

        self.delButton = Button(self, font=("Helvetica", 12), text="Del", borderwidth=1,
                                command=lambda: self.deleteLast())
        self.delButton.grid(row=4, column=3, sticky="nsew")

        self.divButton = Button(self, font=("Helvetica", 12), text="/", borderwidth=1,
                               command=lambda: self.addToDisplay("/"))
        self.divButton.grid(row=4, column=4, sticky="nsew")



        # Fourth row of buttons
        self.eButton = Button(self, font=("Helvetica", 12), text="e", borderwidth=1,
                                command=lambda: self.addToDisplay("e"))
        self.eButton.grid(row=5, column=0, sticky="nsew")

        self.sevenButton = Button(self, font=("Helvetica", 12), text="7", borderwidth=1,
                                command=lambda: self.addToDisplay("7"))
        self.sevenButton.grid(row=5, column=1, sticky="nsew")

        self.eightButton = Button(self, font=("Helvetica", 12), text="8", borderwidth=1,
                                command=lambda: self.addToDisplay("8"))
        self.eightButton.grid(row=5, column=2, sticky="nsew")

        self.nineButton = Button(self, font=("Helvetica", 12), text="9", borderwidth=1,
                                command=lambda: self.addToDisplay("9"))
        self.nineButton.grid(row=5, column=3, sticky="nsew")

        self.multButton = Button(self, font=("Helvetica", 12), text="*", borderwidth=1,
                               command=lambda: self.addToDisplay("*"))
        self.multButton.grid(row=5, column=4, sticky="nsew")

        # Fifth row of buttons
        self.factButton = Button(self, font=("Helvetica", 12), text="!", borderwidth=1,
                                command=lambda: self.addToDisplay("factorial("))
        self.factButton.grid(row=6, column=0, sticky="nsew")

        self.fourButton = Button(self, font=("Helvetica", 12), text="4", borderwidth=1,
                                command=lambda: self.addToDisplay("4"))
        self.fourButton.grid(row=6, column=1, sticky="nsew")

        self.fiveButton = Button(self, font=("Helvetica", 12), text="5", borderwidth=1,
                                command=lambda: self.addToDisplay("5"))
        self.fiveButton.grid(row=6, column=2, sticky="nsew")

        self.sixButton = Button(self, font=("Helvetica", 12), text="6", borderwidth=1,
                                command=lambda: self.addToDisplay("6"))
        self.sixButton.grid(row=6, column=3, sticky="nsew")

        self.minusButton = Button(self, font=("Helvetica", 12), text="-", borderwidth=1,
                               command=lambda: self.addToDisplay("-"))
        self.minusButton.grid(row=6, column=4, sticky="nsew")

        # Sixth row of buttons
        # NEG TOGGLE BUTTON STILL NEEDS IMPLEMENTATION
        self.negToggleButton = Button(self, font=("Helvetica", 12), text="+-", borderwidth=1,
                                command=lambda: self.negToggle())
        self.negToggleButton.grid(row=7, column=0, sticky="nsew")

        self.oneButton = Button(self, font=("Helvetica", 12), text="1", borderwidth=1,
                                command=lambda: self.addToDisplay("1"))
        self.oneButton.grid(row=7, column=1, sticky="nsew")

        self.twoButton = Button(self, font=("Helvetica", 12), text="2", borderwidth=1,
                                command=lambda: self.addToDisplay("2"))
        self.twoButton.grid(row=7, column=2, sticky="nsew")

        self.threeButton = Button(self, font=("Helvetica", 12), text="3", borderwidth=1,
                                command=lambda: self.addToDisplay("3"))
        self.threeButton.grid(row=7, column=3, sticky="nsew")

        self.plusButton = Button(self, font=("Helvetica", 12), text="+", borderwidth=1,
                               command=lambda: self.addToDisplay("+"))
        self.plusButton.grid(row=7, column=4, sticky="nsew")

        # Seventh row of buttons
        self.leftParenButton = Button(self, font=("Helvetica", 12), text="(", borderwidth=1,
                                command=lambda: self.addToDisplay("("))
        self.leftParenButton.grid(row=8, column=0, sticky="nsew")

        self.rightParenButton = Button(self, font=("Helvetica", 12), text=")", borderwidth=1,
                                command=lambda: self.addToDisplay(")"))
        self.rightParenButton.grid(row=8, column=1, sticky="nsew")

        self.zeroButton = Button(self, font=("Helvetica", 12), text="0", borderwidth=1,
                                command=lambda: self.addToDisplay("0"))
        self.zeroButton.grid(row=8, column=2, sticky="nsew")

        self.decimalButton = Button(self, font=("Helvetica", 12), text=".", borderwidth=1,
                                command=lambda: self.addToDisplay("."))
        self.decimalButton.grid(row=8, column=3, sticky="nsew")

        self.equalsButton = Button(self, font=("Helvetica", 12), text="=", borderwidth=1,
                               command=lambda: self.evalDisplay())
        self.equalsButton.grid(row=8, column=4, sticky="nsew")


calculator = Tk()
calculator.title("PyCalc")
calculator.resizable(False,False)

root = Pycalc(calculator).grid()
calculator.mainloop()
