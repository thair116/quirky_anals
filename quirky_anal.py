import time
import requests
import MySQLdb as mdb
import sys
from bs4 import BeautifulSoup

redirectTitle = "Inventions | Submit, Vote & Collaborate at Quirky"
homeTitle = "Quirky Makes Invention Accessible"
emptyStr = ""


con = mdb.connect('localhost', 'testuser', 'test623', 'testdb');


cur = con.cursor()
#cur.execute("DROP TABLE IF EXISTS Quirky_data")
#cur.execute("CREATE TABLE Quirky_data(Id INT PRIMARY KEY AUTO_INCREMENT, \
 #            Name VARCHAR(25), Stage VARCHAR(25), _DATE DATE)")

for x in range(194,700):
	URL = "http://www.quirky.com/products/%d/timeline" % (x)
	r = requests.get(URL)
	soup = BeautifulSoup(r.text)

	

	title = soup.head.title
	titleText = title.text.replace(' Timeline | Quirky','')
	
	if (titleText != redirectTitle) and (titleText != homeTitle):
		
		
		#print(titleText)
		timeline = soup.find(class_="timeline")
		for event in timeline.find_all(class_="event"):
			stage = event.find(class_="name").text
			#print(stage)
			#print(event['data-title'])
			dateStr = event['data-status'].replace('Completed: ','').replace(',','').replace('In Judgment: ','')
			if dateStr != emptyStr:
				#print(dateStr)
				date_object = time.strptime(dateStr, "%b %d %Y")
				#print(date_object.tm_year)
				date_sql = "%d-%d-%d" % (date_object.tm_year, date_object.tm_mon, date_object.tm_mday)
				cur.execute("INSERT INTO Quirky_data(Name, Stage, _Date) VALUES(%s, %s, %s)",(titleText, stage, date_sql))
			else:
				cur.execute("INSERT INTO Quirky_data(Name, Stage) VALUES(%s, %s)",(titleText, stage))
				print("ERROR - no date found")
			#print(date2)
			#print("\n------------------------------------------------\n")
	else:
		print("\n ----- End of Products - %d Found----- \n") % (x)
		break

	con.commit()
	print("\n ****** Quirky Analysis - %d Done ***** \n") % (x)

con.close()

