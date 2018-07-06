#!/usr/bin/env python3

# Database code for the DB Forum, full solution!

import psycopg2
from datetime import datetime
import re

DBNAME = "news"
articles = """
       SELECT title,cnt
       FROM slugname,slugcnt
       WHERE slugname.slug=slugcnt.substring limit 3;
       """
authors = """
       SELECT name,sum(cnt)
       FROM slugname,slugcnt
       WHERE slugname.slug=slugcnt.substring
       GROUP by name
       ORDER by sum desc;
       """
ratio = """
       SELECT date,result
       FROM httpratio
       WHERE result > 1;
       """


def execute_query(query):
    '''
    Take a string query and execute the query.
    Return a list of tuples.
    '''
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute(query)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    rows = c.fetchall()
    db.close()
    return rows


def top_articles():
    rows = execute_query(articles)
    print('\n')
    print("==== Top viewed Authors ====")
    for title, view in rows:
        print("{} - {} views".format(title, view))


def top_authors():
    rows = execute_query(authors)
    print('\n')
    print("==== Top viewed Authors ====")
    for author, view in rows:
        print("{} - {} views".format(author, view))


def miss_ratio():
    rows = execute_query(ratio)
    print('\n')
    print("==== HTTP Miss Ratio > 1% in one day ====")
    for date, missratio in rows:
        print("{0:%B %d, %Y} - {1:.2f}%".format(date, missratio))


if __name__ == "__main__":
    top_articles()
    top_authors()
    miss_ratio()
