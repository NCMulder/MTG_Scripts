import argparse
import configparser
import os
from datetime import date

from TTS_MTG_deck_creator import create_tts_mtg_decks
from constants import CARD_SIZES
from limited_pools import get_limited_pool
from random_commander_deck import create_random_commander_deck
from scryfall_tools import get_collection

modes = [
    'random_commander',
    'decklist',
    'sealed_pool',
    'draft_packs'
]


def decklist(args):
    # Handle sideboards, sets
    deck_name = os.path.splitext(os.path.basename(args.file.name))[0]
    decklist_array = args.file.readlines()

    # Flip decklist_array ['[amount] [cardname]']
    # to {[cardname]: [amount]}
    deck_dict = {
        ' '.join(entry.split(' ')[1:]).strip()
        : int(entry.split(' ')[0])
        for entry in decklist_array
        if entry.strip() and not entry.startswith('//')
    }

    create_tts_mtg_decks(
        decks={deck_name: get_collection(deck_dict)},
        path=args.out,
        card_size_text=args.size,
    )


def draft(args):
    create_tts_mtg_decks(
        decks=get_limited_pool(
            set_code=args.code,
            number_of_players=args.players,
            packs_per_player=args.packs
        ),
        path=args.out,
        card_size_text=args.size,
        name=f'Draft Pool {args.code.upper()} ({date.today()})',
        packs_per_player=args.packs,
        log_card_names=False
    )


def random_commander(args):
    deck_list, deck_name = create_random_commander_deck(
        verbose=args.verbose,
        query=' '.join(args.query),
        deck_name=args.name
    )
    if not deck_list:
        return

    create_tts_mtg_decks(
        decks={deck_name: deck_list},
        path=args.out,
        card_size_text=args.size,
    )


def sealed(args):
    create_tts_mtg_decks(
        decks=get_limited_pool(
            set_code=args.code,
            number_of_players=args.players,
            packs_per_player=args.packs
        ),
        path=args.out,
        card_size_text=args.size,
        name=f'Sealed Pool {args.code.upper()} ({date.today()})',
        packs_per_player=args.packs,
        log_card_names=False
    )


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')

    parser = argparse.ArgumentParser(
        description='Create the TTS files for an M:TG deck.'
    )
    parser.add_argument(
        '-v', '--verbose',
        help='Display additional information',
        action='store_true'
    )

    subparsers = parser.add_subparsers(
        dest='mode',
        description='Available modes',
        metavar='mode',
        required=True
    )

    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument(
        '-o', '--out',
        help='Absolute path of the directory '
             'in which to store the generated deck',
        default=config['Main'].get('default_output_path', ''),
        type=str
    )
    parent_parser.add_argument(
        '-s', '--size',
        help='Card image size',
        default='normal',
        choices=CARD_SIZES,
        type=str,
        metavar='SIZE'
    )

    # GIVEN DECKLIST
    parser_decklist = subparsers.add_parser(
        'decklist',
        help='Create a TTS deck for the provided decklist file',
        parents=[parent_parser]
    )
    parser_decklist.set_defaults(func=decklist)
    parser_decklist.add_argument(
        'file',
        help='Path to the decklist',
        type=argparse.FileType('r')
    )

    # DRAFT PACKS
    parser_draft = subparsers.add_parser(
        'draft',
        help='Create a TTS deck for a draft pool from the provided set',
        parents=[parent_parser]
    )
    parser_draft.set_defaults(func=draft)
    parser_draft.add_argument(
        'code',
        help='3 letter set code',
    )
    parser_draft.add_argument(
        '-pa', '--packs',
        help='number of packs per player (default: %(default)d)',
        default=3,
        type=int
    )
    parser_draft.add_argument(
        '-pl', '--players',
        help='number of players (default: %(default)d)',
        default=1,
        type=int
    )

    # RANDOM COMMANDER DECK
    parser_random_commander = subparsers.add_parser(
        'random_commander',
        help='Create a TTS deck for a random EDH commander',
        parents=[parent_parser]
    )
    parser_random_commander.set_defaults(func=random_commander)
    parser_random_commander.add_argument(
        'query',
        help='Additional query parameters for selecting the commander',
        default='',
        nargs='*'
    )
    parser_random_commander.add_argument(
        '-n', '--name',
        help='The name of the generated deck',
        default=''
    )

    # SEALED POOL
    parser_sealed = subparsers.add_parser(
        'sealed',
        help='Create a TTS deck for a sealed pool from the provided set',
        parents=[parent_parser]
    )
    parser_sealed.set_defaults(func=sealed)
    parser_sealed.add_argument(
        'code',
        help='3 letter set code'
    )
    parser_sealed.add_argument(
        '-pa', '--packs',
        help='number of packs per player (default: %(default)d)',
        default=6,
        type=int
    )
    parser_sealed.add_argument(
        '-pl', '--players',
        help='number of players (default: %(default)d)',
        default=1,
        type=int
    )

    # Parse the args and call whatever mode was selected
    args = parser.parse_args()
    args.func(args)
