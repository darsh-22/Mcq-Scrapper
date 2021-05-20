# ==================================================== #
#                                                      #
#  Created By: Darhil Aslaliya -  GitHub :- darsh-22   #
#                                                      #
# ==================================================== #

# required modules
from bs4 import BeautifulSoup
import requests

# mian scraping function
def scrapingFunction(link):
    data=requests.get(link)
    soup=BeautifulSoup(data.text,'html.parser')
    page_source=soup.get_text()
    with open('<<----- FILE NAME ----->>','a',errors="ignore") as file:
        file.write(page_source)
        file.write('\n')

# extracting sub-links
def link_find():
    # opens 1.txt which contains html content of site.
    with open('1.txt', 'r',  errors='ignore') as file:
        content = file.read()
        soup = BeautifulSoup(content,features="html.parser")
        # finding all anchor tag and extracting href links
        for tag in soup.findAll('a', href=True):
            # savng all anchor tags into link.txt
            with open("link.txt","w") as f:
                f.write(tag['href'])
                f.write('\n')
            # runs all links 
            with open("link.txt", "r") as link:
                l = link.readlines()
                for i in l:
                    url = i
                    scrapingFunction(url)

#code driver
link_find()