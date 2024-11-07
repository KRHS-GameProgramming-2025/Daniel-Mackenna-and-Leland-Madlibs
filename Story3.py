from Getters import *

def Story3(debug=True):
    if debug: print("Story3 Function")
    
    print("\n")
    friendname1 = getword ("Enter a name: ", debug)
    item1 = getword ("Enter a Item used for diging: ", debug)
    animal1 = getAnimal ("Enter a scary animal: ", debug)
    
    
    out = "\n"
    out += " one day me and my friend, " + friendname1
    out += " wanted to dig a hole to get to the other side of the earth s0 we grabed a, " + item1 + " from the shed as we grabed the, " + item1 + " a, " + animal1 + " appered out of nowhere, "
    out += " me and my friend ran because of the scary, " + animal1
    out += " after me and my friend calmed down we started diging, "
    out += " soon we hit a big rock so we had to get a new tool from the shed with the scary, " + animal1
    
    return out

