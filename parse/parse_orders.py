from bs4 import BeautifulSoup
from db.parse_orders_db import update_last_order
from db.parse_orders_db import get_last_order
import requests
import random
import time

state = {
    'url-order': 'https://kabanchik.ua/task/',
    'headers': {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                              '(KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'},
}

last_order = 0
current_order_plus = 0
rand = random.randint(10, 15)


def parse_circle():     # actions, we repeat every circle (10-15sec random)
    global last_order
    last_order = get_last_order()[0]
    link = f"{state['url-order']}{last_order}"
    response = requests.get(link, headers=state['headers'])
    soup = BeautifulSoup(response.content, 'html.parser')
    # while True:
    #     time.sleep(rand)
    #     if check_page(soup):    # check is page has any problem: yes it has - return False; hasn't - True
    #         parse_page(soup)
    print(parse_page(soup))


def check_page(soup):   # check is page has any problem: yes it has - return False; hasn't - True
    if check_404(soup) and check_promo(soup):
        return True
    else:
        return False


def check_404(page):    # return True if this not 404 page, return False if this 404 page
    return not page.find('h1', class_='kb-error-page__title')


def check_promo(page):  # return True if this not promo page, return False if this promo page
    return not page.find('div', class_='kb-promotion')


def parse_page(page):   # parsing the page
    data = {}
    try:
        title = item_find(page, 'h1', 'kb-task-details__title')
        price = item_find(page, 'span', 'js-task-cost')
        was_created = item_find(page, 'div', 'kb-sidebar-grid__content')
        deadline = item_find(page, 'span', 'js-datetime_due')
        tasks = item_find_all(page, 'div', 'kb-task-details__non-numeric-attribute')
        comment = item_find_all(page, 'div', 'kb-task-details__content')
        client = item_find(page, 'a', 'kb-sidebar-profile__name')
        review = item_find(page, 'span', 'kb-sidebar-profile__reviews-count')
        positive = item_find(page, 'div', 'kb-sidebar-profile__rating')

        if title != 'empty for some reason (o.O)':
            data['title'] = title.split('№')[0]
        else:
            data['title'] = title
        if price != 'empty for some reason (o.O)':
            data['price'] = price
        else:
            data['price'] = price
        if was_created != 'empty for some reason (o.O)':
            data['was_created'] = was_created
        else:
            data['was_created'] = was_created
        if deadline != 'empty for some reason (o.O)':
            data['deadline'] = deadline
        else:
            data['deadline'] = deadline
        if tasks != 'empty for some reason (o.O)':
            tasks2 = []
            for task in tasks:
                tasks2.append(task.get_text(strip=True))
            data['tasks'] = tasks2
        else:
            data['tasks'] = tasks
        if comment != 'empty for some reason (o.O)':
            data['comment'] = comment[3].get_text(strip=True)
        else:
            data['comment'] = comment
        if client != 'empty for some reason (o.O)':
            data['client'] = client
        else:
            data['client'] = client
        if review != 'empty for some reason (o.O)':
            data['review'] = review
        else:
            data['review'] = review
        if positive != 'empty for some reason (o.O)':
            data['positive'] = positive
        else:
            data['positive'] = positive
        # update_last_order(last_order + 1)
    except AttributeError:
        print('error: parse_orders.parse_page() ', AttributeError)
    return data
# title price was_created deadline tasks comment client review positive


def item_find(page, tag, selector):
    result = 'empty for some reason (o.O)'
    try:
        result = page.find(tag, class_=selector).get_text(strip=True)
    except AttributeError:
        print('error: parse_orders.item_find() ', AttributeError)
    return result


def item_find_all(page, tag, selector):
    result = 'empty for some reason (o.O)'
    try:
        result = page.findAll(tag, class_=selector)
    except AttributeError:
        print('error: parse_orders.item_find_all() ', AttributeError)
    return result

