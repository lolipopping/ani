#! /usr/bin/env python3
import os, webbrowser, requests, cfscrape, array, base64
from bs4 import BeautifulSoup

#get url
url = input("url :")
r = requests.get(url)

#get past cloudflare
scraper = cfscrape.create_scraper()
seriesurl = scraper.get(url)

soup = BeautifulSoup(seriesurl.content, "html5lib")

#prints all html
#print (soup.prettify())

#makes empty array
linklist = []

i = 0
#print all links title and add link itself to array
for link in soup.find_all("a"):
    if str(link.get("title")).find("online in high quality") >= 0:
        short = str(link.get("title"))[12:len(str(link.get("title")))-23]
        print ("(", i, ") ", short)
        linklist.append(link.get("href"))
        i += 1

while True:
    #get episode number
    ep = input("ep :")

    #get past cloudflare and go to ep page
    epurl = scraper.get("https://kissanime.com" + str(linklist[int(ep)]))

    soup = BeautifulSoup(epurl.content, "html5lib")

    #array to hold videos
    video = []

    #get base64 code episodes inside selectQuality and store into array
    for link in soup.find(id="selectQuality").find_all("option"):
        video.append((link.get("value")))

    #select quality
    #q = input("quality :")

    #watch highest quality video
    #decode base 64
    play = base64.b64decode(str(video[0]))
    #encode to utf8
    play = play.decode('utf8')
    
    os.system("mpv " + play)

