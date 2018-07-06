# Log Analysis Project

## 1. Purpose:
Build an internal reporting tool for a newspaper website that determines what kinds of articles the site's readers like.

Use SQL and python program to report the following:
1. What are the most popular three articles?
2. Who are the most popular article authors?
3. On which days did more than 1% of requests lead to errors?
This project is part of the Udacity Full Stack Web Developer Nanodegree.

## 2. Technologies Used:
1. PostgreSQL
2. Python
3. Vagrant
4. VirtualBox

## 3. Setup
1. Ensure that Python, the python package psycopg2, Vagrant, and VirtualBox are installed. [Vagrantfile link](https://github.com/udacity/fullstack-nanodegree-vm/blob/master/vagrant/Vagrantfile) is here.
2. Download or clone the [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
3. Download the SQL database, unzip, and save [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) in the vagrant directory.
4. Navigate to the vagrant folder in the terminal and enter vagrant up to bring the server online, followed by vagrant ssh to log in.
5. To run the SQL queries directly, navigate to the vagrant directory with cd /vagrant, then enter "psql -d news -f newsdata.sql" to connect to and run the project database.


After installation of "News" PostgreSQL DB it will consist of three tables:
The articles table includes information about news articles and their contents.
The authors table includes information about the authors of articles.
The log table includes one entry for each time a user has accessed the news site.

## 4. ===SQL Views (newsview.sql) content===
'''
CREATE view slugname as
SELECT slug,title,name
FROM articles,authors
WHERE articles.author=authors.id;

CREATE view slug as
SELECT substring(log.path, '.*/(.*)$')
FROM log;

CREATE view slugcnt as
SELECT substring,count(*) as cnt
FROM slug group by substring
order by cnt desc;

CREATE view statusokdate as
SELECT status,time::date as date
FROM log where status like '200%';

CREATE view statusnotfounddate as
SELECT status,time::date as date
FROM log
WHERE status like '404%';

CREATE view cntokdate as
SELECT date,count(*) as cntok
FROM statusokdate
GROUP by date;

CREATE view cntnotfounddate as
SELECT date,count(*) as cntnotfound
FROM statusnotfounddate
GROUP by date;

CREATE view dateoknotfound as
SELECT cntnotfounddate.date,cntok,cntnotfound
FROM cntnotfounddate inner join cntokdate
ON cntnotfounddate.date=cntokdate.date;

CREATE view httpratio as
SELECT date, (1.0*cntnotfound/(cntok+cntnotfound))*100 as result
FROM dateoknotfound;
'''

## 5. Operation:
1. To create the SQL views, run the newsview.sql, enter "psql -d news -f newsview.sql" 
2. To execute the program in this repo, enter "python3 newsdb.py".
