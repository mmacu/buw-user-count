import requests
from bs4 import BeautifulSoup
from datetime import date

# Send a GET request to the website
response = requests.get("https://www.buw.uw.edu.pl/")

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the span element with the desired value
span_element = soup.find("span", style="font-size:14pt; color: #fff")

# Extract the value from the span element
value = span_element.get_text()

# Get the current date
current_date = date.today().strftime("%Y-%m-%d")

# Append the value and current date to the file
with open("results.csv", "a") as file:
    file.write(f"{current_date},{value}\n")
