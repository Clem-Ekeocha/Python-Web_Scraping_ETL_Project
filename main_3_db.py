"""
This is an augumented alternative of main.py
python program with the aim of scraping a music webpage
and storing it in a database
"""

# Import libraries
import requests
import selectorlib
import smtplib, ssl
import os
import time
import sqlite3

# Assign url address to a variable
url = "http://programmer100.pythonanywhere.com/tours/"

# Add the HEADER variable to bypass websites with restrictions to webscrapping programs
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

# Create a connection instance outside any lopp to avoid resource waste
connection = sqlite3.connect("data.db")


# Define a scrape function
def scrape(url):
    """
    scrape the page source from url
    """
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


# Define an extract function that takes the source argument
# Remember to create the "extract.yaml" file gotten from the website element source page
def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value


# Define a store function to the database and append extracted data to the database
def store(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]

    # Create a cursor for executing sql queries
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES(?,?,?)", row)
    connection.commit()



# Define a read function that changes the text to a list using split
# And cleans off every trailing or leading spaces after the split.
def read(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    band, city, date = row


    # Create a cursor for executing sql queries
    cursor = connection.cursor()

    # Query the data using the sql script
    cursor.execute("SELECT * FROM events \
                    WHERE band=? AND city=? AND date=?", (band, city, date)
                   )

    # Extract data from sql code
    rows = cursor.fetchall()
    print(rows)
    return rows


# Define an email sending function
def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "approachphinearts@gmail.com"
    password = "Akukouwa10"

    receiver = "approachphinearts@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)



if __name__ == "__main__":
    scrapped = scrape(url)
    extracted = extract(scrapped)
    print(extracted)

    # Under this code block, first store the new extract and send email only
    # if the extracted is not "No upcoming tours" and
    # if the extracted is not in the previous stored events in the database
    if extracted != "No upcomimg tours":
        row = read(extracted)
        if not row:
            store(extracted)
            send_email(message="Hey, new event was found")

