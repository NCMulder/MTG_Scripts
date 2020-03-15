# Overrides specified cards with a different identifier scheme.
# Useful when you don't want to use the most recent art for a given card.
# Cardnames not featured in this dict use the identifier {'name': [cardname]}
# See https://scryfall.com/docs/api/cards/collection#card-identifiers
cardname_identifier_overrides = {
    'Plains': {'collector_number': '250', 'set': 'thb'},
    'Island': {'collector_number': '251', 'set': 'thb'},
    'Swamp': {'collector_number': '252', 'set': 'thb'},
    'Mountain': {'collector_number': '253', 'set': 'thb'},
    'Forest': {'collector_number': '254', 'set': 'thb'},
}
