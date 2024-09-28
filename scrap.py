from bs4 import BeautifulSoup
import requests
import csv
from transformers import pipeline

# def convertStr(cookie_str):
#     cookies = {}
#     for key_val in cookie_str:
#         temp = key_val.split(':')
#         key = ''.join(temp[0].split())
#         value = temp[1]
#         cookies[key] = value
#     return cookies
summarizer = pipeline("summarization")
csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary'])

url = 'https://en.wikipedia.org/wiki/Technology'

source = requests.get(url).text
# print(source)
soup = BeautifulSoup(source, 'lxml')

content = soup.find('main', id= 'content')

heading = content.find('h1', id = 'firstHeading')

body = content.find('div', id='bodyContent')
subheads = body.find_all('h2')
subtopic = []
str = ''
for head in subheads:
    if(head.text == 'References'):
        break
    else:
        for par in head.find_previous('p'):
            str += par.text
        subtopic.append(str);
        str = ''
        str += head.text
        str += '\n'
summary_list = []
for topic in subtopic:
     summary_list.append(summarizer(topic, max_length=50, min_length=10, do_sample=False));


summary = ''
for _ in summary_list:
    summary += _[0]['summary_text']

print(summary)
csv_writer.writerow([heading.text,summary])

csv_file.close()