### This shows the development of 2 python programs main.py and main_2.py

1. main.py scraps music events from a webpage, stores it in a text file, and finally sends an email notification.
2. main_2.py similar scraps temperature readings from a webapge, stores in a txt file and plots a chart using streamlit 
3. main_3_db.py similar to main.py but stores the data in a database using SQLite through "data.db" stored in the project repo
4. main_4_db.py similar to main_2.py but rather stores data in a database using SQLite through "data.db" stored in the project repo

developed to scrape music event data from a webpage

**_main.py_** works by scraping and extracting data using requests and selectorlib from the website url,
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


**_main_2.py_** scraps the temperature data alongside the timestamp for the visualization creation purpose 
and stores that information in the data_2.txt file. 

The modules used in the main_2.py program include:
1. requests
2. selectorlib
3. smtplib
4. pandas
5. datetime
6. time
7. streamlit
8. plotly.express

