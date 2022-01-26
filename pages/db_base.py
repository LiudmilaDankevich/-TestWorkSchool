import mysql.connector as mysql


class DataBase:
    def __init__(self):
        self.conn = mysql.connect(host="localhost",
                                  user="root",
                                  passwd="",
                                  database="litecart")
        self.conn.is_connected()
    # print('Connected to MySQL')

    def show_tables(self):
        cursor = self.conn.cursor()
        query = "SHOW TABLES"
        cursor.execute(query)
        print(cursor.fetchall())



    def find_order_in_the_base(self):
        cursor = self.conn.cursor()
        cursor.execute("DESC lc_orders")
        print(cursor.fetchall())

    def check_order_by_id(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM lc_orders WHERE id=8"
        cursor.execute(query)
        print(cursor.fetchall())
        # i = cursor.fetchall()
        # print(i)
        # a = "[(19,)]"
        # assert a == cursor.fetchall(), f'Text on UI {a} is not eq {i}'


connect = DataBase()
# connect.show_tables()
# connect.find_order_in_the_base()
connect.check_order_by_id()
# connect.close()
