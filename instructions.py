def animal_action(animal, gen, value):

    prop = animal.properties


    if gen == 0:
        # ген, отвечающий за направление
        if value == 0:
            prop["pos"][0] += 1
        elif value == 1:
            prop["pos"][0] -= 1
        elif value == 2:
            prop["pos"][1] += 1
        elif value == 3:
            prop["pos"][1] -= 1
        else:
            prop["pos"][1] += 1