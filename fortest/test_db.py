# import mysql.connector
# cnx = mysql.connector.connect(user='root',password='123321',host='127.0.0.1',database='test')
# cur = cnx.cursor()
# cur.execute('select * from user')
# print cur.fetchall()

import MySQLdb
conn = MySQLdb.connect(host="127.0.0.1",
                       port=3306,
                       user='root',
                       passwd='123321',
                       db='test')
cursor = conn.cursor()
cursor.fetchone()

cursor.close()
conn.close()