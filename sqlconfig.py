#!/usr/bin/env python
#import pymysql

def connectDb():
	conn = pymysql.connect(host='localhost', user='root', passwd='', db='products')

	curs = conn.cursor()

	return curs, conn

def sqlSelect(curs, sql_str, sql_args = None):
    if sql_args != None:
        curs.execute(sql_str % sql_args)
    else:
        curs.execute(sql_str)
    list = curs.fetchall()
    return list

def closeConn(curs,conn):
	curs.close()
	conn.close()

insert = """
INSERT INTO `headphoneslist` (`ID`, `Title`, `LinkCell`, `PriceCell`, `LinkEmag`, `PriceEmag`) 
VALUES (NULL, '%s', '%s', '%s', '%s', '%s')
"""
