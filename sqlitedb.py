# Reference : http://www.tutorialspoint.com/sqlite/sqlite_python.htm

import sqlite3

conn = sqlite3.connect("testdb.db")                                   #connect DB, if not exist, new DB will be created

conn.execute('''create table stud
 	(roll_no int primary key not null,
 	name varchar(20),
 	father_name varchar(20) not null
 	);''')                                                            #create table

conn.execute("insert into stud values(40, 'rkapoor', 'akapoor');")
conn.execute("insert into stud (father_name, roll_NO,name ) values ('ak', 081,NULL);")
conn.execute("insert into stud (name, FATher_name, roll_NO) values ('ak', 'ak', 0013);")
                                                                      # insert values

cursor = conn.execute('''select * from stud;''')                      # select data
for row in cursor:
  print(row[0], row[1])                                             # only 0th and 1th column to display

cursor = conn.execute("select name from sqlite_master where type = 'table';")
for i in cursor:
	print(i[0])                                                       # get names of tables in current db

conn.execute("delete from stud where roll_NO = 4084;")                # deletion

print(cursor.fetchone())
print(cursor.fetchone())                                             # fetches current row, and point to next

res = cursor.fetchmany(size=5)
for i in res:
	print(i)                                                         # fetches rows depending on size param from current cursor pos

resall = cursor.fetchall()
for i in resall:
	print(i)                                                         # fetches remaining rows from current cursor pos

conn.commit()                                                        # commit to any changes made

print(conn.total_changes)                                            # returns no. of rows inserted, deleted, modified 
                                                                     # since DB connection was open

conn.rollback()                                                      # rollback chnages since last commit()

conn.close()                                                         # close connection