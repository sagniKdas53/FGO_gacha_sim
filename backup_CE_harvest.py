from bs4 import BeautifulSoup as soup
import requests

#my_url = "https://fate-go.cirnopedia.org/craft_essence.php?exp=0&bond=0&gift=0&valentine=0"
#r = requests.get(my_url)

r = "Craft Essence _ FGO Cirnopedia.mhtml"
f = open(r)      # simplified for the example (no urllib)
flip_soup = soup(f,"html.parser")
f.close()

#flip_soup = soup(r.content,"html.parser")

containers = flip_soup.find_all("tr",{"class":"reg US"})

f = open("simdata.txt","w+",encoding='utf8')
f.write(soup.prettify(containers[0]))
f.close()
#print(soup.prettify(containers[0]))
f = open("CEs.csv","a",encoding='utf8')


for container in containers:
    name = container.find_all("a",{"class":"fancybox"})
    #print(name[0].text)
    desc = container.find_all("td", {"class": "desc"})
    #print(desc[0].text)
    try:
        rare = container.find_all("span", {"class": "rare1"})
        #print(rare[0].text)
    except IndexError:
        try:
            rare = container.find_all("span", {"class": "rare2"})
            #print(rare[0].text)
        except IndexError:
            try:
                rare = container.find_all("span", {"class": "rare3"})
                #print(rare[0].text)
            except IndexError:
                try:
                    rare = container.find_all("span", {"class": "rare4"})
                    #print(rare[0].text)
                except IndexError:
                    rare = container.find_all("span", {"class": "rare5"})
                    #print(rare[0].text)
    if rare[0].text == "*** R":
        print(name[0].text + "  " + desc[0].text + "  " + rare[0].text + "\n")
        f.write(name[0].text + "  " + desc[0].text + "  " + rare[0].text + "\n")
    elif rare[0].text == "**** SR":
        print(name[0].text + "  " + desc[0].text + "  " + rare[0].text + "\n")
        f.write(name[0].text + "  " + desc[0].text + "  " + rare[0].text + "\n")
    elif rare[0].text == "***** SSR":
        print(name[0].text + "  " + desc[0].text + "  " + rare[0].text + "\n")
        f.write(name[0].text + "  " + desc[0].text + "  " + rare[0].text + "\n")

f.close()
