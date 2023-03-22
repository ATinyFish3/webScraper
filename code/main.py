import requests
from bs4 import BeautifulSoup

import sys

import re


def scraper():  # main scraping function
    NUM_RESULTS = 3  # number of results that the searching should return
    BASE_WIKI_ADDRESS = 'https://en.wikipedia.org'  # wiki URL to prepend to URLs

    SEARCH = "data scrape"  # the 'user' search to be replaced with input

    # Get results from user search
    wikiLinks = []  # store links to search result pages
    searchResults = userSearch(SEARCH, NUM_RESULTS)
    for i in searchResults:
        wikiLinks.append(i.find('a')['href'])
    # print(wikiLinks)

    # need to get user to choose which result they want to use, for now just use top result

    URL = BASE_WIKI_ADDRESS + wikiLinks[0]
    print('Page URL: ', URL)
    #for u in wikiLinks:
        #print(BASE_WIKI_ADDRESS + u)

    # Get summary
    if True:  # Replace with user input
        sumResult = summary(URL)
        print(sumResult)

    # Get all text
    if True:
        print('allText here')
        # allText(URL)

    # Get headers from contents table || get from user input later
    # contentsHeaders = soup.find(id="toc")# id of contents

    # print(contentsHeaders.text)


def getHTML(pageURL):
    try:
        page = requests.get(pageURL)
    except:
        sys.exit('Bad URL')
    soup = BeautifulSoup(page.content, 'html.parser')

    return soup


def userSearch(searchTerm, numResults):
    searchReq = "https://en.wikipedia.org/w/index.php?search=" + searchTerm + "&title=Special:Search&profile=advanced&fulltext=1&ns0=1"
    soup = getHTML(searchReq)

    # Check if search results page is a disambiguation page
    disambiguation = soup.find(class_='mw-disambig')
    if disambiguation:
        #for l in soup.find_all('a',href=True):
            #print('https://en.wikipedia.org' + l['href'])
        return sys.exit("The search result page is a disambiguation page. Please use a more specific query.")

    allResults = soup.find_all('div', class_='mw-search-result-heading')

    # Need to add validation

    if allResults:
        return allResults[:numResults]
    else:
        return sys.exit("No results found.")


def summary(pageURL):
    soup = getHTML(pageURL)
    try:
        paras = soup.select('p')
    except:
        sys.exit('Error in extracting summary info')  # keep to handle exceptionos

    for p in paras:
        # Remove any citation references in square brackets
        text = re.sub(r'\[[^\]]*\]', '', p.text)
        # Remove any non-word characters (e.g. punctuation, symbols, etc.)
        text = re.sub(r'[^\w\s]', '', text)
        # Find the first paragraph with more than 50 characters (excluding spaces)
        if len(text.replace(' ', '')) > 50:
            return return re.sub(r'\[[^\]]*\]', '', p.text)
    return "Summary not available"


# Better if get rid of things in []
def allText(pageURL):  # Return all text from wiki page
    soup = getHTML(pageURL)
    try:
        paras = soup.select('p')
    except:
        sys.exit('Error in extracting summary info')  # keep to handle exceptionos
    for i in paras:
        print(i.text)


if __name__ == '__main__':
    scraper()
