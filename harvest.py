from bs4 import BeautifulSoup as soup
import wget
import os
my_url = "https://fate-go.cirnopedia.org/craft_essence.php?exp=0&bond=0&gift=0&valentine=0"

r = "Craft Essence _ FGO Cirnopedia.html"
if  not os.path.isfile(r):
    wget.download(my_url, r)
f = open(r)      # simplified for the example (no urllib)
flip_soup = soup(f,"html.parser")
f.close()

if os.path.isfile("CEs.ssv"):
    os.remove("CEs.csv")

containers = flip_soup.find_all("tr",{"class":"reg US"})
f = open("CEs.csv","a", encoding='utf8')
for container in containers:
    name = container.find_all("a",{"class":"fancybox"})
    print(name[0].text)
    desc = container.find_all("td", {"class": "desc"})
    print(desc[0].text)
    try:
        rare = container.find_all("span", {"class": "rare1"})
        print(rare[0].text)
        r = "1"
    except IndexError:
        try:
            rare = container.find_all("span", {"class": "rare2"})
            print(rare[0].text)
            r = "2"
        except IndexError:
            try:
                rare = container.find_all("span", {"class": "rare3"})
                print(rare[0].text)
                r = "3"
            except IndexError:
                try:
                    rare = container.find_all("span", {"class": "rare4"})
                    print(rare[0].text)
                    r = "4"
                except IndexError:
                    rare = container.find_all("span", {"class": "rare5"})
                    print(rare[0].text)
                    r = "5"
    print(name[0].text + "," + desc[0].text.replace(",", "") + "," + rare[0].text + "\n")
    f.write(name[0].text + "," + desc[0].text.replace(",", "") + "," + rare[0].text + "," + r + "\n")
f.close()
