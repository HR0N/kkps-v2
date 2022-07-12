from bs4 import BeautifulSoup
import requests

state = {
    'url-categories': 'https://kiev.kabanchik.ua/all-categories',
    'headers': {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                              '(KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
}


def get_categories():
    response = requests.get(state['url-categories'], headers=state['headers'])
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('h2', class_='CategoryName__textSizeH1--3CXRM')
    print(items)

