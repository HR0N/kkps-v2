from db.db import create_connection


def update_last_order(order):
    connection = create_connection()
    cursor = connection.cursor()
    last_order = str(order)
    sql_query = (
        "UPDATE `last_order` SET `last_order`='"+last_order+"' WHERE id=1")
    cursor.execute(sql_query)
    records = cursor.fetchall()
    cursor.close()


def get_last_order():
    connection = create_connection()
    cursor = connection.cursor()
    sql_query = (
        "SELECT `last_order` FROM `last_order` WHERE id=1")
    cursor.execute(sql_query)
    record = cursor.fetchone()
    cursor.close()
    return record

