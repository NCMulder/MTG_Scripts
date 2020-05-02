# Bundles some Scryfall related tools together
# to use in other scripts or from the command line

import requests

from overrides import cardname_identifier_overrides


def get_random_card(q=None, verbose=False):
    """Gets a random card from Scryfall.
    See https://scryfall.com/docs/api/cards/random
    """

    result = requests.get(
        f'https://api.scryfall.com/cards/random?{f"q={q}" if q else ""}'
    ).json()
    if result['object'] == 'card':
        if verbose:
            print('Found', result['name'])
        return result
    if result['object'] == 'error':
        print(result["details"])

    return None


def get_card(cardname, uri=None, fuzzy=False, verbose=False):
    """Get a card from Scryfall based on card name.
    See https://scryfall.com/docs/api/cards/named
    """

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
        print(result["details"])

    return None


def get_card_image(cardname='', version='large', uri=''):
    """Get a card image from Scryfall based on card name.
    See https://scryfall.com/docs/api/images
    """

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


def get_collection(decklist_dict):
    """Return a dictionary of identifiers for posting to Scryfall.
    See https://scryfall.com/docs/api/cards/collection
    """

    results = []
    base = {}
    identifiers = []
    for idx, (cardname, count) in enumerate(decklist_dict.items()):
        card_identifier = getattr(
            cardname_identifier_overrides,
            cardname,
            {'name': cardname}
        )

        for _ in range(count):
            identifiers.append(card_identifier)
            if (len(identifiers) + 1) % 75 == 0 \
                    or idx + 1 == len(decklist_dict):
                # Either the identifiers' list is getting too long
                # or we are at the end of the list. Post the data,
                # store the result and reset the data.
                base['identifiers'] = identifiers
                cards = requests.post(
                    'https://api.scryfall.com/cards/collection',
                    json=base
                ).json()
                results.append(cards)
                identifiers = []

    # Merge the results
    cards = [card for d in results for card in d['data']]
    return cards
