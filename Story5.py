from Getters import *
# Easter egg # = 8
def Story5(debug=False):
    if debug: print("Story5 Function")
    
    print("\n")
    shopitem1 = getItem("Enter a shop item", debug)
    time1 = getword("Enter a time", debug)
    hoursworked1 = getword("Enter an amout of hours worked", debug)
    didonbreak1 = getword("Enter something to do on a break", debug)
    hoursworked2 = getword("Enter an amout of hours worked after break", debug)
    
    
    
    
    out = "\n"
    out += " one day I decided to organize a shop so i decided to start with " + shopitem1
    out += " once we started organize the " + shopitem1
    out += " we put each different type of item into different 8ins and we started at " + time1
    out += " after we worked for " + hoursworked1
    out += " we decided to take a break and on that break we decided to " + didonbreak1
    out += " once we were done with our break we decided to continue working on organizing the " +shopitem1
    out += " once we were done organizing it turned out that " + hoursworked2
    out += " hours went by "
    
