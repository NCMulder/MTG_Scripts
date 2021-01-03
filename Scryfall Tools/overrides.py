# Overrides specified cards with a different identifier scheme.
# Useful when you don't want to use the most recent art for a given card.
# Cardnames not featured in this dict use the identifier {'name': [cardname]}
# See https://scryfall.com/docs/api/cards/collection#card-identifiers

import random

_lands = {
    'basic': {
        'def': {
            'Plains': {'name': 'Plains'},
            'Island': {'name': 'Island'},
            'Swamp': {'name': 'Swamp'},
            'Mountain': {'name': 'Mountain'},
            'Forest': {'name': 'Forest'},
        }
    },
    'snow': {
        'def': {
            'Snow-Covered Plains': {'name': 'Snow-Covered Plains'},
            'Snow-Covered Island': {'name': 'Snow-Covered Island'},
            'Snow-Covered Swamp': {'name': 'Snow-Covered Swamp'},
            'Snow-Covered Mountain': {'name': 'Snow-Covered Mountain'},
            'Snow-Covered Forest': {'name': 'Snow-Covered Forest'},
        }
    },
    'wastes': {
        'def': {
            'Wastes': {'name': 'Wastes'}
        }
    },

    'bond': {
        'ally': {
            'def': {
                'Bountiful Promenade': {'name': 'Bountiful Promenade'},
                'Luxury Suite': {'name': 'Luxury Suite'},
                'Morphic Pool': {'name': 'Morphic Pool'},
                'Sea of Clouds': {'name': 'Sea of Clouds'},
                'Spire Garden': {'name': 'Spire Garden'},
            }
        },
        'enmy': {
            'def': {
                'Rejuvenating Springs': {'name': 'Rejuvenating Springs'},
                'Spectator Seating': {'name': 'Spectator Seating'},
                'Traing Center': {'name': 'Spectator Seating'},
                'Undergrowth Stadium': {'name': 'Undergrowth Stadium'},
                'Vault of Champions': {'name': 'Vault of Champions'},
            }
        }
    },
    'check': {
        'def': {
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
    },
    'dual': {
        'def': {
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
    },
    'fast': {
        'def': {
            'Seachrome Coast': {'name': 'Seachrome Coast'},
            'Darkslick Shores': {'name': 'Darkslick Shores'},
            'Blackcleave Cliffs': {'name': 'Blackcleave Cliffs'},
            'Copperline Gorge': {'name': 'Copperline Gorge'},
            'Razorverge Thicket': {'name': 'Razorverge Thicket'},
        }
    },
    'fetch': {
        'ally': {
            'def': {
                'Flooded Strand': {'name': 'Flooded Strand'},
                'Polluted Delta': {'name': 'Polluted Delta'},
                'Bloodstained Mire': {'name': 'Bloodstained Mire'},
                'Wooded Foothills': {'name': 'Wooded Foothills'},
                'Windswept Heath': {'name': 'Windswept Heath'},
            }
        },
        'enmy': {
            'def': {
                'Marsh Flats': {'name': 'Marsh Flats'},
                'Scalding Tarn': {'name': 'Scalding Tarn'},
                'Verdant Catacombs': {'name': 'Verdant Catacombs'},
                'Arid Mesa': {'name': 'Arid Mesa'},
                'Misty Rainforest': {'name': 'Misty Rainforest'},
            }
        }
    },
    'pathway': {
        'def': {
            'Barkchannel Pathway // Tidechannel Pathway': {
                'collector_number': '290', 'set': 'khm'
            },
            'Blightstep Pathway // Searstep Pathway': {
                'collector_number': '291', 'set': 'khm'
            },
            'Branchloft Pathway // Boulderloft Pathway': {
                'collector_number': '284', 'set': 'znr'
            },
            'Brightclimb Pathway // Grimclimb Pathway': {
                'collector_number': '285', 'set': 'znr'
            },
            'Clearwater Pathway // Murkwater Pathway': {
                'collector_number': '286', 'set': 'znr'
            },
            'Cragcrown Pathway // Timbercrown Pathway': {
                'collector_number': '287', 'set': 'znr'
            },
            'Darkbore Pathway // Slitherbore Pathway': {
                'collector_number': '292', 'set': 'khm'
            },
            'Hengegate Pathway // Mistgate Pathway': {
                'collector_number': '293', 'set': 'khm'
            },
            'Needleverge Pathway // Pillarverge Pathway': {
                'collector_number': '288', 'set': 'znr'
            },
            'Riverglide Pathway // Lavaglide Pathway': {
                'collector_number': '289', 'set': 'znr'
            },
        }
    },
    'shock': {
        'def': {
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
    },
    'special': {
        'def': {
            'Ancient Tomb': {'name': 'Ancient Tomb'},
            'Cavern of Souls': {'name': 'Cavern of Souls'},
            'Celestial Colonnade': {'name': 'Celestial Colonnade'},
            'Creeping Tar Pit': {'name': 'Creeping Tar Pit'},
            'Grove of the Burnwillows': {'name': 'Grove of the Burnwillows'},
            'Horizon Canopy': {'name': 'Horizon Canopy'},
            'Prismatic Vista': {'name': 'Prismatic Vista'},
            'Strip Mine': {'name': 'Strip Mine'},
            'Valakut, the Molten Pinnacle': {
                'name': 'Valakut, the Molten Pinnacle'
            },
            'Wasteland': {'name': 'Wasteland'},
        }
    },
    'triome': {
        'def': {
            'Indatha Triome': {'name': 'Indatha Triome'},
            'Ketria Triome': {'name': 'Ketria Triome'},
            'Raugrin Triome': {'name': 'Raugrin Triome'},
            'Savai Triome': {'name': 'Savai Triome'},
            'Zagoth Triome': {'name': 'Zagoth Triome'},
        }
    }
}

_lands['basic']['thb'] = {
    'Plains': {'collector_number': '250', 'set': 'thb'},
    'Island': {'collector_number': '251', 'set': 'thb'},
    'Swamp': {'collector_number': '252', 'set': 'thb'},
    'Mountain': {'collector_number': '253', 'set': 'thb'},
    'Forest': {'collector_number': '254', 'set': 'thb'}
}
_lands['basic']['und'] = {
    key: {**value, 'set': 'und'}
    for key, value in _lands['basic']['def'].items()
}
_lands['basic']['ust'] = {
    key: {**value, 'set': 'ust'}
    for key, value in _lands['basic']['def'].items()
}
_lands['basic']['unh'] = {
    key: {**value, 'set': 'unh'}
    for key, value in _lands['basic']['def'].items()
}
_lands['basic']['ugl'] = {
    key: {**value, 'set': 'ugl'}
    for key, value in _lands['basic']['def'].items()
}
_lands['basic']['znr'] = {
    'Plains': {
        'collector_number': random.choice(['266', '267', '268']),
        'set': 'znr'
    },
    'Island': {
        'collector_number': random.choice(['269', '270', '271']),
        'set': 'znr'
    },
    'Swamp': {
        'collector_number': random.choice(['272', '273', '274']),
        'set': 'znr'
    },
    'Mountain': {
        'collector_number': random.choice(['275', '276', '277']),
        'set': 'znr'
    },
    'Forest': {
        'collector_number': random.choice(['278', '279', '280']),
        'set': 'znr'
    }
}

_lands['snow']['mh1'] = {
    key: {**value, 'set': 'mh1'}
    for key, value in _lands['snow']['def'].items()
}
_lands['snow']['sld'] = {
    key: {**value, 'set': 'sld'}
    for key, value in _lands['snow']['def'].items()
}

_lands['wastes']['ula'] = {
    'Wastes': {'collector_number': '184', 'set': 'ogw'}
}
_lands['wastes']['koz'] = {
    'Wastes': {'collector_number': '183', 'set': 'ogw'}
}

_lands['bond']['ally']['zne'] = {
    key: {**value, 'set': 'zne'}
    for key, value in _lands['bond']['ally']['def'].items()
}
_lands['bond']['enmy']['cmr'] = {
    'Rejuvenating Springs': {
        'collector_number': '709', 'set': 'cmr'
    },
    'Spectator Seating': {
        'collector_number': '711', 'set': 'cmr'
    },
    'Training Center': {
        'collector_number': '713', 'set': 'cmr'
    },
    'Undergrowth Stadium': {
        'collector_number': '714', 'set': 'cmr'
    },
    'Vault of Champions': {
        'collector_number': '715', 'set': 'cmr'
    }
}

_lands['fast']['zne'] = {
    key: {**value, 'set': 'zne'}
    for key, value in _lands['fast']['def'].items()
}

_lands['fetch']['ally']['exp'] = {
    key: {**value, 'set': 'exp'}
    for key, value in _lands['fetch']['ally']['def'].items()
}
_lands['fetch']['ally']['zne'] = {
    key: {**value, 'set': 'zne'}
    for key, value in _lands['fetch']['ally']['def'].items()
}

_lands['fetch']['enmy']['exp'] = {
    key: {**value, 'set': 'exp'}
    for key, value in _lands['fetch']['enmy']['def'].items()
}
_lands['fetch']['enmy']['slu'] = {
    key: {**value, 'set': 'slu'}
    for key, value in _lands['fetch']['enmy']['def'].items()
}
_lands['fetch']['enmy']['zne'] = {
    key: {**value, 'set': 'zne'}
    for key, value in _lands['fetch']['enmy']['def'].items()
}

_lands['pathway']['khm'] = {
    **_lands['pathway']['def'],

    'Branchloft Pathway // Boulderloft Pathway': {
        'name': 'Branchloft Pathway', 'set': 'slu'
    },
    'Brightclimb Pathway // Grimclimb Pathway': {
        'name': 'Brightclimb Pathway', 'set': 'slu'
    },
    'Clearwater Pathway // Murkwater Pathway': {
        'name': 'Clearwater Pathway', 'set': 'slu'
    },
    'Cragcrown Pathway // Timbercrown Pathway': {
        'name': 'Cragcrown Pathway', 'set': 'slu'
    },
    'Needleverge Pathway // Pillarverge Pathway': {
        'name': 'Needleverge Pathway', 'set': 'slu'
    },
    'Riverglide Pathway // Lavaglide Pathway': {
        'name': 'Riverglide Pathway', 'set': 'slu'
    },

}
_lands['pathway']['znr'] = {
    **_lands['pathway']['def'],

    # TODO: Add these when they get released
    # 'Barkchannel Pathway // Tidechannel Pathway': {
    #     'name': 'Barkchannel Pathway', 'set': 'slu'
    # },
    # 'Blightstep Pathway // Searstep Pathway': {
    #     'name': 'Blightstep Pathway', 'set': 'slu'
    # },
    # 'Darkbore Pathway // Slitherbore Pathway': {
    #     'name': 'Darkbore Pathway', 'set': 'slu'
    # },
    # 'Hengegate Pathway // Mistgate Pathway': {
    #     'name': 'Hengegate Pathway', 'set': 'slu'
    # },
}

_lands['shock']['exp'] = {
    key: {**value, 'set': 'exp'}
    for key, value in _lands['shock']['def'].items()
}

_lands['special']['zne'] = {
    key: {**value, 'set': 'zne'}
    for key, value in _lands['special']['def'].items()

}

_lands['triome']['iko'] = {
    **_lands['triome']['def'],
    'Indatha Triome': {
        'collector_number': '309', 'set': 'iko'
    },
    'Ketria Triome': {
        'collector_number': '310', 'set': 'iko'
    },
    'Raugrin Triome': {
        'collector_number': '311', 'set': 'iko'
    },
    'Savai Triome': {
        'collector_number': '312', 'set': 'iko'
    },
    'Zagoth Triome': {
        'collector_number': '313', 'set': 'iko'
    },
}

_etched_foil_legends = {
    'Najeela, the Blade-Blossom': {'collector_number': '514', 'set': 'cmr'},
    'Akiri, Line-Slinger': {'collector_number': '515', 'set': 'cmr'},
    'Brago, King Eternal': {'collector_number': '516', 'set': 'cmr'},
    'Bruse Tarl, Boorish Herder': {'collector_number': '517', 'set': 'cmr'},
    'Derevi, Empyrial Tactician': {'collector_number': '518', 'set': 'cmr'},
    'Ikra Shidiqi, the Usurper': {'collector_number': '519', 'set': 'cmr'},
    'Ishai, Ojutai Dragonspeaker': {'collector_number': '520', 'set': 'cmr'},
    'Karador, Ghost Chieftain': {'collector_number': '521', 'set': 'cmr'},
    'Karametra, God of Harvests': {'collector_number': '522', 'set': 'cmr'},
    'Kraum, Ludevic\'s Opus': {'collector_number': '523', 'set': 'cmr'},
    'Kydele, Chosen of Kruphix': {'collector_number': '524', 'set': 'cmr'},
    'Ludevic, Necro-Alchemist': {'collector_number': '525', 'set': 'cmr'},
    'Maelstrom Wanderer': {'collector_number': '526', 'set': 'cmr'},
    'Marath, Will of the Wild': {'collector_number': '527', 'set': 'cmr'},
    'Muldrotha, the Gravetide': {'collector_number': '528', 'set': 'cmr'},
    'Nekusar, the Mindrazer': {'collector_number': '529', 'set': 'cmr'},
    'Prossh, Skyraider of Kher': {'collector_number': '530', 'set': 'cmr'},
    'Queen Marchesa': {'collector_number': '531', 'set': 'cmr'},
    'Rakdos, Lord of Riots': {'collector_number': '532', 'set': 'cmr'},
    'Ravos, Soultender': {'collector_number': '533', 'set': 'cmr'},
    'Reyhan, Last of the Abzan': {'collector_number': '534', 'set': 'cmr'},
    'Sidar Kondo of Jamuraa': {'collector_number': '535', 'set': 'cmr'},
    'Silas Renn, Seeker Adept': {'collector_number': '536', 'set': 'cmr'},
    'Tana, the Bloodsower': {'collector_number': '537', 'set': 'cmr'},
    'Thrasios, Triton Hero': {'collector_number': '538', 'set': 'cmr'},
    'Tymna the Weaver': {'collector_number': '539', 'set': 'cmr'},
    'Vial Smasher the Fierce': {'collector_number': '540', 'set': 'cmr'},
    'Xenagos, God of Revels': {'collector_number': '541', 'set': 'cmr'},
    'Yuriko, the Tiger\'s Shadow': {'collector_number': '542', 'set': 'cmr'},
    'Zedruu the Greathearted': {'collector_number': '543', 'set': 'cmr'},
    'Zur the Enchanter': {'collector_number': '544', 'set': 'cmr'},
    'Ramos, Dragon Engine': {'collector_number': '545', 'set': 'cmr'},
    'The Prismatic Piper': {'collector_number': '546', 'set': 'cmr'},
    'Akroma, Vision of Ixidor': {'collector_number': '547', 'set': 'cmr'},
    'Alharu, Solemn Ritualist': {'collector_number': '548', 'set': 'cmr'},
    'Ardenn, Intrepid Archaeologist': {
        'collector_number': '549', 'set': 'cmr'
    },
    'Keleth, Sunmane Familiar': {'collector_number': '550', 'set': 'cmr'},
    'Livio, Oathsworn Sentinel': {'collector_number': '551', 'set': 'cmr'},
    'Prava of the Steel Legion': {'collector_number': '552', 'set': 'cmr'},
    'Radiant, Serra Archangel': {'collector_number': '553', 'set': 'cmr'},
    'Rebbec, Architect of Ascension': {
        'collector_number': '554', 'set': 'cmr'
    },
    'Brinelin, the Moon Kraken': {'collector_number': '555', 'set': 'cmr'},
    'Eligeth, Crossroads Augur': {'collector_number': '556', 'set': 'cmr'},
    'Esior, Wardwing Familiar': {'collector_number': '557', 'set': 'cmr'},
    'Ghost of Ramirez DePietro': {'collector_number': '558', 'set': 'cmr'},
    'Glacian, Powerstone Engineer': {'collector_number': '559', 'set': 'cmr'},
    'Malcolm, Keen-Eyed Navigator': {'collector_number': '560', 'set': 'cmr'},
    'Sakashima of a Thousand Faces': {'collector_number': '561', 'set': 'cmr'},
    'Siani, Eye of the Storm': {'collector_number': '562', 'set': 'cmr'},
    'Armix, Filigree Thrasher': {'collector_number': '563', 'set': 'cmr'},
    'Falthis, Shadowcat Familiar': {'collector_number': '564', 'set': 'cmr'},
    'Keskit, the Flesh Sculptor': {'collector_number': '565', 'set': 'cmr'},
    'Miara, Thorn of the Glade': {'collector_number': '566', 'set': 'cmr'},
    'Nadier, Agent of the Duskenel': {'collector_number': '567', 'set': 'cmr'},
    'Sengir, the Dark Baron': {'collector_number': '568', 'set': 'cmr'},
    'Tormod, the Desecrator': {'collector_number': '569', 'set': 'cmr'},
    'Alena, Kessig Trapper': {'collector_number': '570', 'set': 'cmr'},
    'Breeches, Brazen Plunderer': {'collector_number': '571', 'set': 'cmr'},
    'Dargo, the Shipwrecker': {'collector_number': '572', 'set': 'cmr'},
    'Kediss, Emberclaw Familiar': {'collector_number': '573', 'set': 'cmr'},
    'Krark, the Thumbless': {'collector_number': '574', 'set': 'cmr'},
    'Rograkh, Son of Rohgahh': {'collector_number': '575', 'set': 'cmr'},
    'Toggo, Goblin Weaponsmith': {'collector_number': '576', 'set': 'cmr'},
    'Anara, Wolvid Familiar': {'collector_number': '577', 'set': 'cmr'},
    'Gilanra, Caller of Wirewood': {'collector_number': '578', 'set': 'cmr'},
    'Halana, Kessig Ranger': {'collector_number': '579', 'set': 'cmr'},
    'Ich-Tekik, Salvage Splicer': {'collector_number': '580', 'set': 'cmr'},
    'Kamahl, Heart of Krosa': {'collector_number': '581', 'set': 'cmr'},
    'Kodama of the East Tree': {'collector_number': '582', 'set': 'cmr'},
    'Numa, Joraga Chieftain': {'collector_number': '583', 'set': 'cmr'},
    'Slurrk, All-Ingesting': {'collector_number': '584', 'set': 'cmr'},
    'Abomination of Llanowar': {'collector_number': '585', 'set': 'cmr'},
    'Amareth, the Lustrous': {'collector_number': '586', 'set': 'cmr'},
    'Araumi of the Dead Tide': {'collector_number': '587', 'set': 'cmr'},
    'Archelos, Lagoon Mystic': {'collector_number': '588', 'set': 'cmr'},
    'Averna, the Chaos Bloom': {'collector_number': '589', 'set': 'cmr'},
    'Belbe, Corrupted Observer': {'collector_number': '590', 'set': 'cmr'},
    'Bell Borca, Spectral Sergeant': {'collector_number': '591', 'set': 'cmr'},
    'Blim, Comedic Genius': {'collector_number': '592', 'set': 'cmr'},
    'Captain Vargus Wrath': {'collector_number': '593', 'set': 'cmr'},
    'Colfenor, the Last Yew': {'collector_number': '594', 'set': 'cmr'},
    'Ghen, Arcanum Weaver': {'collector_number': '595', 'set': 'cmr'},
    'Gnostro, Voice of the Crags': {'collector_number': '596', 'set': 'cmr'},
    'Gor Muldrak, Amphinologist': {'collector_number': '597', 'set': 'cmr'},
    'Hamza, Guardian of Arashin': {'collector_number': '598', 'set': 'cmr'},
    'Hans Eriksson': {'collector_number': '599', 'set': 'cmr'},
    'Imoti, Celebrant of Bounty': {'collector_number': '600', 'set': 'cmr'},
    'Jared Carthalion, True Heir': {'collector_number': '601', 'set': 'cmr'},
    'Juri, Master of the Revue': {'collector_number': '602', 'set': 'cmr'},
    'Kangee, Sky Warden': {'collector_number': '603', 'set': 'cmr'},
    'Kwain, Itinerant Meddler': {'collector_number': '604', 'set': 'cmr'},
    'Lathiel, the Bounteous Dawn': {'collector_number': '605', 'set': 'cmr'},
    'Liesa, Shroud of Dusk': {'collector_number': '606', 'set': 'cmr'},
    'Nevinyrral, Urborg Tyrant': {'collector_number': '607', 'set': 'cmr'},
    'Nymris, Oona\'s Trickster': {'collector_number': '608', 'set': 'cmr'},
    'Obeka, Brute Chronologist': {'collector_number': '609', 'set': 'cmr'},
    'Reyav, Master Smith': {'collector_number': '610', 'set': 'cmr'},
    'Thalisse, Reverent Medium': {'collector_number': '611', 'set': 'cmr'},
    'Tuya Bearclaw': {'collector_number': '612', 'set': 'cmr'},
    'Yurlok of Scorch Thrash': {'collector_number': '613', 'set': 'cmr'},
    'Zara, Renegade Recruiter': {'collector_number': '614', 'set': 'cmr'},
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

_planeswalkers = {
    'Elspeth, Sun\'s Nemesis': {'collector_number': '255', 'set': 'thb'},
    'Ashiok, Nightmare Muse': {'collector_number': '256', 'set': 'thb'},
    'Calix, Destiny\'s Hand': {'collector_number': '257', 'set': 'thb'},

    'Lukka, Coppercoat Outcast': {'collector_number': '276', 'set': 'iko'},
    'Viven, Monsters\'s Advocate': {'collector_number': '277', 'set': 'iko'},
    'Narset of the Ancient Way': {'collector_number': '278', 'set': 'iko'},

    'Jace, Mirror Mage': {'collector_number': '281', 'set': 'znr'},
    'Nahiri, Heir of the Ancients': {'collector_number': '282', 'set': 'znr'},
    'Nissa of Shadowed Boughs': {'collector_number': '283', 'set': 'znr'},
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

cardname_identifier_overrides = {
    **_lands['basic']['znr'],
    **_lands['snow']['mh1'],
    **_lands['wastes']['ula'],

    **_lands['bond']['ally']['zne'],
    **_lands['bond']['enmy']['cmr'],

    **_lands['fast']['zne'],

    **_lands['fetch']['ally']['zne'],
    **_lands['fetch']['enmy']['zne'],

    **_lands['pathway']['khm'],

    **_lands['special']['zne'],

    **_lands['triome']['iko'],

    **_etched_foil_legends,

    **_planeswalkers,

    **_transform_cards_ixalan,

    **_mutatoes_showcase,

    **_secret_lair_legends,

    **_theros_divines,
}
