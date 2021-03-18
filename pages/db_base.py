import mysql.connector as mysql



class DataBase:
    def __init__(self):

        self.conn = mysql.connect(host="127.0.0.1",
                            user="root",
                            passwd="",
                            database='litecart')
        self.conn.is_connected()
        print('Connected to MySQL')

    def find_order_in_the_base(self):
        cursor = self.conn.cursor()
        query = 'SELECT name, sku, quantity, price FROM lc_orders_items WHERE id = 19 '
        cursor.execute(query)
        print(cursor.fetchall())
        # i = str(cursor.fetchall())
        # a = "[('Blue Duck', 'RD004', Decimal('3.0000'), Decimal('20.0000'))]"
        # assert a == str(cursor.fetchall()), f'Text on UI {a} is not eq {i}'




connect = DataBase()
connect.find_order_in_the_base()


# db.close()
