
import mysql.connector as mysql

db = mysql.connect(host="127.0.0.1",
                    user="root",
                    passwd="",
                    database='litecart')
cursor = db.cursor()


class DataBase():

    def should_be_order_in_db(self):
        query = 'SELECT name, sku, quantity, price FROM lc_orders_items WHERE id = 19 '
        cursor.execute(query)
        print(cursor.fetchall())
    # assert check_quantity_duck_text == check_quantity, f'Text on UI {check_quantity_duck_text} is not eq {check_quantity}'


