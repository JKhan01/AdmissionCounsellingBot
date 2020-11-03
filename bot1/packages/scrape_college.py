from bs4 import BeautifulSoup
import requests
import csv

stream=input()
location=input()
url='https://collegedunia.com/'+stream+'//'+location+'-colleges'
source = requests.get(url).text
soup= BeautifulSoup(source,'lxml')
i=0
for article in soup.find_all('div',class_='clg-name-address'):
	link=article.a
	print(article.h3.text)
	print()
	i=i+1
	if i==5:
		break

