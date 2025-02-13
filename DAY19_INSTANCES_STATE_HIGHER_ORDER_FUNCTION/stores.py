import requests
from bs4 import BeautifulSoup

# pip3 install beautifulsoup4

# Replace this with the actual URL
url = "http://storemaster.mavistire.com/"

# Fetch the webpage
response = requests.get(url)
html_content = response.content

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find the table containing store information
table = soup.find('table', {'style': 'font-size: 14px; background-color: #f5f5f5'})

# Extract the headers
headers = [header.text.strip() for header in table.find_all('a')]

# Extract the rows
rows = table.find_all('tr')[1:]  # Skip the header row # Use [1:11]  # Limit to the first 10 rows

# Store the extracted data
stores_info = []
for row in rows:
    columns = row.find_all('td')
    store_info = {headers[i]: columns[i].text.strip() for i in range(len(columns))}
    stores_info.append(store_info)

# Display the extracted store information
for store in stores_info:
    print(store)

# Example of how to save the data to a CSV file
import csv

with open('stores_info.csv', 'w', newline='') as csvfile:
    fieldnames = headers
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for store in stores_info:
        writer.writerow(store)
