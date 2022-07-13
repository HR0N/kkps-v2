from db.db import create_connection


def insert_categories(category):
    connection = create_connection()
    cursor = connection.cursor()
    category = rm_quotes(category)
    sql_query = (
        "INSERT INTO `categories`(`category`) VALUES (\'"+category+"\')")
    cursor.execute(sql_query)
    cursor.close()


def insert_categories_sub1(sub_category, p_category):
    connection = create_connection()
    cursor = connection.cursor()
    sub_category = rm_quotes(sub_category)
    p_category = rm_quotes(p_category)
    sql_query = (
        "INSERT INTO `categories_sub_1`(`category`, `parent_category`) "
        "VALUES (\'"+sub_category+"\', \'"+p_category+"\')")
    cursor.execute(sql_query)
    cursor.close()


def insert_categories_sub2(sub_category, p_category):
    connection = create_connection()
    cursor = connection.cursor()
    sub_category = rm_quotes(sub_category)
    p_category = rm_quotes(p_category)
    sql_query = (
        "INSERT INTO `categories_sub_2`(`category`, `parent_category`) "
        "VALUES (\'"+sub_category+"\', \'"+p_category+"\')")
    cursor.execute(sql_query)
    cursor.close()


def rm_quotes(string):
    result = string.replace('"', '')
    result = result.replace("'", "")
    result = result.strip('\"')
    result = result.lstrip('\"')
    result = result.rstrip('\"')
    result = result.strip("\'")
    result = result.lstrip("\'")
    result = result.rstrip("\'")
    return result
