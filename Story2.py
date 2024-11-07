from Getters import *

def Story2(debug=False):
    if debug: print("Story1 Function")
    
    print("\n")
    friendname1 = getword ("Enter a name: ", debug)
    song1 = getword ("Enter a song: ", debug)
    animal1 = getword ("Enter a animal: ", debug)
    action1 = getword ("Enter a action word: ", debug)
    action2 = getword ("Enter another action word: ", debug)
    
    
    
    out = "\n"
    out += "one day me and my friend " + friendname1
    out += "were 1istening to a song called " + song1
    out += " and while we where listening to " + song1 
    out += " when suddenly " +  animal1
    out += " jumped out of no where and then we decided to " + action1
    out += " once we knew we were safe we decided to " + action2
    out += " "
    
    return out
