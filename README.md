REQUIREMENTS:
=============
 - python 2,7
 - django
 - mysql
 - requests

SETUP:
======
 - Set up mysql preferrably on a linux machine 
 put your username and password in `eeassignment/eeassignment/settings.py`
 in the DATABASES dictionary

 - Install django via pip or any other package manager. Install requests
 and any other required library

 Run:
 ====

 - cd into the eeassignment main directory and run `python manage.py runserver`

 - if you wish to crawl the internet and setup your database go to the link:
   `127.0.0.1/crawler/crawler`

 - if you wish to display the products stored in the database use
 `127.0.0.1/crawler/website`