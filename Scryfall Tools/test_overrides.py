import argparse
import configparser

from TTS_MTG_deck_creator import create_tts_mtg_decks
from constants import CARD_SIZES
from overrides import cardname_identifier_overrides
from scryfall_tools import get_collection, search_for_cards


def main(out, name, size, etched, lands, sld):
    deck_array = [
        ({'name': cardname}, 1)
        for cardname in cardname_identifier_overrides.keys()
    ]

    if etched:
        name += ' - Etched'
        control_array = [
            ({'name': card['name']}, 1)
            for card in search_for_cards('frame:etched')
        ]

    elif lands:
        name += ' - Lands'
        control_array = [
            ({'name': card['name']}, 1)
            for card in search_for_cards('t:basic order:color')
        ]
        control_array += [
            ({'name': card['name']}, 1)
            for card in search_for_cards('Pathway t:land')
        ]
        control_array += [
            ({'name': card['name']}, 1)
            for card in search_for_cards('Triome t:land')
        ]
        control_array += [
            ({'name': card['name']}, 1)
            for card in search_for_cards('s:zne order:set')
        ]
        # TODO: Add tests for these land types
        #  when overrides for them get added.
        # control_array += [
        #     ({'name': card['name']}, 1)
        #     for card in search_for_cards('is:checkland')
        # ]
        # control_array += [
        #     ({'name': card['name']}, 1)
        #     for card in search_for_cards('is:dual')
        # ]
        # control_array += [
        #     ({'name': card['name']}, 1)
        #     for card in search_for_cards('is:shockland')
        # ]

    elif sld:
        name += ' - SLD'
        control_array = [
            ({'name': card['name']}, 1)
            for card in search_for_cards('set:sld')
        ]

    else:
        control_array = []

    for control in control_array:
        if control not in deck_array:
            print(control[0])

    decklist = get_collection(control_array)

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
                    'to test overrides.py'
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

    parser.add_argument(
        '-e', '--etched',
        help='Test CMR Etched Foils specifically',
        action='store_true'
    )
    parser.add_argument(
        '-l', '--lands',
        help='Test Lands specifically',
        action='store_true'
    )
    parser.add_argument(
        '-sld',
        help='Test Secret Lair cards specifically',
        action='store_true'
    )

    args = parser.parse_args()

    main(
        out=args.out, name=args.name, size=args.size,
        etched=args.etched, lands=args.lands, sld=args.sld
    )
