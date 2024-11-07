from Getters import *

def Story1(debug=False):
    if debug: print("Story1 Function")
    
    print("\n")
    friendname1 = getword ("Enter a name: ", debug)
    sport1 = getSport ("Enter a Sport: ", debug)
    animal1 = getAnimal ("Enter an Animal: ", debug)
    verb1 = getword ("Enter a past-tense Verb: ", debug)
    verb2 = getword ("Enter a Verb: ", debug)
    item1 = getword ("Enter a plural Item: ", debug)
    item2 = getword ("Enter a plural Item: ", debug)
    item3 = getword ("Enter a Item: ", debug)
    number1 = getNumber ("Enter a Number: ", debug)
    adj1 = getword ("Enter an Adjective: ", debug)
    verb3 = getED ("Enter a Verb ending in -ed: ", debug)
    relative1 = getword ("Enter a Relative: ", debug)
    occupation1 = getword ("Enter an Occupation: ", debug)
    verb4 = getED ("Enter a Verb ending in -ed: ", debug)
    place1 = getword ("Enter a Place: ", debug)
    verb5 = getword ("Enter a Verb: ", debug)
    if animal1.lower().strip() == "gigantopithecus":
        relative1 = "father, Ralph von Koenigswald"
        occupation1 = "paleoanthropologist"

    out = "\n"
    out += "one day me and my friend, " + friendname1
    out += " were out playing " + sport1
    out += " when we found a " + animal1
    out += ", we " + verb1 + " home to " + verb2 + " something to catch it."
    out += " we grabbed " + item1 + ", " + item2 + " and a " + item3 + "."
    out += " we " + verb1 + " back to where we saw the " + animal1
    out += ". we searched for it for " + number1 + " hours and found it again after it was " + adj1 + " out."
    out += "we used the " + item1 + " to lure the " + animal1 + " closer, then I grabbed the " + item2 + " and " + friendname1 + " grabbed the " + item3
    out += ". we " + verb3 + " the " + animal1 + " and were able to catch it."
    out += " we " + verb1 + " back home again with the " + animal1 + " and showed it to my " + relative1 + ", who is a " + occupation1
    out += ". they " + verb4 + " us and took the " + animal1 + " to the " + place1 + "."
    out += " after a while they " + verb5 + " back with the " + animal1 + " and claimed they fully trained it."
    
    return out
