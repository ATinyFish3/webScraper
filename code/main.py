# https://realpython.com/beautiful-soup-web-scraper-python/

import requests
from bs4 import BeautifulSoup

def scraper():
    #Base URL to use, get from user input later
    URL = "https://en.wikipedia.org/wiki/Web_scraping"

    #Get page html
    page = requests.get(URL)

    #Get soup object
    soup = BeautifulSoup(page.content, "html.parser")

    #Get headers from contents table || get from user input later
    contentsHeaders = soup.find(id="toc")

    print(contentsHeaders.prettify())

    print(contentsHeaders.text)

if __name__ == '__main__':
    scraper()
