print ("Think of a Game out of Call Of Duty Rainbow Six Siege ,GTA ,Mario, Super Smash Bros, Celest")
q1 = input ("Is your game a shooter")
if q1 == "yes":
    q2 = input ("Is your game first person?")
    if q2 == "no": print ("your game is GTA")
    elif q2 == "yes":
        q3 = input ("Is your game based on the Tom Clancy Books?")
        if q3 == "yes": print ("Your game is Call Of Duty")
        elif q3 == "no": print ("Your game is Rainbow Six Siege")
if q1 == "no":
    q4 = input ("Is your game a Nintendo exclusive?")
    if q4 == "no": print ("Your game is Celeste")
    elif q4 == "yes":
        q5 = input ("Is your game a platformer?")
        if q5 == "yes": print ("Your game is Mario")
        elif q5 == "no": print ("Your game is Super Smash Bros")


