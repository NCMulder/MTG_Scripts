"""Creates the files needed for a Magic: The Gathering deck
used in TableTop Simulator
 """

import itertools
import json
import random
import time
from datetime import datetime
from io import BytesIO
from pathlib import Path

from PIL import Image

import scryfall_tools
from constants import CARD_SIZES
from dropbox_uploader import upload_to_dropbox

# Card-back and ad cards taken from https://deckmaster.info.
# Backed up to Dropbox for persistence and to avoid loading issues
back_1_url = "https://www.dropbox.com/s/9aecuelfwga8bv4/back_1.jpg?dl=1"
back_2_url = "https://www.dropbox.com/s/ral1ldk9odsycqd/back_2.jpg?dl=1"

token_cardbacks = [
    'https://www.dropbox.com/s/jbnpcn4xs14myot/token_1.jpg?dl=1',
    'https://www.dropbox.com/s/7lvnf1z6paj6ds9/token_2.jpg?dl=1',
    'https://www.dropbox.com/s/pb4um3zm56i2nuj/token_3.jpg?dl=1',
    'https://www.dropbox.com/s/xx14lh7qty4x9a2/token_4.jpg?dl=1',
    'https://www.dropbox.com/s/p512mi23b3ptb4h/token_5.jpg?dl=1',
    'https://www.dropbox.com/s/w0ro7596gp5kk05/token_6.jpg?dl=1',
    'https://www.dropbox.com/s/dobryp84n34tjha/token_7.jpg?dl=1',
    'https://www.dropbox.com/s/a5sahr1jmuk51h8/token_8.jpg?dl=1',
    'https://www.dropbox.com/s/ss0pch8fdnv3f5i/token_9.jpg?dl=1',
    'https://www.dropbox.com/s/tw03iokf84smj74/token_10.jpg?dl=1',
    'https://www.dropbox.com/s/xk4bo87zp4aoq59/token_11.jpg?dl=1',
    'https://www.dropbox.com/s/ckvcduv45ha9e3x/token_12.jpg?dl=1',
    'https://www.dropbox.com/s/psfebladd3ta9lw/cardback_hearthstone.png?dl=1',
    'https://www.dropbox.com/s/4jy042wqgzwwmrx/cardback_lor_order.png?dl=1',
    'https://www.dropbox.com/s/9gzsugzq29qfqfq/cardback_lor_chaos.png?dl=1',
    'https://www.dropbox.com/s/x21iqrbaxlub9nw/cardback_pokemon.jpg?dl=1',
    'https://www.dropbox.com/s/9aguj8yuld44ofe/cardback_yugioh.jpg?dl=1'
]


def get_contained_object(nickname, card_id):
    transform = {
        'posX': 0.0, 'posY': 0.0, 'posZ': 0.0,
        'rotX': 0.0, 'rotY': 180, 'rotZ': 180,
        'scaleX': 1, 'scaleY': 1, 'scaleZ': 1
    }

    return {
        'Name': 'Card',
        'Transform': transform,
        'Nickname': nickname,
        'CardID': card_id
    }


sf_unique_cards = {}
sf_card_ids = {}

df_unique_cards = {}
df_card_ids = {}


def collect_ids(deck):
    deck_as_ids = {}

    for card in deck:
        if card['layout'] in ('transform', 'double_faced_token', 'modal_dfc'):
            if card['id'] not in df_card_ids:
                card_id = (
                        int(len(df_card_ids) / 24) * 100
                        + len(df_card_ids) % 24 + 100
                )
                df_card_ids[card['id']] = card_id
                df_unique_cards[card_id] = card
            else:
                card_id = df_card_ids[card['id']]
        else:
            if card['id'] not in sf_card_ids:
                card_id = (
                        int(len(sf_card_ids) / 24) * 100
                        + len(sf_card_ids) % 24 + 100
                )
                sf_card_ids[card['id']] = card_id
                sf_unique_cards[card_id] = card
            else:
                card_id = sf_card_ids[card['id']]

        if card_id not in deck_as_ids:
            deck_as_ids[card_id] = 1
        else:
            deck_as_ids[card_id] += 1

    return deck_as_ids


