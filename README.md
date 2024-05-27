### This is a python program developed to scrape music event data from a webpage

The program works by scraping and extracting data using requests and selectorlib from the website url,
and then storing this data into a text file under 2 conditions which are:

1st conditon: That the scrapped data isn't "No upcoming tours"
2nd condition: That the scrapped data hasn't been scrapped and stored earlier.

If both conditions are met, then the data is appeneded to the data.txt file and 
an email alert is sent to a designated email address stating a new event has been scrapped.

Depending on the user and expected recency, this program can be run on a timely basis
and the code blockwas provided for that.

The modules used in this program include:
1. requests
2. selectorlib
3. smtplib
4. ssl
5. os
6. time


