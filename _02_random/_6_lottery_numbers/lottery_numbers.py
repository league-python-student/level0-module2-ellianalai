import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    # TODO 1) Get 6 random numbers to put on your lottery ticket
    ticket = random.randint(1,100)
    ticket1 = random.randint(1,100)
    ticket2 = random.randint(1, 100)
    ticket3 = random.randint(1, 100)
    ticket4 = random.randint(1, 100)
    ticket5 = random.randint(1, 100)
    # TODO 2) Display the selected numbers to the user in a pop-up
    messagebox.showinfo(title = 'Lottery ticket', message = 'Your six random numbers are,' + str(ticket) + ' ' + str(ticket1)+ ' ' + str(ticket2)+' ' + str(ticket3)+' ' + str(ticket4)+' ' + str(ticket5))

    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
