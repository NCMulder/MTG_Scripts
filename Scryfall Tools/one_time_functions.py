import scryfall_tools as st


def create_set_review_lists(setcode):
    set_names = st.get_set_cards(setcode, keys=['name'])
    with open(f'{setcode}_review.txt', 'w') as review_file:
        for entry in set_names:
            review_file.write(f'{entry["name"]}\n')
    print(f'Wrote names to {setcode}_review.txt.')
