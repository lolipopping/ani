import os, webbrowser, requests, cfscrape, array, base64
from bs4 import BeautifulSoup

#function input scraper from cfscrape, series url
#asks user episode number launches mpv 
#no output
def stream(scraper, url):
	try:
		series = scraper.get(url)
	except:
		print("url error")
		return
	soup = BeautifulSoup(series.content, "html5lib")
	#eplist stores the url for all episodes
	eplist = []
	#titlelist stores all the titles of the episodes
	titlelist = []
	i = 0
	#stores all episode url into eplist
	#stores all titles into titlelist newest first
	for link in soup.find_all("a"):
		if str(link.get("title")).find("online in high quality") >= 0:
			short = str(link.get("title"))[12:len(str(link.get("title")))-23]
			tmp = "(" + str(i) + ") " + short
			titlelist.insert(0, tmp)
			eplist.append(link.get("href"))
			i += 1
	try:
		#keep asking for ep number and playing 
		#^C exits ep loop into url loop
		while True:
			for title in titlelist:
				print (title)
			ep = input("ep :")
			try:
				epurl = scraper.get("https://kissanime.com" + str(eplist[int(ep)]))
			except:
				print("ep number error")
				return
			soup = BeautifulSoup(epurl.content, "html5lib")
			#array to hold videos url
			video = []
			#video contains video url from 0 with best quality to n with worst quality
			for link in soup.find(id="selectQuality").find_all("option"):
				video.append((link.get("value")))
			play = base64.b64decode(str(video[0]))
			play = play.decode('utf8')
			launch = "mpv " + "\"" + play + "\""
			os.system(launch)
	except KeyboardInterrupt:
		print("")
