from bs4 import BeautifulSoup
import requests


def getFlights():
    url = 'https://kiev.kabanchik.ua/all-categories'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/95.0.4638.69 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    # items = soup.find('div', class_='DailyForecast--DisclosureList--msYIJ')
    # items = items.findAll('details', class_='Disclosure--themeList--25Q0H')