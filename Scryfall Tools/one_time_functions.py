import scryfall_tools as st


def create_set_review_lists(setcode):
    set_cards = st.search_for_cards(f'set={setcode} in:booster order=set')
    if not set_cards:
        print('Set not found')
        return
    cu_names = [(card['name'], card['collector_number']) for card in set_cards if card['rarity'] in ['common', 'uncommon']]
    rm_names = [(card['name'], card['collector_number']) for card in set_cards if card['rarity'] in ['rare', 'mythic']]
    with open(f'{setcode}_review.txt', 'w') as review_file:
        for name, number in cu_names:
            review_file.write(f'{number}\t{name}\n')
        for name, number in rm_names:
            review_file.write(f'{number}\t{name}\n')
    print(f'Wrote names to {setcode}_review.txt.')
