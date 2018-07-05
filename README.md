# Log Analysis Project

## 1. Purpose:
Build an internal reporting tool for a newspaper website that determines what kinds of articles the site's readers like.

Use SQL and python program to report the following:
1. What are the most popular three articles?
2. Who are the most popular article authors?
3. On which days did more than 1% of requests lead to errors?
This project is part of the Udacity Full Stack Web Developer Nanodegree.

## 2. Technologies Used:
SQL
Python
Vagrant
VirtualBox
Setup
Ensure that Python, the python package psycopg2, Vagrant, and VirtualBox are installed.

'News' postgres DB with three tables in installed:
The articles table includes information about news articles and their contents.
The authors table includes information about the authors of articles.
The log table includes one entry for each time a user has accessed the news sit

## 3. ===Views required for the program:===

create view slugname as select slug,title,name from articles,authors where articles.author=authors.id;

create view slug as select substring(log.path, '.*/(.*)$') from log;

create view slugcnt as select substring,count(*) as cnt from slug group by substring order by cnt desc;

create view statusokdate as select status,to_char(time, 'YYYY-MM-DD' ) as date from log where status like '200%';

create view statusnotfounddate as select status,to_char(time, 'YYYY-MM-DD' ) as date from log where status like '404%';

create view cntokdate as select date,count(*) as cntok from statusokdate group by date;

create view cntnotfounddate as select date,count(*) as cntnotfound from statusnotfounddate group by date;

create view dateoknotfound as select cntnotfounddate.date,cntok,cntnotfound from cntnotfounddate inner join cntokdate on cntnotfounddate.date=cntokdate.date;

create view httpratio as select date, (1.0*cntnotfound/cntok)*100  as result from dateoknotfound;

## 4. Operation:
Create above views in the database, and run "python3 newsdb.py" to see the report.


