import requests
from bs4 import BeautifulSoup



def getshirturls():
    url = "https://theyetee.com/collections/daily-tees"  # website that images will be pulled from
    link = [] #empty list where URLs of the pictures will be added later
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    # print(doc.prettify())
    # tag = doc.find_all("a", {"class": "js--modaal-gallery"})
    # for url in doc.find_all('a'):
    #    print(url.get('href'))
    for url in doc.find_all(class_="js--modaal-gallery"): #searches all classes with js--modaal-gallery
        link.append(url.get('href')) #specifies only URLs

    if len(link) == 0: #checks if the link list is empty, which only happens when there are no shirts available
        return [] #print("No shirts today!")
    else:
        return ["https:" + link[0], "https:" + link[6]]
        #print("https:" + link[0]) #prints the first url, with formatting added
        #print("https:" + link[6]) #prints the second url
