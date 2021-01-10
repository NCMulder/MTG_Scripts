# Bundles some Scryfall related tools together
# to use in other scripts or from the command line
import time

import requests

from overrides import cardname_identifier_overrides


def get_set_list(verbose=False):
    """Gets a random set from Scryfall.
    See https://scryfall.com/docs/api/sets/all
    """

    time.sleep(0.1)
    result = requests.get(
        f'https://api.scryfall.com/sets'
    ).json()

    if result['object'] == 'list':
        if verbose:
            print('Got the set list')
        return result
    if result['object'] == 'error':
        print(result['details'])

    return None


def get_random_card(q=None, verbose=False):
    """Gets a random card from Scryfall.
    See https://scryfall.com/docs/api/cards/random
    """

    time.sleep(0.1)
    result = requests.get(
        f'https://api.scryfall.com/cards/random?{f"q={q}" if q else ""}'
    ).json()

    if result['object'] == 'card':
        if verbose:
            print('Found', result['name'])
        return result
    if result['object'] == 'error':
        print(result['details'])

    return None


def get_card(cardname, uri=None, fuzzy=False, verbose=False):
    """Get a card from Scryfall based on card name.
    See https://scryfall.com/docs/api/cards/named
    """

    time.sleep(0.1)
    if uri:
        result = requests.get(uri).json()
    else:
        result = requests.get(
            'https://api.scryfall.com/cards/named?'
            f'{"fuzzy" if fuzzy else "exact"}={cardname}'
        ).json()

    if result['object'] == 'card':
        if verbose:
            print('Found', result['name'])
        return result

    if result['object'] == 'error':
        print(result['details'])

    return None


def get_card_image(cardname='', version='large', uri=''):
    """Get a card image from Scryfall based on card name.
    See https://scryfall.com/docs/api/images
    """

    time.sleep(0.1)
    if uri:
        result = requests.get(uri).content
    else:
        result = requests.get(
            'https://api.scryfall.com/cards/'
            f'named?exact={cardname}&format=image&version={version}'
        ).content

    return result


def search_for_cards(query):
    """Return a list of search results."""

    time.sleep(0.1)
    cards = requests.get(
        f'https://api.scryfall.com/cards/search?q={query}'
    ).json()

    if cards['object'] == 'error':
        return None
    else:
        stored = [cards['data']]
        while cards['has_more']:
            cards = requests.get(cards['next_page']).json()
            stored.append(cards['data'])
        return [card for lst in stored for card in lst]


def get_collection(decklist):
    """Return a dictionary of identifiers for posting to Scryfall.
    See https://scryfall.com/docs/api/cards/collection
    """

    results = []
    identifiers = []

    for idx, (identifier, count) in enumerate(decklist):
        if 'set' not in identifier.keys():
            card_identifier = cardname_identifier_overrides.get(
                identifier['name'],
                identifier
            )
        else:
            card_identifier = identifier

        for _ in range(count):
            identifiers.append(card_identifier)

            # If we reached the limit of Scryfall's collection lookup
            # or the end of the decklist:
            # Retrieve the cards and continue parsing lines.
            if len(identifiers) == 75 or idx + 1 == len(decklist):
                time.sleep(0.1)
                cards = requests.post(
                    'https://api.scryfall.com/cards/collection',
                    json={'identifiers': identifiers}
                )
                results.append(cards.json())
                identifiers = []

    # Merge the results
    cards = [card for d in results for card in d['data']]
    return cards
