from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime

LINK = "https://www.nytimes.com"

def getArticles(link):

    r=requests.get(link)

    page_parse = BeautifulSoup(r.text, 'html.parser')
    #print(page_parse)

    titleList = []
    search_results = []

    
    search_results = page_parse.find_all("h3",{"class":"indicate-hover"})
    #for p in page_parse.find_all("h3",{"class":"indicate-hover"}):
    #    if(p.find(class_ = 'css-1h1983p')):
    #        continue
    #    search_results = search_results.append(p)


    #print(len(search_results))
    for result in search_results:
        realText = result.text
        titleList.append(realText)
    return(titleList)

def seperatePrint(list):
    wrongItems = ["Wordle", "Today’s Wordle Review", "Connections | Beta", "Spelling Bee", "The Crossword", "Letter Boxed"]
    finalList = []
    for f in list:
        if(f in wrongItems):
            continue
        print(f)
        finalList.append(f)
        print()
    return finalList

def save_to_file(list):
    with open('NYTdaily.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(list)
    print("CSV file updated.")

articles = getArticles(LINK)
#print(articles)

final = seperatePrint(articles)
print(final)
#save_to_file(final)
