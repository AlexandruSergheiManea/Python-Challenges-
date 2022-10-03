print ("Think of a superhero out of IronMan ,Thor ,Batman ,Superman")
q1 = input ("Is your hero from marvel?")
if q1 == "yes":
    q2 = input ("Does your character have superpowers?")
    if q2 == "yes": print ("your character is thor")
    elif q2 == "no": print ("your character is IronMan")
elif q1 == "no":
    q3 = input ("Does your character have superpowers?")
    if q3 == "yes": print ("your character is Superman")
    elif q3 == "no": print ("your character is Batman")

