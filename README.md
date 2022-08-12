# LINE-Sticker-Web-Scraping
Download static and animated LINE stickers and resize them

What this does:
 - Gets LINE sticker files (without alteration)
 - Gets animated LINE stickers and converts them to GIF files.

To do:
 - Resize files

## How to Use (Docker, easiest method imo):

Run the following command below in the directory you want to put the stickers in:

```docker run -v ${pwd}:/usr/src/app -it --rm ghcr.io/turtlejamec/line-sticker-web-scraping:master URL PERCENT_SIZE```

The above is for Windows Powershell. If on Unix, use `$(pwd)` instead of `${pwd}`.

For example:

```docker run -v ${pwd}:/usr/src/app -it --rm ghcr.io/turtlejamec/line-sticker-web-scraping:master https://store.line.me/stickershop/product/14611718/en 50```

## How to Use (Install dependencies and run Python file):

Install the dependencies in requirements.txt (ex. with pip + venv). After that, run scrape.py like so:

```python .\scrape.py URL PERCENT_SIZE```

The above is for Windows Powershell. If on Unix, use `scrape.py` instead of `.\scrape.py`

For example:

```python .\scrape.py https://store.line.me/stickershop/product/14611718/en 50```
