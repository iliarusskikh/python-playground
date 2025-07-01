import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'http://quotes.toscrape.com'

try:
    # Send a GET request to the website
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all quotes (within <span class="text"> tags)
        quotes = soup.find_all('span', class_='text')
        
        # Print each quote
        print("Quotes:")
        for i, quote in enumerate(quotes, 1):
            print(f"{i}. {quote.get_text().strip()}")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

except requests.RequestException as e:
    print(f"Error fetching the page: {e}")
