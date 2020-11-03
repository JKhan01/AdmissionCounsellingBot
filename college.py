from bs4 import BeautifulSoup
import requests
import csv
csv_file = open('cms_scrape1.csv', 'w')
csv_writer = csv.writer(csv_file)


source = requests.get('https://www.teachuseducation.com/maharashtra-board/Mumbai/Science/').text

soup = BeautifulSoup(source, 'lxml')
i=0
for row in soup.find_all('td', class_='two_col'):
    college = row.find('b')
    a=college.text
    print(a)
    csv_writer.writerow([a,'','Mumbai','Science'])

for row in soup.find_all('td', class_='three_col'):
    i=i+1
    if i%2 == 0:
        college = row.find('b')
        b=college.text
        print(b)
        csv_writer.writerow([' ',b])
       
    

csv_file.close()

    




    


'''csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    print(yt_link)

    print()

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()'''
