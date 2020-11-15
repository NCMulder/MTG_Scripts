import argparse
import configparser

from TTS_MTG_deck_creator import create_tts_mtg_decks
from constants import CARD_SIZES
from overrides import cardname_identifier_overrides
from scryfall_tools import get_collection


def main(out, name, size):
    deck_array = [
        ({'name': cardname}, 1)
        for cardname in cardname_identifier_overrides.keys()
    ]

    decklist = get_collection(deck_array)

    create_tts_mtg_decks(
        {name: decklist},
        out,
        card_size_text=size
    )


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')

    parser = argparse.ArgumentParser(
        description='Create a TTS deck filled '
                    'with all the cards in overrides.py'
    )
    parser.add_argument(
        '-o', '--out',
        help='Absolute path of which directory to store the generated deck',
        default=config['Main'].get('default_output_path', ''),
        type=str
    )
    parser.add_argument(
        '-n', '--name',
        help='The name of the generated deck',
        default='[TEST] Overrides',
        type=str
    )
    parser.add_argument(
        '-s', '--size',
        help='Card image size',
        default='normal',
        choices=CARD_SIZES,
        type=str
    )

    args = parser.parse_args()

    main(out=args.out, name=args.name, size=args.size)
