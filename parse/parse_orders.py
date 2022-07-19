from bs4 import BeautifulSoup
import requests

state = {
    'url-order': 'https://kabanchik.ua/task/',
    'headers': {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                              '(KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'},
}
# response = requests.get(state['url-categories'], headers=state['headers'])
# soup = BeautifulSoup(response.content, 'html.parser')

current_order = 3054900
current_order_plus = 0
link = f"{state['url-order']}{current_order}"


def check_page():
    response = requests.get(link, headers=state['headers'])
    soup = BeautifulSoup(response.content, 'html.parser')

    print(link)
    print(check_404(soup))


def check_404(page):  # return True if this not 404 page, return False if this 404 page
    return not page.find('h1', class_='kb-error-page__title')


def check_promo(page):  # return True if this not promo page, return False if this promo page
    return not page.find('div', class_='kb-promotion')


