from db.db import create_connection


def get_current_order(category):
    connection = create_connection()
    cursor = connection.cursor()
    sql_query = (
        "INSERT INTO `categories`(`category`) VALUES (\'"+category+"\')")
    cursor.execute(sql_query)
    records = cursor.fetchall()
    cursor.close()

