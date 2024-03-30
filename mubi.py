import requests
from bs4 import BeautifulSoup
import json

links = []

def get_links(page):
    url = f'https://mubi.pt/page/{page}/'
    response = requests.get(url)
    if response.status_code == 404:
        global done
        done = True
        return
    soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.findAll('a', {'class': 'continue_reading_link'}):
        links.append(link.get('href'))

page = 1
done = False

while not done:
    get_links(page)
    page += 1

with open('links.json', 'w', encoding='utf-8') as f:
    json.dump(links, f, ensure_ascii=False, indent=4)


def get_article(article_url):
    response = requests.get(article_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('h1', {'class': 'entry-title'}).text
    date = soup.find('span', {'class': 'date time published'})['title']
    categories = soup.findAll('a', {'rel': 'category tag'})
    categories = [category.text for category in categories]
    content = soup.find('div', {'class': 'entry_content'}).text
    return {'title': title, 'date': date, 'categories': categories, 'content': content}

articles = {}

for link in links:
    articles[link] = get_article(link)

with open('articles.json', 'w', encoding='utf-8') as f:
    json.dump(articles, f, ensure_ascii=False, indent=4)
