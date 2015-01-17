import MySQLdb
conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='root',db='mytest')
print conn
conn.close()



fn="MF65+_AUTO_HSPA_IPV4&v6.csv"
fr=open(fn,'rb+')
print fr.readline()
field=fr.readline()
print field

creat="CREATE TABLE `testss` (`id` INT(11) NOT NULL AUTO_INCREMENT,`name` VARCHAR(50) NULL DEFAULT '0',	PRIMARY KEY (`id`))"

conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='root',db='mytest')
print conn
cur=conn.cursor()
n=cur.execute(create)
conn.
conn.close()

field=field.strip('\n\r')
print field
print '\n'
flist=field.split(',')
print flist
fr.close()
