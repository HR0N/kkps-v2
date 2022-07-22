from bs4 import BeautifulSoup
import requests

state = {
    'url-categories': 'https://kiev.kabanchik.ua/all-categories',
    'headers': {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                              '(KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'},
    'categories': [],
    'sub-categories-1': {},
    'sub-categories-2': {},
}
response = requests.get(state['url-categories'], headers=state['headers'])
soup = BeautifulSoup(response.content, 'html.parser')


#                                   ..:: Main Functions ::..


def fetch_categories():
    components = soup.findAll('div', class_='ek-grid_indent_s')

    get_categories(components)  # get categories
    return state

#                                   ..:: Sub Functions ::..


def get_categories(components):
    for component in components:
        try:
            category = component.find('h2', class_='CategoryName__textSizeH1--3CXRM').get_text(strip=True)

            state['categories'].append(category)
            state['sub-categories-1'][category] = []
            get_sub_categories_1(component, category)  # get sub categories 1
        except AttributeError:
            print('error: get_categories() ', AttributeError)


def get_sub_categories_1(component, category):
    sub_category_list = []
    last_sub_category = ''
    sub_categories = component.findAll('li', class_='CategoryTree__childrenItemIncreasedIndent--3NkFW')
    try:
        for sub_category in sub_categories:
            sub_cat_a = sub_category.find('a', class_='CategoryName__link--26-fs')
            sub_cat_ul = sub_category.find('ul', class_='CategoryTree__childrenList--33TNh')
            if sub_cat_ul:
                state['sub-categories-2'][last_sub_category] = []
                get_sub_categories_2(sub_cat_ul, last_sub_category)  # get sub categories 2
            if sub_cat_a:
                state['sub-categories-1'][category].append(sub_cat_a.get_text(strip=True))
                sub_category_list.append(sub_cat_a.get_text(strip=True))
                last_sub_category = sub_cat_a.get_text(strip=True)
    except AttributeError:
        print('error: get_sub_categories_1() ', AttributeError)


def get_sub_categories_2(sub_category_1, last_category):
    try:
        for sub_category in sub_category_1:
            sub_cat_2 = sub_category.find('span', class_='CategoryName__textSizeDefault--1Tq00')
            state['sub-categories-2'][last_category].append(sub_cat_2.get_text(strip=True))
    except AttributeError:
        print('error: get_sub_categories_2() ', AttributeError)