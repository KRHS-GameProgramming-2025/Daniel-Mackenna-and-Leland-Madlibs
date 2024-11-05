from Getters import *

def Story3(debug=True):
    if debug: print("Story3 Function")
    
    print("\n")
    friendname1 = getword ("Enter a name: ", debug)
    
    
    out = "\n"
    out += "one day me and my friend, " + friendname1
    
    return out

