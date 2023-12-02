# web_scraper.py

import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract information from the HTML (customize based on the website structure)
            # Example: Extract all the links on the page
            links = [a['href'] for a in soup.find_all('a', href=True)]

            return links
        else:
            print(f"Failed to retrieve content. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage: Scraping links from the OpenAI homepage
    url_to_scrape = "https://www.openai.com/"
    scraped_links = scrape_website(url_to_scrape)

    if scraped_links:
        print(f"Scraped links from {url_to_scrape}:\n")
        for link in scraped_links:
            print(link)
    else:
        print("No links scraped.")
