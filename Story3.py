from Getters import *
# Easter egg # = 0
def Story3(debug=False):
    if debug: print("Story3 Function")
    
    print("\n")
    friendname1 = getword ("Enter a name: ", debug)
    item1 = getword ("Enter a Item used for digging: ", debug)
    animal1 = getAnimal ("Enter a scary animal: ", debug)
    item2 = getword ("Enter a Item used for mining: ", debug)
    food1 = getword ("Enter a food that you would have for dinner: ", debug)
    
    out = "\n"
    out += " one day me and my friend " + friendname1
    out += " wanted to dig a hole to get to the other side of the earth, s0 we grabed a " + item1 + " from the shed. As we grabed the " + item1 + " a " + animal1 + " appered out of nowhere. "
    out += "My friend and I ran because of the scary " + animal1
    out += ". After my friend and I calmed down we started digging. "
    out += " Soon we hit a big rock, so we had to get a new tool from the shed with the scary " + animal1
    out += ". We grabed a " + item2 + " from the shed and then got back to digging."
    out += " We had made it half way through the earth, but then we incountered the scary " + animal1
    out += ", so we dug as fast as possible and we popped out onto the other side of the earth. "
    out += "We then we had to go back because it was time for dinner. we had " + food1 + " and it was amazing"
    out += " THE END "
    
    return out

