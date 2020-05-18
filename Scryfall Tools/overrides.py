# Overrides specified cards with a different identifier scheme.
# Useful when you don't want to use the most recent art for a given card.
# Cardnames not featured in this dict use the identifier {'name': [cardname]}
# See https://scryfall.com/docs/api/cards/collection#card-identifiers

__basic_lands_defaults = {
    'Plains': {'name': 'Plains'},
    'Island': {'name': 'Island'},
    'Swamp': {'name': 'Swamp'},
    'Mountain': {'name': 'Mountain'},
    'Forest': {'name': 'Forest'},
}
__basic_lands_thb = {
    **__basic_lands_defaults,
    'Plains': {'collector_number': '250', 'set': 'thb'},
    'Island': {'collector_number': '251', 'set': 'thb'},
    'Swamp': {'collector_number': '252', 'set': 'thb'},
    'Mountain': {'collector_number': '253', 'set': 'thb'},
    'Forest': {'collector_number': '254', 'set': 'thb'}
}
__basic_lands_und = {
    key: {**value, 'set': 'und'}
    for key, value in __basic_lands_defaults.items()
}
__basic_lands_ust = {
    key: {**value, 'set': 'ust'}
    for key, value in __basic_lands_defaults.items()
}
__basic_lands_unh = {
    key: {**value, 'set': 'unh'}
    for key, value in __basic_lands_defaults.items()
}
__basic_lands_ugl = {
    key: {**value, 'set': 'ugl'}
    for key, value in __basic_lands_defaults.items()
}
_basic_lands = {
    'thb': __basic_lands_thb,
    'und': __basic_lands_und,
    'ust': __basic_lands_ust,
    'unh': __basic_lands_unh,
    'ugl': __basic_lands_ugl,
}

__basic_lands_snow_covered_defaults = {
    'Snow-Covered Plains': {'name': 'Snow-Covered Plains'},
    'Snow-Covered Island': {'name': 'Snow-Covered Island'},
    'Snow-Covered Swamp': {'name': 'Snow-Covered Swamp'},
    'Snow-Covered Mountain': {'name': 'Snow-Covered Mountain'},
    'Snow-Covered Forest': {'name': 'Snow-Covered Forest'},
}
__basic_lands_snow_covered_mh1 = {
    key: {**value, 'set': 'mh1'}
    for key, value in __basic_lands_snow_covered_defaults.items()
}
__basic_lands_snow_covered_sld = {
    key: {**value, 'set': 'sld'}
    for key, value in __basic_lands_snow_covered_defaults.items()
}
_basic_lands_snow_covered = {
    'mh1': __basic_lands_snow_covered_mh1,
    'sld': __basic_lands_snow_covered_sld,
}

__basic_lands_wastes_ula = {
    'Wastes': {'collector_number': '184', 'set': 'ogw'}
}
__basic_lands_wastes_koz = {
    'Wastes': {'collector_number': '183', 'set': 'ogw'}
}
_basic_lands_wastes = {
    'koz': __basic_lands_wastes_koz,
    'ula': __basic_lands_wastes_ula
}

_check_lands_defaults = {
    'Glacial Fortress': {'name': 'Glacial Fortress'},
    'Drowned Catacomb': {'name': 'Drowned Catacomb'},
    'Dragonskull Summit': {'name': 'Dragonskull Summit'},
    'Rootbound Crag': {'name': 'Rootbound Crag'},
    'Sunpetal Grove': {'name': 'Sunpetal Grove'},
    'Isolated Chapel': {'name': 'Isolated Chapel'},
    'Woodland Cemetery': {'name': 'Woodland Cemetery'},
    'Sulfur Falls': {'name': 'Sulfur Falls'},
    'Clifftop Retreat': {'name': 'Clifftop Retreat'},
    'Hinterland Harbor': {'name': 'Hinterland Harbor'},
}

_dual_lands_defaults = {
    'Badlands': {'name': 'Badlands'},
    'Bayou': {'name': 'Bayou'},
    'Plateau': {'name': 'Plateau'},
    'Savannah': {'name': 'Savannah'},
    'Scrubland': {'name': 'Scrubland'},
    'Taiga': {'name': 'Taiga'},
    'Tropical Island': {'name': 'Tropical Island'},
    'Tundra': {'name': 'Tundra'},
    'Underground Sea': {'name': 'Underground Sea'},
    'Volcanic Island': {'name': 'Volcanic Island'},
}

__fetch_lands_ally_defaults = {
    'Flooded Strand': {'name': 'Flooded Strand'},
    'Polluted Delta': {'name': 'Polluted Delta'},
    'Bloodstained Mire': {'name': 'Bloodstained Mire'},
    'Wooded Foothills': {'name': 'Wooded Foothills'},
    'Windswept Heath': {'name': 'Windswept Heath'},
}
__fetch_lands_ally_exp = {
    key: {**value, 'set': 'exp'}
    for key, value in __fetch_lands_ally_defaults.items()
}
_fetch_lands_ally = {
    'exp': __fetch_lands_ally_exp
}

