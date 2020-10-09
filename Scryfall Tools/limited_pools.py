import random

import scryfall_tools as st


def get_pack(set_code):
    # Get a rare or mythic (~14% chance of Mythic)
    if random.randint(0, 7) == 7:
        rare_card = st.get_random_card(f'set:{set_code} r=m in:booster')
    else:
        rare_card = st.get_random_card(f'set:{set_code} r=r in:booster')

    pack = [rare_card]

    # Get 3 uncommons
    cards = st.search_for_cards(f'set:{set_code} r=u in:booster')
    uncommons = random.sample(list(cards), 3)
    pack += uncommons

    # Get 10 commons
    cards = st.search_for_cards(f'set:{set_code} r=c in:booster')
    commons = random.sample(list(cards), 10)
    pack += commons

    return pack


def get_limited_pool(set_code, number_of_packs):
    return {
        f'{set_code.upper()} - Pack {i + 1}': get_pack(set_code)
        for i in range(number_of_packs)
    }
