"""
This is a python program with the aim of scraping a music webpage
"""

# Import libraries
import requests
import selectorlib
import smtplib, ssl
import os
import time

# Assign url address to a variable
url = "http://programmer100.pythonanywhere.com/tours/"

# Add the HEADER variable to bypass websites with restrictions to webscrapping programs
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}


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


# Define a store function to a txt tile and append extracted data to the txt file
def store(extracted):
    with open("data.txt", "a") as file:
        file.write(extracted + '\n')


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


# Define a function that reads the data.txt file
def read(extracted):
    with open("data.txt", "r") as file:
        return file.read()


if __name__ == "__main__":
    scrapped = scrape(url)
    extracted = extract(scrapped)
    print(extracted)
    content = read(extracted)

    # Under this code block, first store the new extract and send email only
    # if the extracted is not "No upcoming tours" and
    # if the extracted is not in the previous stored events in the data.txt file
    if extracted != "No upcomimg tours":
        if extracted not in content:
            store(extracted)
            send_email(message = "Hey, new event was found")



# If you want the script to run non-stop and keep checking everytime,
# then replace code block from line 68 - 80 with the WHILE loop and
# use the code block below to adjust the time.sleep for the desired frequency
# Or better still use "pythonanywhere.com"
"""
if __name__ == "__main__":
    while True:
        scrapped = scrape(url)
        extracted = extract(scrapped)
        print(extracted)
        content = read(extracted)
    
        # Under this code block, first store the new extract and send email only
        # if the extracted is not "No upcoming tours" and
        # if the extracted is not in the previous stored events in the data.txt file
        if extracted != "No upcomimg tours":
            if extracted not in content:
                store(extracted)
                send_email(message = "Hey, new event was found")
        time.sleep(2)       # Every 2 seconds
"""

