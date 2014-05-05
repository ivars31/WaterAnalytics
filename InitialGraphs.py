__author__ = 'ivan'
import matplotlib as m
import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="ir", db="water_metrics")
cur = db.cursor() #creating a cursor to execute queries
cur.execute("SELECT * FROM daily_flow")
