import sys
import requests
from bs4 import BeautifulSoup
import json
import urllib.request
import certifi
from PIL import Image

# Get html
url = sys.argv[1]
req = requests.get(url)
content = req.text

# Get elements that contain stickers
soup = BeautifulSoup(content, features="html.parser")
sticker_elements = soup.find_all("li", {"class": "FnStickerPreviewItem"})


for index, sticker_element in enumerate(sticker_elements):
    # Get url of sticker
    animation_url = json.loads(sticker_element["data-preview"])["animationUrl"]
    file_name = str(index) + ".png"

    # Download sticker
    with urllib.request.urlopen(animation_url, cafile=certifi.where()) as data, open(file_name, "wb") as output:
        data = data.read()
        output.write(data)
    
    # Make sticker loop
    apng = Image.open(file_name)
    apng.format = "apng"
    apng.info["default_image"] = True

    if apng.mode != 'RGBA':
      apng = apng.convert("RGBA")

    file_name = str(index) + ".gif"
    apng.save(file_name, loop=0, disposal=2, save_all=True)