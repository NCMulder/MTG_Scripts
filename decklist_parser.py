# Parses Magic: The Gathering decklists for cards, counts and printings.
# Returns seperate lists for main deck and sideboard.
# List entries are tuples of card identifiers and count.

import re
import sys


def parse_decklist(deck_name, deck_list):
    # Start parsing the decklist
    decks = {}
    deck = []
    sideboard = False
    for line in deck_list.split('\n'):
        # If the line is a comment, continue to the next line
        if line.startswith('//'):
            continue

        # The first empty line signifies the start of the sideboard
        # Any empty line should be ignored
        if not line.strip():
            if not sideboard:
                decks[deck_name] = deck
                deck_name += ' (sideboard)'
                deck = []
                sideboard = True
            continue

        # Match many types of decklist entries
        regex = r'(\d{0,3})x?\b ?(.+?)(?:$| (?:[([](\w*)[)\]] ?(\w*).*))'
        ma = re.search(regex, line)
        count = int(ma.group(1)) if ma.group(1) else 1

        card_dict = {}
        # If the set and collectors number are specified, use this information.
        if ma.group(4) and ma.group(3):
            card_dict['collector_number'] = ma.group(4)
        # Otherwise, use the card name.
        else:
            # Fix DFC's
            card_name = ma.group(2).split('//')[0].strip()
            card_dict['name'] = card_name
        # In any case, if a set is specified, use this.
        if ma.group(3):
            card_dict['set'] = ma.group(3)

        deck.append((card_dict, count))

    # Add the final deck to the list
    decks[deck_name] = deck

    return decks


if __name__ == '__main__':
    decks = parse_decklist(open(sys.argv[1], mode='r'))
    print(decks)
