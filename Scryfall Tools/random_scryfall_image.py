import urllib.request
import json
from PIL import Image
from io import BytesIO

randomCard = urllib.request.urlopen('https://api.scryfall.com/cards/random?q=is%3Acommander').read()
jsonCard = json.loads(randomCard)

randomImage = urllib.request.urlopen(jsonCard["image_uris"]["png"]).read()
img = Image.open(BytesIO(randomImage))

img.show()

# import matplotlib.pyplot as plt
# imgplot = plt.imshow(img)
# plt.show()
