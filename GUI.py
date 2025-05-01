######################################################################
# Author: Jairus Harrison, Aaron Whitaker
# Username: Harrisonj2, whitakera2
#
# Assignment: p01-final-project
#

######################################################################
# Acknowledgements:
#
####################################################################################
import tkinter as tk
from game import Game #game is called from this file

class MyTkinterApp:
    def __init__(self, windowtext="Exploring Tkinter"):
        """
        The initializer creates a window to contain the widgets

        :param windowtext: The text at the top of the window title
        """
        self.root = tk.Tk()                         # Create the root window where all widgets go
        self.root.minsize(width=300, height=330)    # Sets the window's minimum size
        self.root.maxsize(width=300, height=330)    # Sets the window's maximum size
        self.root.title(windowtext)                 # Sets root window title

        self.myButton1 = None
        self.myButton2 = None
        self.myTextBox1 = tk.Entry(self.root)
        self.myTextLabel1Text = tk.StringVar()      # Makes a Tkinter string variable
        self.myTextLabel2Text = tk.StringVar()
        self.myTextLabel1 = None
        self.myTextLabel2 = None


    def create_button1(self, buttontext="Push"):
        """
        Creates a button with the given buttontext

        :param buttontext: The text on the button
        :return: None
        """
        self.myButton1 = tk.Button(self.root, text=buttontext, command=self.button1_handler)
        # Note that when myButton1 button is pushed, self.button1handler is called
        self.myButton1.pack()                       # pack means add to window

    def button1_handler(self):
        """
        Event handler for myButton1 above.
        Gets the text from the textbox and writes in myTextLabel1

        :return: None
        """
        txt = self.myTextBox1.get()                 # Retrieves the text entered by the user                             # increments each time the handler is called (button is pressed)
        message = ("\nHey,{0}!\n\nIn this game you lost your sheep in a cave.\n\nYour goal is to collect them and get"
                   " out.\n\nYou may find things that are out"
                   " to kill you.\n\nIf you see anything thats not a sheep it's best to run.\n\nUse the arrow keys to"
                   " move and Good luck!\n").format(txt)
        self.myTextLabel2Text.set(message)
        if self.myButton2 == None:
            self.create_button2("Start Game")

    def create_button2(self, buttontext="Push"):
        """
        Creates a button with the given buttontext

        :param buttontext: The text on the button
        :return: None
        """
        self.myButton2 = tk.Button(self.root, text=buttontext, command=self.button2_handler)
        # Note that when myButton1 button is pushed, self.button1handler is called
        self.myButton2.pack()                       # pack means add to window

    def button2_handler(self):
        """
        Event handler for myButton2 above.
        Starts game from game file
        :return: None
        """
        game = Game()
        game.run()

    def create_textbox1(self):
        """
        Creates a textbox into which the user can type

        :return: None
        """

        self.myTextBox1.pack()                      # pack means add to window


    def create_label1(self, labeltext=""):
        """
        Creates a label on the window and sets the label to labeltext

        :param labeltext: The text on the label
        :return: None
        """

        self.myTextLabel1Text.set(labeltext)        # Sets the Tkinter string variable
        self.myTextLabel1 = tk.Label(self.root, textvariable=self.myTextLabel1Text)
        self.myTextLabel1.pack()                    # pack means add to window
        message = "\nWhat is your name?"
        self.myTextLabel1Text.set(message)

    def create_label2(self, labeltext=""):
        """
        Creates a label on the window and sets the label to labeltext

        :param labeltext: The text on the label
        :return: None
        """

        self.myTextLabel2Text.set(labeltext)  # Sets the Tkinter string variable
        self.myTextLabel2 = tk.Label(self.root, textvariable=self.myTextLabel2Text)
        self.myTextLabel2.pack()  # pack means add to window
        # message2 = "hello"
        # self.myTextLabel2Text.set(message2)


def gui():
    """
    Creates GUI and uses button, textbox and label GUI widgets

    :return: None
    """

    myGUI = MyTkinterApp("CSC226 Hello GUI")           # Create a new myTkinter object
    myGUI.create_label1()  # Create a label to writing text into (empty for now)
    myGUI.create_textbox1()                         # Calls the create textbox method for capturing user input
    myGUI.create_button1("Begin")
    myGUI.create_label2()
    myGUI.root.mainloop()   # Needed to start the event loop

def main():
    gui()

if __name__ == "__main__":
    main()
