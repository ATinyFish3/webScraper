# https://realpython.com/beautiful-soup-web-scraper-python/

import requests
from bs4 import BeautifulSoup

import sys

def scraper():
    NUM_RESULTS = 3
    BASE_WIKI_ADDRESS = 'https://en.wikipedia.org'

    search = 'Web Scraper'
    #Get results from user search
    wikiLinks = []
    searchResults = userSearch(search, NUM_RESULTS)
    if not searchResults:
        sys.exit("No results found")
    for i in searchResults:
        wikiLinks.append(i.find('a')['href'])
    print(wikiLinks)

    #need to get user to choose which result they want to use, for now just use top result

    URL = BASE_WIKI_ADDRESS + wikiLinks[0]
    print(URL)

    # Get summary
    summaryResult = summary(URL)
    print(summaryResult[0])
    print(summaryResult[1])


    #Get headers from contents table || get from user input later
    #contentsHeaders = soup.find(id="toc")# id of contents

    #print(contentsHeaders.text)

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

    allResults = soup.find_all('div', class_='mw-search-result-heading')

    #Need to add validation

    if len(allResults) != 0:
        return allResults[:numResults]
    else:
        return False

def summary(pageURL):
    soup = getHTML(pageURL)
    firstStuff = soup.find('div', class_='mw-parser-output')
    if firstStuff == None:
        sys.exit('Error in extracting summary info')
    para1 = firstStuff.find('p').text
    sent1 = para1.split('.')[0] + '.'

    return para1, sent1

if __name__ == '__main__':
    scraper()
