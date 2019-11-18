## pwp
import sys

with open(sys.argv[1]) as file:
    points = 0
    joker = 0
    prereleases = 0
    GP = 0
    other = 0
    draft = 0
    storage = dict()
    storage["prereleases"] = dict()
    storage["joker"] = dict()
    storage["GP"] = dict()
    storage["other"] = dict()
    for line in file:
        pieces = line.split('|')
        points += int(pieces[2][8:])
        if "Prerelease" in pieces[1]:
            prereleases += int(pieces[2][8:])
        elif "Joker" in pieces[1]:
            joker += int(pieces[2][8:])
            if "Tournament" in pieces[1]:
                draft+= int(pieces[2][8:])
        elif "Grand Prix" in pieces[1]:
            GP += int(pieces[2][8:])
        else:
            other += int(pieces[2][8:])
    print("Prereleases: ", prereleases)
    print("The Joker: ", joker)
    print("GP's: ", GP)
    print("Other: ", other)
    print("Draft: ", draft)
    print("Total: ", points)