__fetch_lands_enmy_defaults = {
    'Marsh Flats': {'name': 'Marsh Flats'},
    'Scalding Tarn': {'name': 'Scalding Tarn'},
    'Verdant Catacombs': {'name': 'Verdant Catacombs'},
    'Arid Mesa': {'name': 'Arid Mesa'},
    'Misty Rainforest': {'name': 'Misty Rainforest'},
}
__fetch_lands_enmy_exp = {
    key: {**value, 'set': 'exp'}
    for key, value in __fetch_lands_enmy_defaults.items()
}
__fetch_lands_enmy_slu = {
    key: {**value, 'set': 'slu'}
    for key, value in __fetch_lands_enmy_defaults.items()
}
_fetch_lands_enmy = {
    'exp': __fetch_lands_enmy_exp,
    'slu': __fetch_lands_enmy_slu
}

_shock_lands_defaults = {
    'Hallowed Fountain': {'name': 'Hallowed Fountain'},
    'Watery Grave': {'name': 'Watery Grave'},
    'Blood Crypt': {'name': 'Blood Crypt'},
    'Stomping Ground': {'name': 'Stomping Ground'},
    'Temple Garden': {'name': 'Temple Garden'},
    'Godless Shrine': {'name': 'Godless Shrine'},
    'Overgrown Tomb': {'name': 'Overgrown Tomb'},
    'Breeding Pool': {'name': 'Breeding Pool'},
    'Steam Vents': {'name': 'Steam Vents'},
    'Sacred Foundry': {'name': 'Sacred Foundry'},
}

_tricycle_lands_defaults = {
    'Indatha Triome': {'name': 'Indatha Triome'},
    'Ketria Triome': {'name': 'Ketria Triome'},
    'Raugrin Triome': {'name': 'Raugrin Triome'},
    'Savai Triome': {'name': 'Savai Triome'},
    'Zagoth Triome': {'name': 'Zagoth Triome'},
}
_tricycle_lands = {
    'Indatha Triome': {'collector_number': '309', 'set': 'iko'},
    'Ketria Triome': {'collector_number': '310', 'set': 'iko'},
    'Raugrin Triome': {'collector_number': '311', 'set': 'iko'},
    'Savai Triome': {'collector_number': '312', 'set': 'iko'},
    'Zagoth Triome': {'collector_number': '313', 'set': 'iko'},
}

_secret_lair_legends_defaults = {
    'Reaper King': {'name': 'Reaper King'},
    'Sliver Overlord': {'name': 'Sliver Overlord'},
    'The Ur-Dragon': {'name': 'The Ur-Dragon'},
    'Arahbo, Roar of the World': {'name': 'Arahbo, Roar of the World'},
    'Mirri, Weatherlight Duelist': {'name': 'Mirri, Weatherlight Duelist'},
    'Ink-Eyes, Servant of Oni': {'name': 'Ink-Eyes, Servant of Oni'},
    'Marrow-Gnawer': {'name': 'Marrow-Gnawer'},
    'Thalia, Guardian of Thraben': {'name': 'Thalia, Guardian of Thraben'},
    'Captain Sisay': {'name': 'Captain Sisay'},
    'Meren of Clan Nel Toth': {'name': 'Meren of Clan Nel Toth'},
    'Narset, Enlightened Tutor': {'name': 'Narset, Enlightened Tutor'},
    'Oona, Queen of the Fae': {'name': 'Oona, Queen of the Fae'},
    'Saskia the Unyielding': {'name': 'Saskia the Unyielding'},
}
_secret_lair_legends = {
    'Reaper King': {'collector_number': '9', 'set': 'sld'},
    'Sliver Overlord': {'collector_number': '10', 'set': 'sld'},
    'The Ur-Dragon': {'collector_number': '11', 'set': 'sld'},
    'Arahbo, Roar of the World': {'collector_number': '25', 'set': 'sld'},
    'Mirri, Weatherlight Duelist': {'collector_number': '26', 'set': 'sld'},
    'Ink-Eyes, Servant of Oni': {'collector_number': '33', 'set': 'sld'},
    'Marrow-Gnawer': {'collector_number': '34', 'set': 'sld'},
    'Thalia, Guardian of Thraben': {'collector_number': '38', 'set': 'sld'},
    'Captain Sisay': {'collector_number': '51', 'set': 'sld'},
    'Meren of Clan Nel Toth': {'collector_number': '52', 'set': 'sld'},
    'Narset, Enlightened Tutor': {'collector_number': '53', 'set': 'sld'},
    'Oona, Queen of the Fae': {'collector_number': '54', 'set': 'sld'},
    'Saskia the Unyielding': {'collector_number': '55', 'set': 'sld'},
}

