import requests
import argparse
import sys
import re
import scryfall_tools
import TTS_MTG_deck_creator
try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup


def get_EDHREC_average_deck(commander):
    '''Get the average decklist for a commander from EDHREC
    Parses the deck page html for the given commander
    and returns the decklist as an array
    '''

    # Handle DFC's
    if 'card_faces' in commander:
        name = commander['card_faces'][0]['name']
    else:
        name = commander['name']
    url = f'https://edhrec.com/decks/{name}'.replace(' ', '-')
    random_deck_page = requests.get(url)
    parsed_html = BeautifulSoup(random_deck_page.text, features="html.parser")

    decklist_div = parsed_html.body.find('div', attrs={'class': 'well'})

    if not decklist_div:
        print('Could not find an average deck list for', commander['name'])
        return None

    decklist_raw = decklist_div.get_text(separator='\n').split('\n')
    pattern = re.compile(r'(\d*) (.*)$')
    decklist_filtered = {
        match.group(2): int(match.group(1))
        for match in (pattern.match(entry) for entry in decklist_raw) if match
    }

    if not sum(decklist_filtered.values()) == 100:
        print("The found decklist is incomplete")
        return None

    return decklist_filtered


def create_random_commander_deck(q='', verbose=False, deckname=''):
    '''Creates a random commander deck for use in TTS'''

    query = q
    if 'is:commander' not in query:
        query += '+' + 'is:commander'

    random_commander = scryfall_tools.get_random_card(q=query)
    if verbose:
        print(f'Building deck for commander: {random_commander["name"]}')

    deck_name = deckname or f'(EDH) {random_commander["name"].split(" //")[0]}'

    deck_dict = get_EDHREC_average_deck(random_commander)

    if not deck_dict:
        return None, ''

    decklist = scryfall_tools.get_collection(deck_dict)

    return decklist, deck_name

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Create the TTS files for a (random) commander."
    )
    parser.add_argument(
        'query',
        help='Additional query parameters for selecting the commander',
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
        choices=scryfall_tools.card_sizes,
        type=str
    )

    args = parser.parse_args()

    create_random_commander_deck(verbose=True, q=args.query)
