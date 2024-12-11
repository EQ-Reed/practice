#starting with importing the required modules

import requests
from bs4 import BeautifulSoup
import random

def scrapeWikiArticle(url):
    response = requests.get(
        url=url,
    )

    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find(id="firstHeading")        #identifying the html header of the page we start with

    print(title.text)

    #get all links
    allLinks = soup.find(id="bodyContent").find_all("a")
    random.shuffle(allLinks)
    linkToScrape = 0

    for link in allLinks:
        #we are only interested in other wikipedia articles
        if link['href'].find("/wiki/") == -1:
            continue

        #use this link to scrape
        linkToScrape = link
        break
    scrapeWikiArticle("https://en.wikipedia.org" + linkToScrape['href'])

scrapeWikiArticle("https://en.wikipedia.org/wiki/Web_scraping")

