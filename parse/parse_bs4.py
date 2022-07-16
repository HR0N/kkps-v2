from parse.parse_categories import fetch_categories
from db.insert_categories import insert_categories
from db.insert_categories import insert_categories_sub1
from db.insert_categories import insert_categories_sub2

state = ''


def fill_categories():
    global state
    state = fetch_categories()

    for category in state['categories']:
        insert_categories(category)
    for category in state['sub-categories-1']:
        for sub_category in state['sub-categories-1'][category]:
            insert_categories_sub1(sub_category, category)
    for category in state['sub-categories-2']:
        for sub_category in state['sub-categories-2'][category]:
            insert_categories_sub2(sub_category, category)

    # print(state['categories'])
    # print(state['sub-categories-1'])
    # print(state['sub-categories-2'])


def parse_orders():
    print(2)

