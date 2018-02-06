#!/usr/bin/python3
#coding:utf-8

import cgi
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb as sql

data = cgi.FieldStorage()
if data.__contains__('userTime'):
    value = data['userTime'].value
else:
    value = 'not found'

con = sql.connect(user = 'monitor',passwd = '!QAZxsw2',db = 'monitor',host = '127.0.0.1')
cur = con.cursor()
cur.execute("insert into cpu values(%d,'%s');"%(1,value))
con.commit()
cur.close()
con.close()
