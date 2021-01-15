import configparser
import re

import requests

from scryfall_tools import get_collection, get_random_card

try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup


def get_edhrec_average_deck(commander):
    """Get the average decklist for a commander from EDHREC
    Parses the deck page html for the given commander
    and returns the decklist as an array
    """

    # Handle DFC's
    if 'card_faces' in commander:
        name = commander['card_faces'][0]['name']
    else:
        name = commander['name']

    basic_name = re.sub(r'[^a-zA-Z\- ]', '', name)
    hyphen_name = re.sub(r' ', '-', basic_name).lower()
    url = f'https://edhrec-json.s3.amazonaws.com/en/average-decks/{hyphen_name}.json'

    random_deck_resp = requests.get(url)
    random_deck_json = random_deck_resp.json()
    print(random_deck_json)
    list_ugly = random_deck_json['description']
    list_cards = list_ugly.split('</a>')[2]

    decklist_raw = list_cards.split('\n')
    print(decklist_raw)
    pattern = re.compile(r'(\d*) (.*)$')
    decklist_filtered = [
        ({'name' : match.group(2)}, int(match.group(1)))
        for match in (pattern.match(entry) for entry in decklist_raw) if match
    ]

    if sum([count for card, count in decklist_filtered]) != 100:
        print('The found decklist is incomplete')
        return None

    return decklist_filtered


def create_random_commander_deck(query='', verbose=False, deck_name=''):
    """Creates a random commander deck for use in TTS"""

    if 'is:commander' not in query:
        query = f'({query}) AND is:commander'

    if verbose:
        print(f'Query: {query}')

    random_commander = get_random_card(q=query)

    print(f'Building deck for commander: {random_commander["name"]}')

    project_config = configparser.ConfigParser()
    project_config.read('config.ini')
    pf = project_config['Main'].get('deckname_prefix')
    deck_name = deck_name or f'{pf} {random_commander["name"].split(" //")[0]}'

    deck_array = get_edhrec_average_deck(random_commander)

    if not deck_array:
        return None, ''

    decklist = get_collection(deck_array)

    return decklist, deck_name
