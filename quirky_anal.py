import time
import requests
import re
from bs4 import BeautifulSoup

redirectTitle = "Inventions | Submit, Vote & Collaborate at Quirky"
homeTitle = "Quirky Makes Invention Accessible"
emptyStr = ""

for x in range(653,661):
	URL = "http://www.quirky.com/products/%d/timeline" % (x)
	r = requests.get(URL)
	soup = BeautifulSoup(r.text)

	print("\n ****** Quirky Analysis - %d ***** \n") % (x)

	title = soup.head.title
	titleText = title.text.replace(' Timeline | Quirky','')
	
	if (titleText != redirectTitle) and (titleText != homeTitle):
		print(titleText)
		timeline = soup.find(class_="timeline")
		for event in timeline.find_all(class_="event"):
			print(event.find(class_="name").text)
			#print(event['data-title'])
			date = event['data-status'].replace('Completed: ','').replace(',','')
			if date != emptyStr:
				print(date)
				date2 = time.strptime(date, "%b %d %Y")
			else:
				print("ERROR - no date found")
			#print(date2)
			#print("\n------------------------------------------------\n")
	else:
		print("\n ----- End of Products - %d Found----- \n") % (x)
		break


