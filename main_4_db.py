"""
This program scraps temperature readings from the same webpage as main_2.py
and stores both the time stamp and the temperature readings in a SQLite Database
which is then used to plot a graph.
"""

# Import libraries
import requests
import selectorlib
import smtplib, ssl
import os
import time
import sqlite3
from datetime import datetime

# Assign URL address to the variable
url ='https://programmer100.pythonanywhere.com/'

# Add the Header to help bypass websites with restrictions using the variable below
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

# Create a connection instance outside any lopp to avoid resource waste
connection = sqlite3.connect("data.db")


# Define a scrape function
def scrape(url):
    response = requests.get(url, headers = HEADERS)
    source = response.text
    return source


# Define an extract function that takes the source argument
# Remember to create the "extract.yaml" file gotten from the website element source page
def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract_2.yaml")
    value = extractor.extract(source)["temp"]

    # This bit of code captures the time stamp the data is stored
    now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    return f"{now},{value}"


# Define a store function to a txt file and append extracted data into the txt file
def store(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]

    # Create a cursor for executing sql queries
    cursor = connection.cursor()
    cursor.execute("INSERT INTO temperature VALUES(?,?)", row)
    connection.commit()


# Define an email sending function
def send_email(message):
    print(message)


while True:
    if __name__ == "__main__":
        scrapped = scrape(url)
        extracted = extract(scrapped)
        store(extracted)
        send_email(message = "Email Sent Successfully")

    time.sleep(3)








