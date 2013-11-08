import sqlite3 as lite
import sys
con=lite.connect("blog.db")
with con:
	cur=con.cursor()
	cur.execute("DROP TABLE IF EXISTS posts")
	cur.execute("CREATE TABLE posts(id integer primary key autoincrement,title TEXT,text INT)")

