from Getters import *

def Story1(debug=False):
    if debug: print("Story1 Function")
    
    print("\n")
    friendname1 = getword ("Enter a name: ", debug)
    sport1 = getSport ("Enter a Sport: ", debug)
    animal1 = getAnimal ("Enter an Animal: ", debug)
    verb1 = getVerb ("Enter a past-tense Verb: ", debug)
    verb2 = getVerb ("Enter a Verb: ", debug)
    item1 = getItem ("Enter a plural Item: ", debug)
    item2 = getItem ("Enter a plural Item: ", debug)
    item3 = getItem ("Enter a Item: ", debug)
    number1 = getNumber ("Enter a Number: ", debug)
    adj1 = getAdjective ("Enter an Adjective: ", debug)
    verb3 = getVerb ("Enter a Verb ending in -ed: ", debug)
    relative1 = getRelative ("Enter a Relative: ", debug)
    occupation1 = getOccupation ("Enter an Occupation: ", debug)
    verb4 = getVerb ("Enter a Verb ending in -ed: ", debug)
    place1 = getPlace ("Enter a Place: ", debug)
    
    
    
    
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
    out += " we " + verb1 + " back home again with the " + animal1 + " and showed it to our " + relative1 + ", who is a " + occupation1
    out += ". they " + verb4 + " us and took the " + animal1 + " to the " + place1 + "."
    out += ""
    out += ""
    out += ""
    out += ""
    
   
