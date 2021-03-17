
import mysql.connector as mysql

db = mysql.connect(host="127.0.0.1",
                    user="root",
                    passwd="",
                    database='litecart')
cursor = db.cursor()
# cursor.execute("SHOW DATABASES")
# print(cursor.fetchall())
# cursor.execute("SHOW TABLES")
# print(cursor.fetchall())
# cursor.execute("SELECT * FROM lc_order_statuses_info")
# print(cursor.fetchall())
# cursor.execute("SELECT * FROM lc_orders")
# print(cursor.fetchall())
# cursor.execute("SELECT * FROM lc_order_statuses")
# print(cursor.fetchall())
