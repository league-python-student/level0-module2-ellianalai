import random
from tkinter import messagebox, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()





    # TODO 1) Use each value of random_number to give the user a random compliment
    for i in range(10):
        random_number = random.randint(1, 5)
        if random_number == 1:

            print("You are really nice")
        elif random_number == 2:
            print("You have a great personality")
        if random_number == 3:
            print("You are a bucket filler")
        if random_number == 4:
            print("You are a very caring person")
        if random_number == 5:
            print("You are a super funny person and I like it")
    # TODO 2) Repeat all the code above 10 times

    # TODO 3) Find someone to test out your program. They will like it :)
