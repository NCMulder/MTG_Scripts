import TTS_MTG_deck_creator
import random_commander_deck as rcd
import limited_pools as lp
import scryfall_tools as st
import argparse
import os

modes = [
    'random_commander',
    'decklist',
    'sealed_pool',
    'draft_packs'
]


def main(mode, output_path, query='', size='normal', set_code='ISD'):
    decks = {}

    if mode == 'random_commander':
        decklist, deckname = rcd.create_random_commander_deck(
            verbose=True,
            q=query
        )
        if not decklist:
            return
        decks[deckname] = decklist
    elif mode == 'decklist':
        decklist_path = "C:\\Users\\niels\\Desktop\\(EDH) Teshar.txt"
        with open(decklist_path, mode='r') as decklist_file:
            # TODO: Make this its own file
            # Handle sideboards, sets
            deckname = os.path.splitext(os.path.basename(decklist_path))[0]
            decklist_array = decklist_file.readlines()
            deck_dict = {' '.join(entry.split(' ')[1:]).strip():
                         int(entry.split(' ')[0])
                         for entry in decklist_array if entry.strip()}
            decklist = st.get_collection(deck_dict)
            decks[deckname] = decklist

    elif mode == 'sealed_pool':
        decks = lp.get_sealed_pool(set_code=set_code)

    TTS_MTG_deck_creator.create_TTS_MTG_decks(
        decks,
        output_path,
        card_size_text=size
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Create the TTS files for an M:TG deck."
    )
    parser.add_argument(
        '-mode',
        help='The mode to use for the program',
        default='random_commander',
        choices=modes,
        type=str
    )
    parser.add_argument(
        'query',
        help='Additional query parameters for selecting a random commander',
        nargs='?',
        default='',
        type=str
    )
    parser.add_argument(
        '-out',
        help='Where to store the generated files',
        default='',
        type=str
    )
    parser.add_argument(
        '-q',
        help='Card image size',
        default='normal',
        choices=st.card_sizes,
        type=str
    )

    args = parser.parse_args()

    main(mode=args.mode, output_path=args.out, query=args.query, size=args.q)
