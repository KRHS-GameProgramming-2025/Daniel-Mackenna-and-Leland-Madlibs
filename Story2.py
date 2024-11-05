from Getters import *

def Story2(debug=False):
    if debug: print("Story1 Function")
    
    print("\n")
    friendname1 = getword ('Enter a name: ', debug)
    song1 = getsong ('Enter a song: ', debug)
    animal1 = getanimal1('Enter a animal: ', debug)
    action = getaction1("Enter a action word", dubug)
    
    
    
    out = "\n"
    out += "one day me and my friend " + friendname1
    out += "were listening to a song called " + song1
    out += " and while we where listening to " + song1 
    out += " suddenly " +  animal1
    out += " jumped out of no where "
    out += "then we decided to " + action
    
    return out
