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

class MyTkinterApp:
    def __init__(self, windowtext="Exploring Tkinter"):
        """
        The initializer creates a window to contain the widgets

        :param windowtext: The text at the top of the window title
        """
        self.root = tk.Tk()                         # Create the root window where all widgets go
        self.root.minsize(width=250, height=250)    # Sets the window's minimum size
        self.root.maxsize(width=250, height=250)    # Sets the window's maximum size
        self.root.title(windowtext)                 # Sets root window title

        self.myButton1 = None
        self.myTextBox1 = tk.Entry(self.root)
        self.myTextLabel1Text = tk.StringVar()      # Makes a Tkinter string variable
        self.myTextLabel1 = None

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
        message = "Hey,{0} click it again!\nYou have clicked the button so many times.".format(txt)
        self.myTextLabel1Text.set(message)

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


def main():
    """
    Creates GUI and uses button, textbox and label GUI widgets

    :return: None
    """
    myGUI = MyTkinterApp("CSC226 Hello GUI")           # Create a new myTkinter object
    myGUI.create_button1("What is your name?")
    myGUI.create_textbox1()                         # Calls the create textbox method for capturing user input
    myGUI.create_label1()                           # Create a label to writing text into (empty for now)
    myGUI.root.mainloop()                           # Needed to start the event loop


if __name__ == "__main__":
    main()
