from Screens import *
from Getters import *
from Story1 import *
from Story2 import *


def Madlibs(debug = False):
    if debug: print("Welcome to debug")

    print(TitleScreen(debug))
    try:
        input("press enter to continue")
    except:
        pass

    done = False
    
    while not done:
        print(MainMenu(debug))
        choice = getMenuoption(debug)
        
        if choice == "q":
            exit();
        elif choice == "1":
            print (Story1())
            print ("\n")
            input("press enter to continue")
        elif choice == "2":
            print (Story2())
            print ("\n")
            input("press enter to continue")


Madlibs(False)
