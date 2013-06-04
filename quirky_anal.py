import time
import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.quirky.com/products/1/timeline")
soup = BeautifulSoup(r.text)

timeline = soup.find(class_="horizontal ui timeline eight events")

print("\n ****** Quirky Analysis ***** \n")

for event in timeline.find_all(class_="event"):
	#print(event.div)
	print(event.find(class_="name").text)
	#print(event['data-title'])
	date = event['data-status'].replace('Completed: ','').replace(',','')
	print(date)
	date2 = time.strptime(date, "%b %d %Y")
	print(date2)
	print("\n------------------------------------------------\n")


