from Getters import *

def Secret_Story(debug=True):
    if debug: print("Secret_Story Function")
        
    print("\n")
    gender = getword (" pick either he or she ", debug)
    pronoun = getword (" if you pick He for gender type him if not type her ")
    choice1 = getword ("left or right: ", debug)
   
    
    out = "\n"
    if choice1 == "left":
        print(out)
        out += " How diD YoU gEt HeRE yOu ShoUlD lEaVe BefOrE iT's tO LaTe Oh nO ThEre aLrEadY HeRe YoU NeED To rUn "
        out += " hey there he is get him " 
        out += " hey where did " + gender + " go i don't know well i guess we lost " + pronoun
        out += " HeY iT's mE YoUR sAFe FoR NoW bUt YoU Do NEeD tO GeT OuT oF HeRe i CAn seE tHEm Go nOW "
        print(out)
        choice2 = getword ("left or right: ", debug)
        if choice2 == "left" or "right":
            out = " .it's a deadend. hey there " + gender + " is your not going to get out of here ever bring " + pronoun + " to the chamber "
            out += " put " + pronoun + " in the chamber "
            out += " charing at 10% "
            out += " charing at 20% "
            out += " charing at 30% "
            out += " charing at 40% "
            out += " charing at 50% "
            out += " charing at ERROR charching inturupted charge depleting "
            out += " charing at 45% quick get to the chamber befor they start it back up "
            out += " charing back online charing at 50% "
            out += " charing at 60% "
            out += " charing at 70% we need to get to the chamber now or we lose " + pronoun
            out += " quick shut it down charing at 8........ pry the chamber open "
            out += " .who are you. that dosen't matter all that matters is getting you out of here "
            out += " hey there they are get them "
            out += " there here we will hold them off well you get to the exit .thank you. "
            out += " ThE eND "
    elif choice1 == "right":
        print(out)
        out = " How diD YoU gEt HeRE yOu ShoUlD lEaVe BefOrE iT's tO LaTe Oh nO ThEre aLrEadY HeRe YoU NeED To rUn "
        out += " hey there he is get him " 
        out += " .it's a deadend. hey there " + gender + " is your not going to get out of here ever bring " + pronoun + " to the chamber "
        out += " put " + pronoun + " in the chamber "
        out += " statup sequence initialized "
        out += " charing at 10% "
        out += " charing at 20% "
        out += " charing at 30% "
        out += " charing at 40% "
        out += " charing at 50% "
        out += " charing at ERROR charching inturupted charge depleting "
        out += " charing at 45% quick get to the chamber befor they start it back up "
        out += " charing back online charing at 50% "
        out += " charing at 60% "
        out += " charing at 70% we need to get to the chamber now or we lose " + pronoun
        out += " quick shut it down charing at 8........ pry the chamber open "
        out += " .who are you. that dosen't matter all that matters is getting you out of here "
        out += " hey there they are get them "
        out += " there here we will hold them off well you get to the exit .thank you. "
        out += " ThE eND "
        

    
    return out
