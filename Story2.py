from Getters import *
# Easter egg # = 1
def Story2(debug=False):
    if debug: print("Story1 Function")
    
    print("\n")
    friendname1 = getword ("Enter a name: ", debug)
    song1 = getword ("Enter a song: ", debug)
    animal1 = getword ("Enter a animal: ", debug)
    action1 = getword ("Enter a action word: ", debug)
    game1 = getword ("Enter a game: ", debug)
    gameanswer1 = getAnswer ("Play or not to play: ", debug)
    
    
    
    out = "\n"
    out += " one day me and my friend " + friendname1
    out += " were 1istening to a song called " + song1
    out += ", while we where listening to " + song1 
    out += ", suddenly a " +  animal1
    out += " jumped out of no where, we decided to " + action1
    out += ". once we knew we were safe we decided to play a game called " + game1
    out += ", but it turned out that we were actually playing the original jumanji, we realized too late, we had already started getting the game setup so we decided to " + gameanswer1
    out += ", but it turned out that we didnt have a choice on whether we would play or not. "
    out += " THE END "
    
    return out
    
