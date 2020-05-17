import argparse
import configparser
import os

from TTS_MTG_deck_creator import create_tts_mtg_decks
from constants import CARD_SIZES
from limited_pools import get_sealed_pool
from random_commander_deck import create_random_commander_deck
from scryfall_tools import get_collection

modes = [
    'random_commander',
    'decklist',
    'sealed_pool',
    'draft_packs'
]


def main(
        mode, output_path, size='normal',
        query='', set_code=None, decklist_path=None
):
    decks = {}

    if mode == 'random_commander':
        decklist, deckname = create_random_commander_deck(
            verbose=True,
            q=query
        )
        if not decklist:
            return
        decks[deckname] = decklist
    elif mode == 'decklist':
        if not decklist_path:
            raise TypeError('Please provide a decklist path')
        with open(decklist_path, mode='r') as decklist_file:
            # TODO: Make this its own file
            # Handle sideboards, sets
            deckname = os.path.splitext(os.path.basename(decklist_path))[0]
            decklist_array = decklist_file.readlines()
            # Flip decklist_array ['[amount] [cardname]']
            # to dict {[cardname]: [amount]}
            deck_dict = {
                ' '.join(entry.split(' ')[1:]).strip()
                : int(entry.split(' ')[0])
                for entry in decklist_array
                if entry.strip() and not entry.startswith('//')
            }
            decklist = get_collection(deck_dict)
            decks[deckname] = decklist

    elif mode == 'sealed_pool':
        decks = get_sealed_pool(set_code=set_code)

    create_tts_mtg_decks(
        decks,
        output_path,
        card_size_text=size
    )


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.ini')

    parser = argparse.ArgumentParser(
        description='Create the TTS files for an M:TG deck.'
    )
    parser.add_argument(
        '-m', '--mode',
        help='The mode to use for the program',
        default='random_commander',
        choices=modes,
        type=str
    )
    parser.add_argument(
        '-o', '--out',
        help='Absolute path of which directory to store the generated deck',
        default=config['Main'].get('default_output_path', ''),
        type=str
    )
    parser.add_argument(
        '-s', '--size',
        help='Card image size',
        default='normal',
        choices=CARD_SIZES,
        type=str
    )
    parser.add_argument(
        '-q', '--query',
        help='Additional query parameters for selecting a random commander',
        nargs='?',
        default='',
        type=str
    )
    parser.add_argument(
        '-dl', '--decklist',
        help='URL of the decklist to retrieve',
        type=str
    )
    parser.add_argument(
        '-set',
        help='Limited set',
        default='ISD',
        type=str
    )

    args = parser.parse_args()

    main(
        mode=args.mode, output_path=args.out, size=args.size,
        query=args.query, decklist_path=args.decklist, set_code=args.set
    )
