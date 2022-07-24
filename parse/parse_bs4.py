import json

from parse.parse_orders import parse_circle
from parse.parse_categories import fetch_categories
from db.insert_categories import insert_categories_new
# from db.insert_categories import insert_categories
# from db.insert_categories import insert_categories2
# from db.insert_categories import insert_categories_sub1
# from db.insert_categories import insert_categories_sub2


def fill_categories():
    categories = fetch_categories()
    insert_categories_new(categories)
    # for category in state['categories']:
    #     insert_categories(category)
    # for category in state['sub-categories-1']:
    #     for sub_category in state['sub-categories-1'][category]:
    #         insert_categories2(sub_category, category)
    # for category in state['sub-categories-2']:
    #     for sub_category in state['sub-categories-2'][category]:
    #         insert_categories2(sub_category, category)


def parse_orders():
    parse_circle()

