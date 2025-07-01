#pip install aiohttp beautifulsoup4

import asyncio
import aiohttp #Asynchronous HTTP client for making non-blocking requests.
from bs4 import BeautifulSoup #For parsing HTML,
import time  #timing

async def fetch_page(session, url):
    """Fetch a single page asynchronously and return its HTML content."""
    try:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.text()
            else:
                print(f"Failed to fetch {url}: Status {response.status}")
                return None
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

async def scrape_quotes(url):
    """Scrape quotes from a single page."""
    async with aiohttp.ClientSession() as session:
        html = await fetch_page(session, url)
        if html:
            soup = BeautifulSoup(html, 'html.parser')
            # Extract quotes from <span class="text">
            quotes = soup.find_all('span', class_='text')
            return [quote.get_text().strip() for quote in quotes]
        return []

async def main():
    """Main function to scrape multiple pages concurrently."""
    start_time = time.time()  # Start timing
    base_url = 'http://quotes.toscrape.com/page/{}/'
    # Create tasks for scraping pages 1 to 3
    tasks = [scrape_quotes(base_url.format(i)) for i in range(1, 4)]
    
    # Run tasks concurrently and gather results
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    # Print results
    for i, quotes in enumerate(results, 1):
        if isinstance(quotes, Exception):
            print(f"Page {i} failed: {quotes}")
        else:
            print(f"\nQuotes from page {i}:")
            for j, quote in enumerate(quotes, 1):
                print(f"{j}. {quote}")
    
    # Calculate and print total time
    print(f"\nTotal time: {time.time() - start_time:.2f} seconds")

# Run the asynchronous program
if __name__ == "__main__":
    asyncio.run(main())
