# Nielsch's MTG Scripts
This is a collection of scripts I've been creating for Magic: The Gathering related tasks.

## Tabletop Simulator Deck Generator
The bulk of the useful scripts are located in the [Scryfall Tools](Scryfall%20Tools) subfolder. I really should work on restructuring this whole thing but that's what you'll get for now.
This tool takes a decklist, generates and uploads the card images to your Dropbox, and creates a `.json` that Tabletop Simulator can read to import your deck.

#### Setup
First of all, if you want to run these scripts, you should get a [Dropbox API key](https://blogs.dropbox.com/developers/2014/05/generate-an-access-token-for-your-own-account/) by creating an app choosing the Dropbox API, choosing "App Folder", and naming your app. Get your personal API key under `<appname> -> Settings -> OAuth2 -> Generated access token`, copy the `config_default.ini` file, rename it to `config.ini` and place your API key in there.
Now, the uploader should be functional.

#### Functionality
The main entry point for all functionality is `main.py`; `cd` into the Scryfall Tools folder and run `python main.py` from a command line with your favorite arguments.
Several modes can be specified with `-mode`:

| Argument | Description |
| -------- | ----------- |
| `random-commander` | Grabs a random commander from Scryfall and gets the average decklist from EDHRec. The default mode. |
| `decklist` | Gets a decklist from the specified location. Specify this location with the `-dl` argument.|
| `sealed_pool` | Gets (a) sealed pool(s) from a specified set. WIP. |
| `draft_packs` | Gets (a) draft pack(s) from a specified set. WIP. |

The `-out` argument can be specified to point the `.json` file somewhere (maybe your TTS saved objects folder).

The `-q` argument can be used to specify a card image size. Supported arguments are `png`, `border_crop`, `art_crop`, `large`, `normal` and `small`; larger sizes are nicer to look at but also take longer to generate and load, and will take up more space on Dropbox. Defaults to `normal` (488 by 680px).

All other arguments are assumed to be extra query specifiers to get your random commander. For example, `python main.py "o:instant OR o:sorcery"` gets a random commander with *instant* and/or *sorcery* in its oracle text. See [Scryfall](https://scryfall.com/docs/syntax) for a full syntax guide.

## Bugs, issues, suggestions
If you encounter any bugs/issues/suggestions, [create an issue](https://github.com/NCMulder/MTG_Scripts/issues).

## Credit
Thanks to [Marcanius](https://github.com/Marcanius) for adding printing preference functionality and enforcing a clear code standard.