_theros_divines_defaults = {
    'Heliod, God of the Sun': {'name': 'Heliod, God of the Sun'},
    'Karametra, God of Harvests': {'name': 'Karametra, God of Harvests'},
    'Iroas, God of Victory': {'name': 'Iroas, God of Victory'},
    'Thassa, God of the Sea': {'name': 'Thassa, God of the Sea'},
    'Ephara, God of the Polis': {'name': 'Ephara, God of the Polis'},
    'Kruphix, God of Horizons': {'name': 'Kruphix, God of Horizons'},
    'Erebos, God of the Dead': {'name': 'Erebos, God of the Dead'},
    'Phenax, God of Deception': {'name': 'Phenax, God of Deception'},
    'Athreos, God of Passage': {'name': 'Athreos, God of Passage'},
    'Purphoros, God of the Forge': {'name': 'Purphoros, God of the Forge'},
    'Mogis, God of Slaughter': {'name': 'Mogis, God of Slaughter'},
    'Keranos, God of Storms': {'name': 'Keranos, God of Storms'},
    'Nylea, God of the Hunt': {'name': 'Nylea, God of the Hunt'},
    'Xenagos, God of Revels': {'name': 'Xenagos, God of Revels'},
    'Pharika, God of Affliction': {'name': 'Pharika, God of Affliction'},
    'Daxos, Blessed by the Sun': {'name': 'Daxos, Blessed by the Sun'},
    'Heliod, Sun-Crowned': {'name': 'Heliod, Sun-Crowned'},
    'Callaphe, Beloved of the Sea': {'name': 'Callaphe, Beloved of the Sea'},
    'Thassa, Deep-Dwelling': {'name': 'Thassa, Deep-Dwelling'},
    'Erebos, Bleak-Hearted': {'name': 'Erebos, Bleak-Hearted'},
    'Tymaret, Chosen from Death': {'name': 'Tymaret, Chosen from Death'},
    'Anax, Hardened in the Forge': {'name': 'Anax, Hardened in the Forge'},
    'Purphoros, Bronze-Blooded': {'name': 'Purphoros, Bronze-Blooded'},
    'Nylea, Keen-Eyed': {'name': 'Nylea, Keen-Eyed'},
    'Renata, Called to the Hunt': {'name': 'enata, Called to the Hunt'},
    'Klothys, God of Destiny': {'name': 'Klothys, God of Destiny'},
}
_theros_divines = {
    'Heliod, God of the Sun': {'collector_number': '68', 'set': 'sld'},
    'Karametra, God of Harvests': {'collector_number': '69', 'set': 'sld'},
    'Iroas, God of Victory': {'collector_number': '70', 'set': 'sld'},
    'Thassa, God of the Sea': {'collector_number': '71', 'set': 'sld'},
    'Ephara, God of the Polis': {'collector_number': '72', 'set': 'sld'},
    'Kruphix, God of Horizons': {'collector_number': '73', 'set': 'sld'},
    'Erebos, God of the Dead': {'collector_number': '74', 'set': 'sld'},
    'Phenax, God of Deception': {'collector_number': '75', 'set': 'sld'},
    'Athreos, God of Passage': {'collector_number': '76', 'set': 'sld'},
    'Purphoros, God of the Forge': {'collector_number': '77', 'set': 'sld'},
    'Mogis, God of Slaughter': {'collector_number': '78', 'set': 'sld'},
    'Keranos, God of Storms': {'collector_number': '79', 'set': 'sld'},
    'Nylea, God of the Hunt': {'collector_number': '80', 'set': 'sld'},
    'Xenagos, God of Revels': {'collector_number': '81', 'set': 'sld'},
    'Pharika, God of Affliction': {'collector_number': '82', 'set': 'sld'},
    'Daxos, Blessed by the Sun': {'collector_number': '258', 'set': 'thb'},
    'Heliod, Sun-Crowned': {'collector_number': '259', 'set': 'thb'},
    'Callaphe, Beloved of the Sea': {'collector_number': '260', 'set': 'thb'},
    'Thassa, Deep-Dwelling': {'collector_number': '261', 'set': 'thb'},
    'Erebos, Bleak-Hearted': {'collector_number': '262', 'set': 'thb'},
    'Tymaret, Chosen from Death': {'collector_number': '263', 'set': 'thb'},
    'Anax, Hardened in the Forge': {'collector_number': '264', 'set': 'thb'},
    'Purphoros, Bronze-Blooded': {'collector_number': '265', 'set': 'thb'},
    'Nylea, Keen-Eyed': {'collector_number': '266', 'set': 'thb'},
    'Renata, Called to the Hunt': {'collector_number': '267', 'set': 'thb'},
    'Klothys, God of Destiny': {'collector_number': '268', 'set': 'thb'},
}

