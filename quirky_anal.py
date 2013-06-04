import time
import requests
import re
from bs4 import BeautifulSoup

for x in range(1,6):
	URL = "http://www.quirky.com/products/%d/timeline" % (x)
	r = requests.get(URL)
	soup = BeautifulSoup(r.text)

	print("\n ****** Quirky Analysis - %d ***** \n") % (x)

	
	title = soup.head.title
	titleText = title.text.replace(' Timeline | Quirky','')
	print(titleText)

	timeline = soup.find(class_="timeline")

	for event in timeline.find_all(class_="event"):
		#print(event.div)
		print(event.find(class_="name").text)
		#print(event['data-title'])
		date = event['data-status'].replace('Completed: ','').replace(',','')
		print(date)
		date2 = time.strptime(date, "%b %d %Y")
		#print(date2)
		#print("\n------------------------------------------------\n")


