from Getters import *
# Easter egg # = 5
def Story4(debug=False):
    if debug: print("Story4 Function")

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
    time1 = getword ("Enter a plural word used for measuring time: ", debug)
    smell1 = getword ("Enter something smelly: ", debug)
    adjective4 = getword ("Enter an adjective: ", debug)
    container1 = getword ("Enter a plural container: ", debug)


    out = "\n"
    out += "once I was " + verb1 + " through the woods,"
    out += " when I found an abandoned " + place1 + " and decided to check it out."
    out += " I " + verb2 + " up to it and looked inside."
    out += " It was very " + adjective1 + ", " + adjective2 + ", and just overall " + adjective3
    out += ". I decided it was a better idea to bring a friend, so I went back home. While i was " + verb2 + " home I felt like I was being followed and started " + verb2 + " faster."
    out += " When I finally arrived at my home I grabbed my " + item1 + " and then " + verb3 + " over to my buddies " + place2
    out += ". When I got to his " + place2 + " I greeted his " + relative1 + " at the door and asked if " + friendname1 + " was there. "
    out += "As I said it " + friendname1 + " poked his " + humanpart1 + " out the door and greeted me. "
    out += "I told him what I found and he " + verb4 + " back inside and grabbed a " + item2
    out += ". We then " + verb5 + " all the way back to the " + place1
    out += ". When we got there, we opened the door, walked around, and saw " + item3 + " and " + item4 + " 5tuck in the walls and all over the floor."
    out += " We " + verb6 + " around even more in hopes of finding something interesting, but all we found was broken " + item5 + " and " + item6 
    out += ". We then found a weirdly " + shape1 + " shape on one of the walls. I used the " + item1 + " that I brought to peel back the wallpaper which revealed a door. "
    out += "We slowly opened the door which revealed a descending staircase. we walked down for what seemed like " + time1
    out += ". When we finally reached the bottom we were hit with a smell almost like " + smell1
    out += ". We looked around for a bit but still found nothing of interest but " + adjective4 + " " + container1 + ". "
    out += "We decided it was all just a waste of time, so we " + verb5 + " back home and called it a day."

    return out
