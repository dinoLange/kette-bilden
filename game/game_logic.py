
from PIL import ImageTk, Image
from random import randrange


def push_roll_dice(gui):
    dices = get_random_dice_numbers()
    update_dices(dices, gui)
    dices = switch_dices(dices)

    count(dices, gui)


def get_random_dice_numbers():
    return randrange(1, 7), randrange(1, 7)


def update_dices(dices, gui):
    dice_list = {
        1: ImageTk.PhotoImage(Image.open("images/Alea_1.gif")),
        2: ImageTk.PhotoImage(Image.open("images/Alea_2.gif")),
        3: ImageTk.PhotoImage(Image.open("images/Alea_3.gif")),
        4: ImageTk.PhotoImage(Image.open("images/Alea_4.gif")),
        5: ImageTk.PhotoImage(Image.open("images/Alea_5.gif")),
        6: ImageTk.PhotoImage(Image.open("images/Alea_6.gif")),
    }
    gui.dice1_label.configure(image=dice_list[dices[0]])
    gui.dice1_label.img = dice_list[dices[0]]
    gui.dice2_label.configure(image=dice_list[dices[1]])
    gui.dice2_label.img = dice_list[dices[1]]


def switch_dices(dices):
    if dices[0] < dices[1]:
        return (dices[1], dices[0])
    else:
        return dices


def count(dice_pair, gui):
    if is_meier(dice_pair):
        gui.message_string.set("")
        gui.message_string.set("Meier! Alle trinken!!!")
        gui.global_counter += 1
        gui.last_pair=dice_pair

    elif is_better_pair(dice_pair, gui.last_pair):
        gui.last_pair=dice_pair
        if dice_pair[0] is dice_pair[1]:
            gui.global_counter += dice_pair[0]
        else:
            gui.global_counter += 1
    else:
        if gui.global_counter < 3:
            gui.message_string.set("Selber {} trinken!".format(gui.global_counter))
        else:
            gui.message_string.set("Du darfst {} verteilen!!!".format(gui.global_counter))

        gui.global_counter = 0
        gui.last_pair = (1, 3)

    gui.counter_string.set(gui.global_counter)


def is_meier(dice_pair):
    return dice_pair[0] is 2 and dice_pair[1] is 1


def is_better_pair(dice_pair, last_dice_pair):

    if last_dice_pair[0] is last_dice_pair[1]:
        if dice_pair[0] is dice_pair[1]:
            return dice_pair[0] > last_dice_pair[0]
        else:
            return False

    elif dice_pair[0] is dice_pair[1]:
        return True

    elif dice_pair[0] < last_dice_pair[0]:
        return False
    elif dice_pair[0] == last_dice_pair[0] and dice_pair[1] < last_dice_pair[1]:
        return False
    else:
        return True