def transform_decks(decks):
    tokens = {}
    dfcs = []

    for deck in decks:
        deck_tokens = {}
        deck_dfcs = []
        for card in deck:
            # Add related parts to the tokens deck.
            if 'all_parts' in card:
                for related_entry in card['all_parts']:
                    if (
                            related_entry['component'] == 'token' or
                            related_entry['component'] == 'meld_result' or
                            related_entry['component'] == 'combo_piece' and
                            (
                                    'Emblem' in related_entry['name'] or
                                    'Monarch' in related_entry['name']
                            )
                    ):
                        related_card = scryfall_tools.get_card(
                            '', uri=related_entry['uri']
                        )
                        deck_tokens[related_card['oracle_id']] = related_card

            # Add double-faced cards to the DFCs deck.
            if card['layout'] in ('transform', 'modal_dfc'):
                deck_dfcs.append(card)

        for card in deck_dfcs:
            deck.remove(card)

        tokens = {**tokens, **deck_tokens}
        dfcs.append(deck_dfcs)

    main_decks_as_ids = [collect_ids(deck) for deck in decks]
    token_decks_as_ids = [collect_ids(tokens.values())]
    dfc_decks_as_ids = [collect_ids(deck) for deck in dfcs]

    return main_decks_as_ids, token_decks_as_ids, dfc_decks_as_ids


def create_deck_image_containers(card_size):
    # The initial images for the deck
    sf_images = []
    image_pages = int((len(sf_card_ids)) / 24)
    image_rest = len(sf_card_ids) % 24
    for _ in range(image_pages):
        sf_images.append((Image.new('RGB', [i * 5 for i in card_size])))
    if image_rest > 0:
        rows = int(image_rest / 5) + 1
        sf_images.append(
            Image.new('RGB', [card_size[0] * 5, card_size[1] * rows])
        )

    # Pages for DFCs
    dfc_images = []
    dfc_pages = int(len(df_card_ids) / 24)
    dfc_rest = len(df_card_ids) % 24
    # Add separate pages for both the front and the back images.
    for _ in range(dfc_pages):
        dfc_images.append(Image.new('RGB', [i * 5 for i in card_size]))
        dfc_images.append(Image.new('RGB', [i * 5 for i in card_size]))

    # Add separate pages for both the front and the back images.
    if dfc_rest > 0:
        rows = int(dfc_rest / 5) + 1
        dfc_images.append(
            Image.new('RGB', [card_size[0] * 5, card_size[1] * rows])
        )
        dfc_images.append(
            Image.new('RGB', [card_size[0] * 5, card_size[1] * rows])
        )

    return sf_images, dfc_images


def create_deck_images(card_size_text, log_card_names=True):
    print('Creating deck images...', flush=True)
    card_size = CARD_SIZES[card_size_text]
    sf_images, df_images = create_deck_image_containers(card_size)

    print('Handling single-faced cards')

    start = time.time()
    for card_id, card in sf_unique_cards.items():
        if log_card_names:
            print(
                f'Handling {card["name"] + " - " + str(card_id) + "...":<80}',
                end='\r',
                flush=True
            )

        image_page = int((card_id - 100) / 100)
        image_on_page = (card_id - 100 * (image_page + 1)) % 24
        image_box = (
            card_size[0] * (image_on_page % 5),
            card_size[1] * int(image_on_page / 5)
        )

        front_uri = card['image_uris'][card_size_text]

        # Make sure to leave 100 ms between Scryfall calls
        between = time.time() - start
        if between < 0.1:
            time.sleep(0.1 - between)
        start = time.time()
        card_image = scryfall_tools.get_card_image(uri=front_uri)
        sf_images[image_page].paste(
            Image.open(BytesIO(card_image)),
            box=image_box
        )

    if len(df_unique_cards) > 0:
        print('\n\nHandling double-faced cards')

        for card_id, card in df_unique_cards.items():
            if log_card_names:
                print(
                    f'Handling '
                    f'{card["name"] + " - " + str(card_id) + "...":<80}',
                    end='\r',
                    flush=True
                )

            image_page = int((card_id - 100) / 100)
            image_on_page = (card_id - 100 * (image_page + 1)) % 24
            image_box = (
                card_size[0] * (image_on_page % 5),
                card_size[1] * int(image_on_page / 5)
            )

            front_uri = ''
            back_uri = ''
            if card['layout'] == 'meld':
                front_uri = card['image_uris'][card_size_text]
                back_uri = card['image_uris'][card_size_text]
            if card['layout'] in ('transform', 'modal_dfc'):
                front_uri = card['card_faces'][0]['image_uris'][card_size_text]
                back_uri = card['card_faces'][1]['image_uris'][card_size_text]

            # Make sure to leave 100 ms between Scryfall calls
            # TODO: query multiple cards together
            between = time.time() - start
            if between < (0.1 * 2):
                time.sleep((0.1 * 2) - between)
            start = time.time()
            card_image_front = scryfall_tools.get_card_image(uri=front_uri)
            card_image_back = scryfall_tools.get_card_image(uri=back_uri)

            df_images[image_page * 2].paste(
                Image.open(BytesIO(card_image_front)),
                box=image_box
            )
            df_images[image_page * 2 + 1].paste(
                Image.open(BytesIO(card_image_back)),
                box=image_box
            )

    print('\n\nSaving images...', flush=True)
    sf_urls = save_deck_images(sf_images)
    df_urls = save_deck_images(df_images, start=len(sf_urls) + 1)
    print('', flush=True)

    return sf_urls, df_urls


