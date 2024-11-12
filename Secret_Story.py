from Getters import *

def Secret_Story(debug=True):
    if debug: print("Secret_Story Function")
        
    print("\n")
    choice1 = getword ("left or right: ", debug)

    
    out = "\n"
    out += " How diD YoU gEt HeRE yOu ShoUlD lEaVe BefOrE iT's tO LaTe Oh nO ThEre aLrEadY HeRe YoU NeED To rUn "
    out += " hey there he is get him " 
    if choice1 == "left":
        out += " l "
    elif choice1 == "right":
        out += " that's a deadend you fool "
    

    
    return out
