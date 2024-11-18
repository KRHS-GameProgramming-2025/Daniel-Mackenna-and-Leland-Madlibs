def getMenuoption(debug = False):
    if debug: print("getMenuoption Function")

    goodinput = False
    
    while not goodinput:
        option = input("please select an option: ")
        option= option.lower()

        if (option == "q" or
           option == "quit" or
           option == "x" or
           option == "exit"):
               option = "q"
               goodinput = True
                
        elif (option == "1" or
           option == "one" or
           option == "story1" or
           option == "story 1"):
               option = "1"
               goodinput = True
               
        elif (option == "2" or
           option == "two" or
           option == "story2" or
           option == "story 2"):
               option = "2"
               goodinput = True
               
        elif (option == "3" or
           option == "three" or
           option == "story3" or
           option == "story 3"):
               option = "3"
               goodinput = True
               
        elif (option == "4" or
           option == "four" or
           option == "story4" or
           option == "story 4"):
               option = "4"
            
               goodinput = True
        elif (option == "5" or
           option == "five" or
           option == "story5" or
           option == "story 5"):
               option = "5"
               goodinput = True
               
        elif (option == "31058"):
               goodinput = True
               
        else:
            print("Please make a valid choice")
        
    return option


def getword(prompt, debug = False):
    if debug: print("getMenuoption Function")

    goodinput = False
    
    while not goodinput:
        word = input(prompt)
        goodinput = True
        if isSwear(word, debug) :
            goodinput = False
            print ("dont use language like that")

    return word

def getSport(prompt, debug = False):
    if debug: print("getSport Function")

    goodinput = False
    
    sports = ["soccer",
              "football",
              "hockey",
              "wrestling"]
    
    while not goodinput:
        word = input(prompt)
        goodinput = True
        if isSwear(word, debug) :
            goodinput = False
            print ("dont use language like that")
        elif word.lower() not in sports:
            goodinput = False
            print ("sorry i dont know that one")
            
            
    return word
    

    
def getAnimal(prompt, debug = False):
    if debug: print("getAnimal Function")

    goodinput = False
    
 
    while not goodinput:
        word = input(prompt)
        goodinput = True
        if isSwear(word, debug) :
            goodinput = False
            print ("dont use language like that")
    
    return word



def getBug(prompt, debug = False):
    if debug: print("getBug Function")

    goodinput = False
    
 
    while not goodinput:
        word = input(prompt)
        goodinput = True
        if isSwear(word, debug) :
            goodinput = False
            print ("dont use language like that")
    
    return word


def getNumber(prompt, debug = False):
    if debug: print("getNumber Function")

    goodinput = False
    
    while not goodinput:
        word = input(prompt)
        if isSwear(word, debug) :
            goodinput = False
            
            print ("dont use language like that")
        try:
            float(word)
            goodinput = True
        except:
            print("must be a number")

    return word

def getED(prompt, debug = False):
    if debug: print("getRelative Function")

    goodinput = False
    
    while not goodinput:
        word = input(prompt)
        if isSwear(word, debug) :
            goodinput = False
            print ("dont use language like that")
        elif word.strip().lower()[-2:]=="ed":
            goodinput = True
        else:
            print("The word must end in ed")

    return word

def getING(prompt, debug = False):
    if debug: print("getRelative Function")

    goodinput = False
    
    while not goodinput:
        word = input(prompt)
        if isSwear(word, debug) :
            goodinput = False
            print ("dont use language like that")
        elif word.strip().lower()[-3:]=="ing":
            goodinput = True
        else:
            print("The word must end in ing")

    return word
    


def getAnswer(prompt, debug = False):
    if debug: print("getAnswer Function")
    

    goodinput = False
    
    answer = ["play",
               "do not play",
               "dont play",
               "not to play"]
    
    while not goodinput:
        word = input(prompt)
        goodinput = True
        if isSwear(word, debug) :
            goodinput = False
            print ("dont use language like that")

    return word
    
def getItem(prompt, debug = False):
    if debug: print("getItem Function")
    

    goodinput = False
    
    answer = ["hardware",
               "metal",
               "tools",
               "wood"]
    
    while not goodinput:
        word = input(prompt)
        goodinput = True
        if isSwear(word, debug) :
            goodinput = False
            print ("dont use language like that")

    return word

    
    
    
    
def isSwear (word, debug = False):
    if debug: print("isSwear Function")
    if word.lower() in swearlist:
        return True
    else:
        return False
    
swearlist = ["poop", "pee", "shit", "fuck", "motherfucker", "cunt", "pussy", "dick", "cock", "ass", "nigger", "god damit", "damit", "heil hitler", "sucks", "bitch", "asshole", "penis", "slut", "whore", "how many jews can you fit in a voltswagon", "bullshit", "cocksucker", "damn", "fucker", "fucking", "hell", "holy shit", "horseshit", "piss", "prick", "son of a bitch", "son of a whore", "crap", "goddam", "dumbass", "dickhead", "faggot", "bastard", "bloody hell"
]




