__author__ = 'ivan'
import matplotlib.pyplot as plt
import MySQLdb
from pylab import *

db = MySQLdb.connect(host="localhost", user="root", passwd="ir", db="water_metrics")
#creating a cursor to execute queries
cur = db.cursor()

cur.execute("SELECT DAILY_TOTAL_FLOW, FLOW_DATE FROM daily_flow")
result = cur.fetchall() #Obtaining all the result
#cur.execute("SELECT FLOW_DATE FROM daily_flow")
#date = cur.fetchall() #Obtaining all the result
t = []
s = []

for record in result:
  t.append(record[0])
  s.append(record[1])

plt.scatter(s, t, marker='*')
plt.ylim([0, 45000])
plt.show()

#plot(t, s, 'ko')
#axis([min(t), max(t), min(s), max(s)])
#grid(True)
#
#F = gcf()
#DPI = F.get_dpi()
#F.savefig('plot.png',dpi = 80)
