import json
import copy
from os import listdir
from pathlib import Path
from random import choice
from datetime import date

def classic_jumpstart(pools=2, out=None, unnamed=False):
    list_path = 'resources/Jumpstart JSONs/'
    JS_lists = listdir(list_path)

    states = { 'ObjectStates': [] }
    for i in range(pools):
        for j in range(4):
            deck_path = choice(JS_lists)
            with open(Path(list_path, deck_path)) as deck_file:
                deck_json = json.loads(deck_file.read())
                for deck in deck_json['ObjectStates']:
                    deck['Transform']['posX'] += 3 * j
                    deck['Transform']['posZ'] += 8 * i
                    if unnamed:
                        if 'tokens' in deck['Nickname']:
                            deck['Nickname'] = f'Pool {i + 1}, pack {j + 1} [tokens]'
                        else:
                            deck['Nickname'] = f'Pool {i + 1}, pack {j + 1}'
                    else:
                        deck['Transform']['rotZ'] = 0
                    states['ObjectStates'].append(deck)
    
    json_path = Path(out or Path().absolute(), f'Jumpstart {date.today()}.json')
    with open(json_path, mode='w') as new_json:
        new_json.write(json.dumps(states, indent=4))

def random_jumpstart(decks=2, out=None, unnamed=False):
    list_path = 'resources/Jumpstart JSONs/'
    JS_lists = listdir(list_path)

    states = { 'ObjectStates': [] }
    for deck_i in range(decks):

        deck_1 = choice(JS_lists)
        deck_2 = choice(JS_lists)
        
        with open(Path(list_path, deck_1)) as deck_1_file, open(Path(list_path, deck_2)) as deck_2_file:
            deck_1_json = json.loads(deck_1_file.read())
            deck_2_json = json.loads(deck_2_file.read())

            combined_deck = copy.deepcopy(deck_1_json)

            last_deckname = ''
            for i, deck in enumerate(deck_2_json['ObjectStates']):
                ## If the base deck has no tokens, just add the token deck
                if len(combined_deck['ObjectStates']) <= i:
                    deck['Nickname'] = last_deckname + ' [tokens]'
                    deck['Transform']['posX'] += 3 * deck_i
                    combined_deck['ObjectStates'].append(deck)
                    continue
                ## Get the corresponding deck from the first json
                base_deck = combined_deck['ObjectStates'][i]
                ## Move it for multiple players
                base_deck['Transform']['posX'] += 3 * deck_i

                ## Change the name accordingly
                if unnamed:
                    last_deckname = f'Deck {deck_i + 1}' + ' [tokens]' if 'tokens' in deck['Nickname'] else ''
                else:
                    base_deck['Transform']['rotZ'] = 0
                    last_deckname = base_deck['Nickname'] + '+' + deck['Nickname']
                base_deck['Nickname'] = last_deckname

                ## Add the non-overlapping image sheets
                for key in deck['CustomDeck'].keys():
                    if key not in base_deck['CustomDeck']:
                        base_deck['CustomDeck'][key] = deck['CustomDeck'][key]
                
                ## Add the card objects and IDs
                base_deck['ContainedObjects'][-1:-1] = deck['ContainedObjects']
                base_deck['DeckIDs'][-1:-1] = deck['DeckIDs']
            states['ObjectStates'] += combined_deck['ObjectStates']

    json_path = Path(out or Path().absolute(), f'Jumpstart {date.today()}.json')
    with open(json_path, mode='w') as new_json:
        new_json.write(json.dumps(states, indent=4))

if __name__ == '__main__':
    ## For 2 random Jumpstart decks
    random_jumpstart(decks=2, unnamed=True)
    ## For 2 classic Jumpstart pools
    classic_jumpstart(pools=2)