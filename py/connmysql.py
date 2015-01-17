#coding=utf-8

import MySQLdb
conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='root',db='mytest')

cur=conn.cursor()
n=cur.execute('select * from user')
r=cur.fetchall()
print r

cur.close()
conn.close()
