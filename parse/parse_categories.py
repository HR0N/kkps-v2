from bs4 import BeautifulSoup
import requests
import json

state = {
    'url-categories': 'https://kiev.kabanchik.ua/all-categories',
    'headers': {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                              '(KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'},
}
categories = {}
response = requests.get(state['url-categories'], headers=state['headers'])
soup = BeautifulSoup(response.content, 'html.parser')


#                                   ..:: Main Functions ::..


def fetch_categories():
    components = soup.findAll('div', class_='ek-grid_indent_s')

    return get_categories(components)  # get categories

#                                   ..:: Sub Functions ::..


def get_categories(components):
    global categories
    prev_category = ''
    for component in components:
        try:
            category1 = component.find('h2', class_='CategoryName__textSizeH1--3CXRM').get_text(strip=True)\
                .replace("'", '')  # try 1
            sub_categories_ul = component.find('ul', class_='CategoryTree__childrenList--33TNh')
            sub_categories_list = sub_categories_ul\
                .findAll('li', class_='CategoryTree__childrenItemIncreasedIndent--3NkFW', recursive=False)
            categories[category1] = {}
            for sub_cat in sub_categories_list:
                category2 = sub_cat.find('span', class_='CategoryName__textSizeDefault--1Tq00').get_text(strip=True)\
                    .replace("'", '')
                if 'CategoryTree__childrenItemTypeNestedIncreasedIndent--a7LfT' in sub_cat.attrs['class']:
                    categories[category1][prev_category] = []
                    sub_categories_list2 = sub_cat.findAll('li',
                                                           class_='CategoryTree__childrenItemIncreasedIndent--3NkFW')\
                        .replace("'", '')
                    for sub_cat2 in sub_categories_list2:
                        category3 = sub_cat2.get_text(strip=True)
                        categories[category1][prev_category].append(category3)
                else:
                    categories[category1][category2] = False
                    prev_category = category2.replace("'", '')
        except AttributeError:
            print('error: get_categories() - try 1', AttributeError)
    return categories


# def get_categories(components):
#     for component in components:
#         try:
#             category = component.find('h2', class_='CategoryName__textSizeH1--3CXRM').get_text(strip=True)
#
#             state['categories'].append(category)
#             state['sub-categories-1'][category] = []
#             get_sub_categories_1(component, category)  # get sub categories 1
#         except AttributeError:
#             print('error: get_categories() ', AttributeError)
#
#
# def get_sub_categories_1(component, category):
#     sub_category_list = []
#     last_sub_category = ''
#     sub_categories = component.findAll('li', class_='CategoryTree__childrenItemIncreasedIndent--3NkFW')
#     try:
#         for sub_category in sub_categories:
#             sub_cat_a = sub_category.find('a', class_='CategoryName__link--26-fs')
#             sub_cat_ul = sub_category.find('ul', class_='CategoryTree__childrenList--33TNh')
#             if sub_cat_ul:
#                 state['sub-categories-2'][last_sub_category] = []
#                 get_sub_categories_2(sub_cat_ul, last_sub_category)  # get sub categories 2
#             if sub_cat_a:
#                 state['sub-categories-1'][category].append(sub_cat_a.get_text(strip=True))
#                 sub_category_list.append(sub_cat_a.get_text(strip=True))
#                 last_sub_category = sub_cat_a.get_text(strip=True)
#     except AttributeError:
#         print('error: get_sub_categories_1() ', AttributeError)
#
#
# def get_sub_categories_2(sub_category_1, last_category):
#     try:
#         for sub_category in sub_category_1:
#             sub_cat_2 = sub_category.find('span', class_='CategoryName__textSizeDefault--1Tq00')
#             state['sub-categories-2'][last_category].append(sub_cat_2.get_text(strip=True))
#     except AttributeError:
#         print('error: get_sub_categories_2() ', AttributeError)

