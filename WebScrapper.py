import requests
from bs4 import BeautifulSoup

# URL of the news website
url = "https://www.bbc.com/news"

# Fetch the webpage
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract headlines (customize based on actual structure)
headlines = soup.find_all('h3')  # or 'h2' or other relevant tags

# Save headlines to a text file
with open("headlines.txt", "w", encoding='utf-8') as f:
    for headline in headlines:
        if headline.text.strip():
            f.write(headline.text.strip() + "\n")

print("Headlines saved to headlines.txt")
