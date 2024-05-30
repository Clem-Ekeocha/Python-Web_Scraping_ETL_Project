"""
This is another program that scraps temperature readings from the same webpage as main.py
and stores both the time stamp and the temperature readings which is then used to plot a graph
on streamlit
"""

# Import libraries
import requests
import selectorlib
import smtplib, ssl
import os
import time
from datetime import datetime

# Assign URL address to the variable
url ='https://programmer100.pythonanywhere.com/'

# Add the Header to help bypass websites with restrictions using the variable below
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

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
    return value



# Define a store function to a txt file and append extracted data into the txt file
def store(extracted):

    # This bit of code captures the time stamp the data is stored
    now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    with open("data_2.txt", "a") as file:
        line = f"{now}, {extracted}\n"
        file.write(line)



if __name__ == "__main__":
    scrapped = scrape(url)
    extracted = extract(scrapped)
    print(extracted)
    store(extracted)
    print(f"This {extracted} data has been stored")




