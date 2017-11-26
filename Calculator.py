from tkinter import *
import parser

######################Window Initialization############################
root = Tk()
root.title("Calculator")
root.resizable(0,0)
######################Window Initialization############################

################################Classes################################

class MainScreen:
    __root = None
    __position = 0

    def __init__(self, root):
       self.__root = root
       self.__createDisplay()
       self.__createButtons()

    def __createDisplay(self):
        self.display = Entry(self.__root)
        self.display.grid(row=1, columnspan=6, sticky=W + E, pady=3)

    def __createButtons(self):

        #Number buttons
        self.__createButton(2, 0, "1")
        self.__createButton(2, 1, "2")
        self.__createButton(2, 2, "3")
        self.__createButton(3, 0, "4")
        self.__createButton(3, 1, "5")
        self.__createButton(3, 2, "6")
        self.__createButton(4, 0, "7")
        self.__createButton(4, 1, "8")
        self.__createButton(4, 2, "9")
        self.__createButton(5, 1, "0")

        #Special buttons
        self.__createACButton(5, 0, "AC")
        self.__createCalculateButton(5, 2, "=")

        #Operations buttons
        self.__createButton(2, 4, "+")
        self.__createButton(3, 4, "-")
        self.__createButton(4, 4, "/")
        self.__createButton(5, 4, "*")

        #
        self.__createButton(2, 5, "(")
        self.__createButton(3, 5, ")")
        self.__createButton(4, 5, "%")
        self.__createButton(5, 5, "^2")

    def __setVabiables(self, num):

        if self.display.get() == "Error":
            self.__cleanCalculator()

        self.display.insert(self.__position, num)
        self.__position += 1

    def __cleanCalculator(self):
        self.display.delete(0, 'end')
        self.__position += 0

    def __calculate(self):
        expression = self.display.get()
        try:
            toEval = parser.expr(expression).compile()
            result = eval(toEval)
            self.__cleanCalculator()
            self.display.insert(0, result)
            self.__position = len(self.display.get()) + 1

        except Exception:
            self.__cleanCalculator()
            self.display.insert(0, "Error")

    def __createButton(self, row, column, text):
        return Button(self.__root, text=text, height = 1, width = 2, relief=GROOVE, command=lambda: self.__setVabiables(text)).grid(row=row, column=column, padx=3, pady=3)

    def __createACButton(self, row, column, text):
        return Button(self.__root, text=text, height = 1, width = 2, relief=GROOVE, command=lambda: self.__cleanCalculator()).grid(row=row, column=column, padx=3, pady=3)

    def __createCalculateButton(self, row, column, text):
        return Button(self.__root, text=text, height = 1, width = 2, relief=GROOVE, command=lambda: self.__calculate()).grid(row=row, column=column, padx=3, pady=3)

################################Classes###############################

main = MainScreen(root)
root.mainloop()
