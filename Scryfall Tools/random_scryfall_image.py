import json
import urllib.request
from io import BytesIO

from PIL import Image

randomCard = urllib.request.urlopen(
    'https://api.scryfall.com/cards/random?q=is%3Acommander'
).read()
jsonCard = json.loads(randomCard)

randomImage = urllib.request.urlopen(jsonCard['image_uris']['png']).read()
img = Image.open(BytesIO(randomImage))

img.show()
