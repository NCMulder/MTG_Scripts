import scryfall_tools as st
import random


def get_pack(set_code='ISD'):
    pack = []

    # Get a rare or mythic
    rare_card = None
    get_mythic = random.randint(0, 7) == 7
    if get_mythic:
        rare_card = st.get_random_card(f'set:{set_code} r=m in:booster')

    if rare_card is None:
        rare_card = st.get_random_card(f'set:{set_code} r=r in:booster')

    pack.append(rare_card)

    # Get 3 uncommons
    cards = st.search_for_cards(f'set:{set_code} r=u in:booster')
    uncommons = random.sample(list(cards), 3)
    pack += uncommons

    # Get 10 commons
    cards = st.search_for_cards(f'set:{set_code} r=c in:booster')
    commons = random.sample(list(cards), 10)
    pack += commons

    return pack


def get_sealed_pool(set_code='ISD'):
    # Get 6 packs and add them to the pool
    return {f'{set_code} - Pool {i}': get_pack(set_code) for i in range(6)}


def get_draft_pool(set_code='ISD'):
    # Get 3 packs and add them to the pool
    return {f'{set_code} - Pool {i}': get_pack(set_code) for i in range(3)}
