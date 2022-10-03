print ("Think of a Dino out of T-rex, Megalodon ,Mosasaurus ,plesiosaurs, stegosaurus, Triceratops")
q1 = input ("Is your dinosaur a land or water dinosaur?")
if q1 == "yes":
    q2 = input ("Are they a carnivore??")
    if q2 == "yes": print ("your dino is T-rex")
    elif q2 == "no":
        q3 = input ("Does your dinosaur have horns??")
        if q3 == "yes": print ("your dino is Triceratops")
        elif q3 == "no": print ("your dino is stegosaurus")
if q1 == "no":
    q4 = input ("Are they a reptile??")
    if q4 == "no": print ("your dino is Megalodon")
    elif q4 == "yes":
        q5 = input ("Are your dinosaurs from the Triassic period too the Rhaetian Stage??")
        if q5 == "yes": print ("your dino is plesiosaurs")
        elif q5 == "no": print ("your dino is Mosasaurus")