_planeswalkers = {
    'Elspeth, Sun\'s Nemesis': {'collector_number': '255', 'set': 'thb'},
    'Ashiok, Nightmare Muse': {'collector_number': '256', 'set': 'thb'},
    'Calix, Destiny\'s Hand': {'collector_number': '257', 'set': 'thb'},
    'Lukka, Coppercoat Outcast': {'collector_number': '276', 'set': 'iko'},
    'Viven, Monsters\'s Advocate': {'collector_number': '277', 'set': 'iko'},
    'Narset of the Ancient Way': {'collector_number': '278', 'set': 'iko'},
}

_transform_cards_ixalan = {
    'Legion\'s Landing': {'collector_number': '22', 'set': 'pxtc'},
    'Searh For Azcanta': {'collector_number': '74', 'set': 'pxtc'},
    'Arguel\'s Blood Fast': {'collector_number': '90', 'set': 'pxtc'},
    'Vance\'s Blasting Cannons': {'collector_number': '173', 'set': 'pxtc'},
    'Growing Rites of Itlimoc': {'collector_number': '191', 'set': 'pxtc'},
    'Conqueror\'s Galleon': {'collector_number': '234', 'set': 'pxtc'},
    'Dowsing Dagger': {'collector_number': '235', 'set': 'pxtc'},
    'Primal Amulet': {'collector_number': '243', 'set': 'pxtc'},
    'Thaumatic Compass': {'collector_number': '249', 'set': 'pxtc'},
    'Treasure Map': {'collector_number': '250', 'set': 'pxtc'},
}

_mutatoes_showcase = {
    'Cubwarden': {'collector_number': '279', 'set': 'iko'},
    'Huntmaster Liger': {'collector_number': '280', 'set': 'iko'},
    'Majestic Auricorn': {'collector_number': '281', 'set': 'iko'},
    'Vulpikeet': {'collector_number': '282', 'set': 'iko'},
    'Archipelagore': {'collector_number': '283', 'set': 'iko'},
    'Dreamtail Heron': {'collector_number': '284', 'set': 'iko'},
    'Pouncing Shoreshark': {'collector_number': '285', 'set': 'iko'},
    'Sea-Dasher Octopus': {'collector_number': '286', 'set': 'iko'},
    'Cavern Whisperer': {'collector_number': '287', 'set': 'iko'},
    'Chittering Harvester': {'collector_number': '288', 'set': 'iko'},
    'Dirge Bat': {'collector_number': '289', 'set': 'iko'},
    'Insatiable Hemophage': {'collector_number': '290', 'set': 'iko'},
    'Cloudpiercer': {'collector_number': '291', 'set': 'iko'},
    'Everquil Phoenix': {'collector_number': '292', 'set': 'iko'},
    'Porcuparrot': {'collector_number': '293', 'set': 'iko'},
    'Auspicious Starrix': {'collector_number': '294', 'set': 'iko'},
    'Gemrazer': {'collector_number': '295', 'set': 'iko'},
    'Glowstone Recluse': {'collector_number': '296', 'set': 'iko'},
    'Migratory Greathorn': {'collector_number': '297', 'set': 'iko'},
    'Boneyard Lurker': {'collector_number': '298', 'set': 'iko'},
    'Brokkos, Apex of Forever': {'collector_number': '299', 'set': 'iko'},
    'Illuna, Apex of Wishes': {'collector_number': '300', 'set': 'iko'},
    'Lore Drakkis': {'collector_number': '301', 'set': 'iko'},
    'Necropanther': {'collector_number': '302', 'set': 'iko'},
    'Nethroi, Apex of Death': {'collector_number': '303', 'set': 'iko'},
    'Parcelbeast': {'collector_number': '304', 'set': 'iko'},
    'Regal Leosaur': {'collector_number': '305', 'set': 'iko'},
    'Snapdax, Apex of the Hunt': {'collector_number': '306', 'set': 'iko'},
    'Trumpeting Gnarr': {'collector_number': '307', 'set': 'iko'},
    'Vadrok, Apex of Thunder': {'collector_number': '308', 'set': 'iko'},
}

cardname_identifier_overrides = {
    **_basic_lands['thb'],
    **_basic_lands_snow_covered['mh1'],
    **_basic_lands_wastes['koz'],

    # **_fetch_lands_ally['exp'],

    **_fetch_lands_enmy['slu'],

    **_tricycle_lands,

    **_secret_lair_legends,

    **_theros_divines,

    **_planeswalkers,

    **_transform_cards_ixalan,

    **_mutatoes_showcase,
}
