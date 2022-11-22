# https://realpython.com/beautiful-soup-web-scraper-python/

import requests
from bs4 import BeautifulSoup

def scraper():
    NUM_RESULTS = 3
    BASE_WIKI_ADDRESS = 'https://en.wikipedia.org'

    #Get results from user search
    wikiLinks = []
    searchResults = userSearch("web scraping", NUM_RESULTS)
    for i in searchResults:
        wikiLinks.append(i.find('a')['href'])

    #print(wikiLinks)

    #need to get user to choose which result they want to use, for now just use top result

    URL = BASE_WIKI_ADDRESS + wikiLinks[0]
    print(URL)


    #Get headers from contents table || get from user input later
    #contentsHeaders = soup.find(id="toc")# id of contents

    #print(contentsHeaders.text)

def userSearch(searchTerm, numResults):
    searchReq = "https://en.wikipedia.org/w/index.php?search=" + searchTerm + "&title=Special:Search&profile=advanced&fulltext=1&ns0=1"
    page = requests.get(searchReq)
    soup = BeautifulSoup(page.content, "html.parser")

    allResults = soup.find_all('div', class_='mw-search-result-heading')
    return allResults[:numResults]

if __name__ == '__main__':
    scraper()
