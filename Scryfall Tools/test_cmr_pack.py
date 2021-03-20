import csv

from limited_pools import get_pack

packs = 1000
file_name = f'CMR Card Data for {packs} packs.csv'
column_names = ['Amount', 'Collector Number', 'Name', 'Rarity', 'Legendary']


def test_cmr_packs():
    names = {}
    rarities = {}
    amounts = {}
    legendaries = {}

    print('\n')

    # Generate N packs, then add the cards to the cards dict
    for i in range(packs):
        print(f'Pack {i + 1}', end='\r', flush=True)
        for card in get_pack('cmr'):
            ccn = card.get('collector_number')
            names[ccn] = card.get('name')
            rarities[ccn] = card.get('rarity')
            type_line = card.get('type_line')
            legendaries[ccn] = 'Legendary' in type_line and (
                    'Creature' in type_line or 'Planeswalker' in type_line
            )

            amounts[ccn] = amounts.get(ccn, 0) + 1

    # Output the numbers to a CSV
    card_data = [
        {
            'Amount': amounts[key],
            'Collector Number': key,
            'Name': names[key],
            'Rarity': rarities[key],
            'Legendary': legendaries[key]
        }
        for key in names.keys()
    ]

    try:
        with open(file_name, 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=column_names)
            writer.writeheader()
            for data in card_data:
                writer.writerow(data)
    except IOError:
        print('I/O Error')

    print('\n')
