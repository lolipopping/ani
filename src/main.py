import cfscrape
from anistream import stream

scraper = cfscrape.create_scraper()
while True:
    url = input("url :")
    stream(scraper, url)

