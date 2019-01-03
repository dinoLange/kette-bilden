from tkinter import *
from PIL import ImageTk, Image

from game_logic import push_roll_dice


class MyFirstGUI:
    def __init__(self, master):
        screen_width = 500
        screen_height = 400
        master.minsize(width=screen_width, height=screen_height)
        mainframe = Frame(master)
        mainframe.grid()

        self.global_counter = 0
        self.new_round = True
        init_img = ImageTk.PhotoImage(Image.open("images/Alea_1.gif"))
        self.last_pair = (1, 3)

        self.dice1_label = Label(mainframe)
        self.dice1_label.grid(row=0, column=0, sticky=N)

        self.dice1_label.configure(image=init_img)
        self.dice1_label.img = init_img

        self.dice2_label = Label(mainframe)
        self.dice2_label.grid(row=0, column=1, sticky=N)

        self.dice2_label.configure(image=init_img)
        self.dice2_label.img = init_img

        self.counter_description = Label(mainframe, text="Zähler: ")
        self.counter_description.grid(row=2, column=0)

        self.counter_string = StringVar()
        self.counter = Label(mainframe, textvariable=self.counter_string)
        self.counter.grid(row=2, column=1)
        self.counter_string.set("0")

        self.message_string = StringVar()
        self.message = Label(mainframe, textvariable=self.message_string)
        self.message.grid(row=3, column=0, columnspan=2)
        self.message_string.set("Start Game")

        self.button = Button(mainframe, text="Würfeln", width=25, command=self.push_button)
        self.button.grid(row=1, column=0, columnspan=2, sticky=W)

    def push_button(self):
        push_roll_dice(self)


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
