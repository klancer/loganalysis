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

