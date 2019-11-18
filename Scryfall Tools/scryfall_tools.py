# Bundles some Scryfall related tools together
# to use in other scripts or from the command line

import requests

card_sizes = {
    "png": (745, 1040),
    "border_crop": (480, 680),
    "art_crop": (0, 0),
    "large": (672, 936),
    "normal": (488, 680),
    "small": (146, 204)
}


# Gets a random card from Scryfall
# See https://scryfall.com/docs/api/cards/random
def get_random_card(q=None, verbose=False):
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


# Gets a card from Scryfall based on card name
# See https://scryfall.com/docs/api/cards/named
def get_card(cardname, uri=None, fuzzy=False, verbose=False):
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


# Gets a card image from Scryfall based on card name
# See https://scryfall.com/docs/api/images
def get_card_image(cardname='', version='large', uri=''):
    if not uri:
        result = requests.get(
            'https://api.scryfall.com/cards/'
            f'named?exact={cardname}&format=image&version={version}'
        ).content
    else:
        result = requests.get(uri).content
    return result


# Return a list of search results
def search_for_cards(query):
    cards = requests.get(f'https://api.scryfall.com/cards/search?q={query}').json()

    if cards['object'] == 'error':
        return None
    else:
        return cards['data']


# Returns a dictionary of identifiers for posting to Scryfall
# See https://scryfall.com/docs/api/cards/collection
def get_collection(decklist_dict):
    results = []
    base = {}
    identifiers = []
    for idx, (cardname, count) in enumerate(decklist_dict.items()):
        card_identifier = {}
        card_identifier['name'] = cardname
        for _ in range(count):
            identifiers.append(card_identifier)
            if (idx + 1) % 75 is 0 or idx + 1 is len(decklist_dict):
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
