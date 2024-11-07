from Getters import *

def Story4(debug=False):
    if debug: print("Story1 Function")
    
    print("\n")
    verb1 = getING ("Enter a verb ending in -ing: ", debug)
    place1 = getword ("Enter a place: ", debug)
    verb2 = getED ("Enter a verb ending in -ed: ", debug)
    adjective1 = getword ("Enter a adjective: ", debug)
    adjective2 = getword ("Enter a adjective: ", debug)
    adjective3 = getword ("Enter a adjective: ", debug)
    verb2 = getING ("Enter a verb ending in -ing: ", debug)
    item1 = getword ("Enter an item: ", debug)
    verb3 = getED ("Enter a verb ending in -ed: ", debug)
    place2 = getword ("Enter a place: ", debug)
    relative1 = getword ("Enter a relative: ", debug)
    friendname1 = getword ("Enter a name: ", debug)
    humanpart1 = getword ("Enter a human body part: ", debug)
    verb4 = getED ("Enter verb ending in -ed: ", debug)
    item2 = getword ("Enter an item: ", debug)
    verb5 = getED ("Enter a verb ending in -ed: ", debug)
    item3 = getword ("Enter a plural item: ", debug)
    item4 = getword ("Enter a plural item: ", debug)
    verb6 = getword ("Enter a verb ending in -ed: ", debug)
    item5 = getword ("Enter a plural valuable item: ", debug)
    item6 = getword ("Enter a plural valuable item: ", debug)
    shape1 = getword ("Enter a shape: ", debug)
    
    
    
    
    out = "\n"
    out += "once I was " + verb1 + " through the woods,"
    out += " when I found an abandoned " + place1 + " and decided to check it out."
    out += " I " + verb2 + " up to it and looked inside."
    out += " It was very " + adjective1 + ", " + adjective2 + ", and just overall " + adjective3
    out += ". I decided it was a better idea to bring a friend, so i went back home. while is was " + verb2 + " home i felt like i was being followed and started " + verb2 + " faster."
    out += " When i finally arrived at my home i grabbed my " + item1 + " and then " + verb3 + " over to my buddies " + place2
    out += ". When i got to his " + place2 + " i greeted his " + relative1 + " at the door and asked if " + friendname1 + " was there. "
    out += "as i said it " + friendname1 + " poked his " + humanpart1 + " out the door and greeted me. "
    out += "I told him what i found and he " + verb4 + " back inside and grabbed a " + item2
    out += ". We then " + verb5 + " all the way back to the " + place1
    out += ". when we got, there we opened the door, walked around, and saw " + item3 + " and " + item4 + " stuck in the walls and all over the floor."
    out += " we " + verb6 + " around even more in hopes of finding something interesting, but all we found was broken " + item5 + " and " + item6 
    out += ". we then found a weirdly " + shape1 + " shape on one of the walls. i used the " + item1 + " that i brought to peel back the wallpaper which revealed a door. "
    out += ""
    out += ""
    out += ""
    out += ""
    out += ""
    out += ""
    out += ""
    out += ""
    out += ""

    return out
