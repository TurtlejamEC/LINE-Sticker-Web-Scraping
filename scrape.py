import sys
import requests
from bs4 import BeautifulSoup
import json
import urllib.request
import certifi

url = sys.argv[1]
url = "https://store.line.me/stickershop/product/14611718/en"
req = requests.get(url)
content = req.text

soup = BeautifulSoup(content, features="html.parser")
sticker_elements = soup.find_all("li", {"class": "FnStickerPreviewItem"})

for index, sticker_element in enumerate(sticker_elements):
    animation_url = json.loads(sticker_element["data-preview"])["animationUrl"]
    file_name = str(index) + ".png"

    with urllib.request.urlopen(animation_url, cafile=certifi.where()) as data, open(file_name, "wb") as output:
        data = data.read()
        output.write(data)