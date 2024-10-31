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
    
    
    
    
def isSwear (word, debug = False):
    if debug: print("isSwear Function")
    if word.lower() in swearlist:
        return True
    else:
        return False
    
swearlist = ["poop", "pee"
]




