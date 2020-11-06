import random

import scryfall_tools as st


def get_pack(set_code):
    def get_cmr_pack(set_code):
        # Commander Legends pack distribution        
        pack = []
        
        # Get 1 foil
        # Randomly determine rarity of foil
        foil_rng = random.randint(0, 119)
        if(foil_rng == 119):
            rarity = 'm'
        elif(foil_rng > 111):
            rarity = 'r'
        elif(foil_rng > 88):
            rarity = 'u'
        else:
            rarity = 'c'
        
        # If the foil is mythic, the foil can also be one of the 32 reprint commanders only found in foil etched versions
        if(rarity == 'm'):
            card = st.get_random_card(f's:cmr r:{rarity} (is:booster or (is:reprint frame:etched))')
        # If the foil is not mythic, the foil can only be a card found in draft boosters of the foil's rarity
        else:
            card = st.get_random_card(f's:cmr r:{rarity} is:booster')
        
        # There is a fifty percent chance a legendary foil will be replaced with an foil etched version
        card_name = card['name']
        # Search for the legendary keyword in the typeline
        if('Legendary' in card['type_line']):
            # If the card is legendary, replace it with the etched foil frame 50% of the time
            etched_foil_rng = random.randint(0, 1)
            if(etched_foil_rng == 1):
                # Replace the card with the foil etched version of the same name
                card = st.search_for_cards(f's:cmr {card_name} frame:etched')[0]
        
        pack += [card]
        
        # Get 2 legendary cards of any rarity
        legendary_rng_1 = random.randint(0,31)
        legendary_rng_2 = random.randint(0,31)
        
        if(legendary_rng_1 == 31):
            rarity_1='m'
        elif(legendary_rng_1 > 23):
            rarity_1='r'
        else:
            rarity_1='u'
        
        if(legendary_rng_2 == 31):
            rarity_2='m'
        elif(legendary_rng_2 > 23):
            rarity_2='r'
        else:
            rarity_2='u'
        
        pack += [st.get_random_card(f'set:{set_code} t:legendary is:booster r:{rarity_1}')]
        pack += [st.get_random_card(f'set:{set_code} t:legendary is:booster r:{rarity_2}')]
        
        # Get a rare or mythic (~14% chance of Mythic)
        if random.randint(0, 7) == 7:
            rare_card = st.get_random_card(f'set:{set_code} r=m is:booster -t:legendary')
        else:
            rare_card = st.get_random_card(f'set:{set_code} r=r is:booster -t:legendary')

        pack += [rare_card]
        
        # Get 3 uncommons
        cards = st.search_for_cards(f'set:{set_code} r=u -t:legendary is:booster')
        uncommons = random.sample(list(cards), 3)
        pack += uncommons
        
        # Get 13 commons
        # Determine if Prismatic piper replaces one of the foils
        if random.randint(0, 5) == 5:
            cards = st.search_for_cards(f'set:{set_code} r=c is:booster -"prismatic piper"')
            commons = random.sample(list(cards), 12)
            pack += commons
            pack += [st.get_card("The Prismatic Piper")]
        else:
            cards = st.search_for_cards(f'set:{set_code} r=c is:booster -"prismatic piper"')
            commons = random.sample(list(cards), 13)
            pack += commons
        # Finish the pack
        return pack
    
    def get_default_pack(set_code):
        # The default pack distribution
        # Get a rare or mythic (~14% chance of Mythic)
        if random.randint(0, 7) == 7:
            rare_card = st.get_random_card(f'set:{set_code} r=m is:booster')
        else:
            rare_card = st.get_random_card(f'set:{set_code} r=r is:booster')

        pack = [rare_card]

        # Get 3 uncommons
        cards = st.search_for_cards(f'set:{set_code} r=u is:booster')
        uncommons = random.sample(list(cards), 3)
        pack += uncommons

        # Get 10 commons
        cards = st.search_for_cards(f'set:{set_code} r=c is:booster')
        commons = random.sample(list(cards), 10)
        pack += commons

        return pack
        
    switcher = { 
        'cmr': get_cmr_pack
    }
    pack_constructor = switcher.get(set_code, get_default_pack)
    return pack_constructor(set_code)


def get_limited_pool(set_code, number_of_packs):
    return {
        f'{set_code.upper()} - Pack {i + 1}': get_pack(set_code)
        for i in range(number_of_packs)
    }
