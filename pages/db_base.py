# import mysql.connector as mysql
#
#
#
#
# class DataBase:
#     def __init__(self):
#         self.conn = mysql.connect(host="127.0.0.1",
#                                   user="root",
#                                   passwd="",
#                                   database='test new base')
#         self.conn.is_connected()
#         print('Connected to MySQL')
# #
#     def find_order_in_the_base(self):
#         cursor = self.conn.cursor()
#         query = 'SHOW database'
#         cursor.execute(query)
#         print(cursor.fetchall())
#         i = cursor.fetchall()
#         print(i)
# #         # a = "[(19,)]"
# #         # assert a == cursor.fetchall(), f'Text on UI {a} is not eq {i}'
# #
#
# connect = DataBase()
# connect.find_order_in_the_base()
#
# # # db.close()
