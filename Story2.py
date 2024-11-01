from Getters import *

def Story2(debug=False):
    if debug: print("Story1 Function")
    
    print("\n")
    friendname1 = getword ('Enter a name: ', debug)
    song1 = getsong ('Enter a song: ', debug)
    
    
    out = "\n"
    out = 'one day me and my friend ' + friendname1
    out = 'were listening to a song called ' + song1
    out = 'and while we where listening to ' + song1 ' when suddenly'
    
    return out
