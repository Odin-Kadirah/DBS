from bs4 import BeautifulSoup as bs
import requests
import csv
from collections import Counter

# this function returns a soup page object
def getPage(url):
    r = requests.get(url)
    data = r.text
    spobj = bs(data, "lxml")
    return spobj

# scraper website: heise.de
def main():
    # dynamische url
    heise_url = "https://www.heise.de/thema/https"
    a =[]
    #geht solange durch die header bis bei keiner neuen seite die Schleife verlassen wird
    while(True):
        #updaten der Url
        content=getPage(heise_url)
        #navigieren zur relevanten Sektion
        content=content.find("div",{"class":"keywordliste"}).nav
        #Als Datenstruktur haben wir ein Array benutzt.
        #finde alle Header und schreibe sie in Arrays
        for i in content.findAll("header"):
            #liest die Zeilen der Header ein
            liste1 = i.text.split("\n")
            #verwirft die Leertasten
            liste2 = liste1[0].split(" ")
            #vereinigt die Listen
            a=a+liste2
            #print(i.text)
            #print(a)
        #navigieren zur nächsten seite
        temp1=getPage(heise_url)
        temp1=temp1.find("a",{"class":"seite_weiter"})
        #verlasse scheife wenn keine neue Seite mehr existiert
        if(temp1==None):
            break
        temp1=temp1.get("href")
        heise_url="https://www.heise.de"+temp1
        print ("die neue url ist: "+heise_url+"\n")
    #Analysiere das Array
    zähler=Counter(a)
    print ("Die am häufigsten vorkommenden Wörter sind:\n",zähler.most_common(3))
    print("\nDONE !\n\n\nheise scrapped completly.\n")



# main program

if __name__ == '__main__':
    main()