def save_deck_images(images, start=1):
    urls = []
    for i, image in enumerate(images):
        print(f'Saving image {start + i}...', end='\r', flush=True)
        image_bytes = BytesIO()
        image.save(image_bytes, format='png')
        dropbox_url = upload_to_dropbox(
            image_bytes.getvalue(),
            f'TTS_{datetime.now():%Y-%m-%d-%H_%M_%S}.png'
        )
        if not dropbox_url:
            return []
        urls.append(dropbox_url)

    return urls


def create_deck_json_files(
        decks,
        sf_urls,
        df_urls,
        path,
        name,
        packs_per_player=3
):
    """
    Transform the decks iterable into a single JSON file containing
    the complete information TTS will need for a set of Custom Decks.
    Then save the JSON file.
    """

    # The base JSON container
    base = {
        'Date': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
        'ObjectStates': []
    }

    sf_pages = int((len(sf_card_ids)) / 24)
    remaining_rows = int((len(sf_card_ids) % 24) / 5) + 1

    back_url = random.choices([back_1_url, back_2_url], [999, 1])[0]
    main_customdeck = {
        i + 1: {
            'NumWidth': 5,
            'NumHeight': 5 if i < sf_pages else remaining_rows,
            'FaceURL': url,
            'BackURL': back_url,
            'BackIsHidden': True
        } for i, url in enumerate(sf_urls)
        # Ignore the page if it contains only tokens;
        # Check if the first card on the page is a token.
        if not sf_unique_cards[(i + 1) * 100]['layout'] == 'token'
    }

    token_customdeck = {
        i + 1: {
            'NumWidth': 5,
            'NumHeight': 5 if i < sf_pages else remaining_rows,
            'FaceURL': url,
            'BackURL': random.choice(token_cardbacks),
            'BackIsHidden': True
        } for i, url in enumerate(sf_urls)
        # Ignore the page if it doesn't contain tokens;
        # Check if the last card on the page is not a token.
        if sf_unique_cards[
               (i + 1) * 100 + (
                   23 if i < sf_pages
                   else (
                           (remaining_rows - 1) * 5
                           + (len(sf_card_ids) % 24) % 5 - 1
                   )
               )]['layout'] in ['token', 'emblem', 'meld']
    }

    df_pages = int((len(df_card_ids)) / 24) + 1
    remaining_rows = int((len(df_card_ids) % 24) / 5) + 1

    df_customdeck = {
        i + 1: {
            'NumWidth': 5,
            'NumHeight': 5 if i + 1 < df_pages else remaining_rows,
            'FaceURL': df_urls[i * 2],
            'BackURL': df_urls[i * 2 + 1],
            'BackIsHidden': True,
            'UniqueBack': True
        }
        for i in range(int(len(df_urls) / 2))
    }

    # Add the df-fronts to the main deck
    for i, df_url in enumerate(df_urls):
        # Skip the back faces
        if not i % 2 == 0:
            continue

        main_customdeck[len(main_customdeck) + 1] = {
            'NumWidth': 5,
            'NumHeight': 5 if i + 1 < df_pages else remaining_rows,
            'FaceURL': df_url,
            'BackURL': back_url,
            'BackIsHidden': True
        }

    for i, (deck_name, deck, tokens, dfcs) in enumerate(decks):
        # The main deck
        if deck:
            deck_container = {
                'Name': 'DeckCustom',
                'Transform': {
                    'posX': (i % packs_per_player) * 3.0,
                    'posY': 0.0,
                    'posZ': int(i / packs_per_player) * -4.0,
                    'rotX': 0, 'rotY': 180, 'rotZ': 180,
                    'scaleX': 1, 'scaleY': 1, 'scaleZ': 1
                },
                'Nickname': f'{deck_name}',
                'CustomDeck': main_customdeck,
                'ContainedObjects': [
                    get_contained_object(
                        sf_unique_cards[card_id]['name'], card_id
                    )
                    for card_id, amount in deck.items()
                    for i in range(amount)
                ],
                'DeckIDs': [
                    card_id
                    for card_id, amount in deck.items()
                    for i in range(amount)
                ]
            }

            # DFC fronts, IDs are offset by the number of SFC pages
            df_offset = 100 * (1 + int(len(sf_unique_cards) / 24))

            deck_container['ContainedObjects'] += [
                get_contained_object(
                    df_unique_cards[card_id]['name'],
                    card_id + df_offset
                )
                for card_id, amount in dfcs.items()
                for i in range(amount)
            ]
            deck_container['DeckIDs'] += [
                card_id + df_offset
                for card_id, amount in dfcs.items()
                for i in range(amount)
            ]

            base['ObjectStates'].append(deck_container)

        # The token container
        if tokens:
            token_deck = {
                'Name': 'DeckCustom',
                'Transform': {
                    'posX': i * 3, 'posY': 0.0, 'posZ': 4.0,
                    'rotX': 0, 'rotY': 180, 'rotZ': 180,
                    'scaleX': 1, 'scaleY': 1, 'scaleZ': 1
                },
                'Nickname': f'{deck_name} [tokens]',
                'CustomDeck': token_customdeck,
                'ContainedObjects': [
                    get_contained_object(
                        sf_unique_cards[card_id]['name'], card_id
                    )
                    for card_id, amount in tokens.items() for i in
                    range(amount)
                ],
                'DeckIDs': [
                    card_id
                    for card_id, amount in tokens.items()
                    for i in range(amount)
                ]
            }
            base['ObjectStates'].append(token_deck)

        # The DFC container
        if dfcs:
            dfc_transform = {
                'posX': i * 3, 'posY': 0.0, 'posZ': 8.0,
                'rotX': 0, 'rotY': 180, 'rotZ': 0,
                'scaleX': 1, 'scaleY': 1, 'scaleZ': 1
            }
            if len(dfcs) == 1:
                dfc = list(dfcs.keys())[0]
                dfc_deck = {
                    'Name': 'Card',
                    'Transform': dfc_transform,
                    'Nickname': df_unique_cards[dfc]['name'],
                    'CustomDeck': df_customdeck,
                    'CardID': dfc
                }
            else:
                dfc_deck = {
                    'Name': 'DeckCustom',
                    'Transform': dfc_transform,
                    'Nickname': f'{deck_name} [dfc]',
                    'CustomDeck': df_customdeck,
                    'ContainedObjects': [
                        get_contained_object(
                            df_unique_cards[card_id]['name'],
                            card_id
                        )
                        for card_id, amount in dfcs.items()
                        for _ in range(amount)
                    ],
                    'DeckIDs': [
                        card_id
                        for card_id, amount in dfcs.items()
                        for _ in range(amount)
                    ]
                }

            base['ObjectStates'].append(dfc_deck)

    json_path = Path(path or Path().absolute(), f'{name}.json')
    with open(json_path, 'w') as outfile:
        json.dump(base, outfile, indent=2, ensure_ascii=False)


def create_tts_mtg_decks(
        decks,
        path='',
        card_size_text='normal',
        name=None,
        packs_per_player=3,
        log_card_names=True
):
    print(
        f'{datetime.now().strftime("%H:%M:%S")} - Gathering unique cards...',
        flush=True
    )
    mains_as_ids, tokens_as_ids, dfcs_as_ids = transform_decks(decks.values())

    sf_urls, df_urls = create_deck_images(card_size_text, log_card_names)

    if not sf_urls and not df_urls:
        print('Something went wrong with uploading the deck images.')
        return

    print('Creating deck JSON files', flush=True)
    create_deck_json_files(
        itertools.zip_longest(
            [deck for deck in decks],
            mains_as_ids,
            tokens_as_ids,
            dfcs_as_ids,
            fillvalue=[]
        ),
        sf_urls,
        df_urls,
        path,
        name if name else list(decks.keys())[0],
        packs_per_player
    )

    print(
        f'{datetime.now().strftime("%H:%M:%S")} - Done!',
        flush=True
    )
