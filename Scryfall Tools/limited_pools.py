import random

import scryfall_tools as st


def get_pack(set_code):
    def get_cmr_pack():
        # Commander Legends pack distribution        
        pack = []

        # Get 1 foil
        # Get a random card of weighted random rarity, found in booster packs.
        # If the rarity is mythic, the foil can also be
        # one of the 32 reprint commanders only found in foil etched versions.
        card = st.get_random_card(
            f's:cmr (is:booster or (is:reprint frame:etched))'
            f' r:{random.choices(["m", "r", "u", "c"], [1, 8, 23, 88])[0]}'
        )

        # There is a 50% chance a legendary foil
        # will be replaced with a foil etched version.
        if 'Legendary' in card['type_line'] and \
                'Creature' in card['type_line']:
            if random.randint(0, 1) == 1:
                card = st.search_for_cards(
                    f's:cmr {card["name"]} frame:etched'
                )[0]

        pack += [card]

        # Add 2 legendary cards of any rarity
        rarities = random.choices(
            ['m', 'r', 'u'],
            [1, 8, 23],
            k=2
        )

        legendary_card_1 = st.get_random_card(
            f'set:{set_code} t:legendary is:booster r:{rarities[0]}'
        )
        pack += [
            legendary_card_1,
            st.get_random_card(
                f'set:{set_code} t:legendary is:booster '
                f'-"{legendary_card_1["name"]}" '
                f'r:{rarities[1]}'
            )
        ]

        # Add a rare or mythic (~14% chance of Mythic)
        pack += [st.get_random_card(
            f'set:{set_code} is:booster '
            f'r={random.choices(["m", "r"], [1, 6])[0]}'
        )]

        # Add 3 uncommons
        cards = st.search_for_cards(
            f'set:{set_code} r=u -t:legendary is:booster'
        )
        pack += [random.sample(list(cards), 3)]

        # Add 13 commons
        cards = st.search_for_cards(
            f'set:{set_code} r=c is:booster -"prismatic piper"'
        )
        # Prismatic Piper sometimes replaces one of the commons (~16.7% chance)
        if random.randint(0, 5) == 5:
            commons = random.sample(list(cards), 12)
            pack += [st.get_card("The Prismatic Piper")]
        else:
            commons = random.sample(list(cards), 13)
        pack += commons

        return pack

    def get_default_pack():
        # The default pack distribution
        pack = []

        # Add 1 basic land
        pack += [st.get_random_card(f'set:{set_code} is:booster t:basic')]

        # Add a rare or mythic (~14% chance of Mythic)
        pack += [st.get_random_card(
            f'set:{set_code} is:booster '
            f'r={random.choices(["m", "r"], [1, 6])[0]}'
        )]

        # Add 3 uncommons
        cards = st.search_for_cards(f'set:{set_code} r=u is:booster')
        pack += random.sample(list(cards), 3)

        # Add 10 commons
        cards = st.search_for_cards(f'set:{set_code} r=c is:booster -t:basic')
        pack += random.sample(list(cards), 10)

        return pack

    alt_distributions = {
        'cmr': get_cmr_pack
    }

    return alt_distributions.get(set_code, get_default_pack)()


def get_limited_pool(set_code, number_of_players, packs_per_player):
    if number_of_players == 1:
        names = [
            f'{set_code.upper()} - Pack {i + 1}'
            for i in range(packs_per_player)
        ]
    else:
        names = [
            f'{set_code.upper()} - Player {j + 1}, Pack {i + 1}'
            for j in range(number_of_players)
            for i in range(packs_per_player)
        ]

    return {name: get_pack(set_code) for name in names}
