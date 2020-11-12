# Parses Magic: The Gathering decklists for cards, counts and printings.
# Returns seperate lists for main deck and sideboard.
# List entries are tuples of card identifiers and count.

import os
import re
from scryfall_tools import get_collection

import sys

def parse_decklist(file):
    ## Get the main deck name
    deck_name = os.path.splitext(os.path.basename(file.name))[0]

    ## Start parsing the decklist
    line = file.readline()
    decks = {}
    deck = []
    sideboard = False
    while line:
        ## If the line is a comment, continue to the next line
        if line.startswith('//'):
            line = file.readline()
            continue

        ## The first empty line signifies the start of the sideboard
        ## Any empty line should be ignored
        if not line.strip():
            if not sideboard:
                decks[deck_name] = deck
                deck_name += ' (sideboard)'
                deck = []
                sideboard = True
            line = file.readline()
            continue

        ## Match many types of decklist entries
        regex = r'(\d*)x? ?([^\(\)\[\]\n]+)(?:[\(\[](.*)[\)\]] ?([0-z]*)(.*))?'
        ma = re.search(regex, line)
        count = int(ma.group(1)) if ma.group(1) else 1

        card_dict = {}
        ## If the set and collectors number are specified, use this information.
        if ma.group(4) and ma.group(3):
            card_dict['collector_number'] = ma.group(4)
        ## Otherwise, use the card name.
        else:
            card_dict['name'] = ma.group(2)
        ## In any case, if a set is specified, use this.
        if ma.group(3):
            card_dict['set'] = ma.group(3)

        deck.append((card_dict, count))
        line = file.readline()
    
    ## Add the final deck to the list
    decks[deck_name] = deck

    return decks

if __name__ == '__main__':
    decks = parse_decklist(open(sys.argv[1], mode='r'))
    print(decks)
