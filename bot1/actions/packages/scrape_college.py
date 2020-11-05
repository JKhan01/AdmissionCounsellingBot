from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

class CollegeScrape:

	def __init__ (self,stream,location, grades):
		self.stream = stream
		self.location = location
		self.grades = grades
		
	def fetch_list_on_location(self):
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

	def fetch_list_on_guidance(self):
		# making data frame from csv file  
		data = pd.read_csv("College.csv") 
		pd.options.display.max_colwidth = 200
		# replacing blank spaces with '_'  
		data.columns =[column.replace(" ", "_") for column in data.columns] 
		print(data.columns)
		print (self.stream.capitalize())
		print (type(self.location))
		print (self.grades)

		# filtering with query method 
		sakshi=data.query(f'Stream == "{self.stream.capitalize()}" and percentage <= {self.grades} and Location =="{self.location.capitalize()}" ') 
		print (sakshi)
		returnString = 'Accordingly here are some colleges' + '\n'
		if sakshi.shape[0] > 5 :
			for i in range(5):
				returnString += str(sakshi[i:i+1].college.values[0]) + '\n'
		
			
		else:
			for i in range(sakshi.shape[0]):
				returnString += str(sakshi[i:i+1].college) + '\n'
		print (returnString)	
		return returnString

