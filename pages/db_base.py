
import mysql.connector as mysql


db = mysql.connect(host="127.0.0.1",
                    user="root",
                    passwd="",
                    database='litecart')
cursor = db.cursor()

query = 'SELECT name, sku, quantity, price FROM lc_orders_items WHERE id = 19 '
cursor.execute(query)
print(cursor.fetchall())
