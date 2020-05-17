# Nielsch's MTG Scripts
This is a collection of scripts I've been creating for Magic: The Gathering related tasks.

## Tabletop Simulator Deck Generator
The bulk of the useful scripts are located in the [Scryfall Tools](Scryfall%20Tools) Folder. 
I really should work on restructuring this whole thing but that's what you'll get for now.
This tool takes a decklist, generates and uploads the card images to your Dropbox, 
and creates a JSON file that Tabletop Simulator can read to import your deck.

#### Setup
First of all, if you want to run these scripts, you should get a [Dropbox API key](
https://blogs.dropbox.com/developers/2014/05/generate-an-access-token-for-your-own-account/
) by creating an app choosing the Dropbox API, choosing "App Folder", and naming your app. 
Get your personal API key under `<appname> -> Settings -> OAuth2 -> Generated access token`, 
copy the `config_default.ini` file, rename it to `config.ini` and place your API key in there.

Next we have a few dependencies to install. 
First off, you will need `pipenv`, instructions on how to install it are found on [its site](
https://pipenv.pypa.io/en/latest/install/#pragmatic-installation-of-pipenv
).

After installing `pipenv` we can use it to install the rest of our dependencies. 
Open your favorite command line tool to the Scryfall Tools directory and run `pipenv install`.

After installation we open the virtual environment through `pipenv shell`. 

Voilà, we can now run the scripts without any `ModuleNotFoundErrors`!

#### Functionality
The main entry point for all functionality is `python main.py mode`
You can run this command with one of the modes below to create a deck.

| Mode					| Description																		|
| --------------------- | ---------------------------------------------------------------------------------	|
| `decklist`			| Gets a decklist from the specified location.										|
| `draft`				| Gets a 3 pack draft pool from a specified set.									|
| `random_commander`	| Grabs a random commander from Scryfall and gets the average decklist from EDHRec.	|
| `sealed`				| Gets a 6 pack sealed pool from a specified set.									|

#### Global parameters
`-o`

*"Absolute path of the directory in which to store the generated deck"*

Defaults to the output path set in `config.ini`, or the Scryfall Tools folder.

This argument can be specified to point the generated JSON file somewhere other than the Scryfall Tools folder.
We recommend setting it to `D:\Documents\My Games\Tabletop Simulator\Saves\Saved Objects`, 
or wherever you get your Saved Objects in Tabletop Simulator.

`-s` 

*"Card image size"*

Defaults to `normal` (488 by 680px).

This argument can be used to specify a card image size. 
Supported arguments are `png`, `border_crop`, `art_crop`, `large`, `normal` and `small`.
Larger sizes are nicer to look at but also take longer to generate and load, and will take up more space on Dropbox. 

##### Decklist
`usage: main.py decklist [-h] [-o OUT] [-s SIZE] file`

*"Create a TTS deck for the provided decklist file"*

The `file` argument should be used to specify the path to the decklist file. The path can be either relative to the Scryfall Tools folder, or absolute.

```bash
# Generate a JSON file from a file named 'The Pile'..

# ..saved on Dave's desktop
>>> python main.py decklist 'C:/Users/Dave/Desktop/The Pile.txt'

# ..saved inside the Scryfall Tools folder
>>> python main.py decklist 'The Pile.txt'
```

##### Draft / Sealed
`usage: main.py draft [-h] [-o OUT] [-s SIZE] code`

*"Create a TTS deck for a draft pool from the provided set"*

`usage: main.py sealed [-h] [-o OUT] [-s SIZE] code`

*"Create a TTS deck for a sealed pool from the provided set"*

The `code` argument should be used to specify the 3 letter code of the set for which you want to create a limited pool.

```bash
# Create a draft pool for the Ikoria set
>>> python main.py draft iko

# Create a sealed pool for Core set 2019
>>> python main.py sealed m19
```

##### Random Commander
`usage: main.py random_commander [-h] [-o OUT] [-s SIZE] [query [query...]]`

*"Create a TTS deck for a random EDH commander"*

Any additional arguments you pass add query specifiers to get your random commander. (*) (**)

```bash
# Generate a commander deck with a commander that..

# ..has 'instant' and/or 'sorcery' in its oracle text. 
>>> python main.py random_commander o:instant OR o:sorcery

# ..has at least Green and Blue in its color identity
>>> python main.py random_commander 'id>=gu'

# ..costs less than 0.05 tix on MTGO
>>> python main.py random_commander 'tix<0.05'
```

\* When using query arguments that contain 

\*\* See [Scryfall](https://scryfall.com/docs/syntax) for a full syntax guide.

## Bugs, issues, suggestions
If you encounter any bugs/issues/suggestions, [create an issue](https://github.com/NCMulder/MTG_Scripts/issues).

## Credit
Thanks to [Marcanius](https://github.com/Marcanius) for adding printing preference functionality and enforcing a clear code standard.
