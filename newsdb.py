# Database code for the DB Forum, full solution!

#import psycopg2, bleach
import psycopg2
from datetime import datetime
import re

DBNAME = "news"
cmd1 = "select title,cnt from slugname,slugcnt \
where slugname.slug=slugcnt.substring limit 3"
cmd2 = "select name,sum(cnt) from slugname,slugcnt \
where slugname.slug=slugcnt.substring group by name order by sum desc"
cmd3 = "select date,result from httpratio where result > 1"

def get_posts():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("{}".format(cmd1))
  rows = c.fetchall()
  db.close()
  print('\n')
  print("==== Top 3 most viewed Title ====")
  for row in rows:
     print("{} - {} views".format(row[0],row[1]))


def get_auth():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("{}".format(cmd2))
  rows = c.fetchall()
  db.close()
  print('\n')
  print("==== Top viewed Authors ====")
  for row in rows:
     print("{} - {} views".format(row[0],row[1]))

def get_ratio():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("{}".format(cmd3))
  rows = c.fetchall()
  db.close()
  print('\n')
  print("==== HTTP Miss Ratio > 1% in one day ====")
  for row in rows:
     x = re.split('-',row[0])
     y = datetime(int(x[0]),int(x[1]),int(x[2]))
     z = y.strftime('%B %d, %Y')
     q="{0:.2f}%".format(row[1])
     print(z +" - " +q +" errors")

if __name__=="__main__":
  get_posts()
  get_auth()
  get_ratio()
