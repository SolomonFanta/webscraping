# getting the html file
from requests import get
url = 'https://www.thepatriot.co.bw/news/item/6917-bdp%E2%80%99s-history-of-banning-critics.html'
response = get(url)

# parsing the html file and creating the BeautifulSoup object
from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# processing
webpage = soup.find_all('p', class_='MsoNormal')

# title
article_title = webpage[0].text

# body
body = ''
# combining all paragraphs to make a body
for para in webpage[1:]:
    body += para.text + '\n\n'

# combining everything to make the article
article = article_title + '\n\n' + body

# writing to a text file
filename = 'patriot_article2.txt'
with open(filename, 'w') as file_obj:
    file_obj.write(article)
