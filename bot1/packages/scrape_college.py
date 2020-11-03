from bs4 import BeautifulSoup
import requests
import csv

class CollegeScrape:

	def __init__ (self,stream,location):
		self.stream = stream
		self.location = location
		
	def fetch_list(self):
		url='https://collegedunia.com/'+self.stream+'//'+self.location+'-colleges'
		source = requests.get(url).text
		soup= BeautifulSoup(source,'lxml')
		i=0
		collegeDict = []
		for article in soup.find_all('div',class_='clg-name-address'):
			link = article.a
			collegeDict[article.h3.text] = link
			i=i+1
			if i==5:
				break
		
		return collegeDict

