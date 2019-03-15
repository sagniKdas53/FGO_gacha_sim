from __future__ import print_function
from bs4 import BeautifulSoup as Soup
import wget
import os
import re

rowst = []
i = 0
# r = "Servants _ FGO Cirnopedia.html"
# r="Servants _ Fate Grand Order Wiki - GamePress.html"
r = "Servant List by ID _ Fate_Grand Order Wikia _ FANDOM powered by Wikia.mhtml"
# my_url = "https://fate-go.cirnopedia.org/servant_all.php?JP=0#nav"
# my_url="https://grandorder.gamepress.gg/servants"
my_url = "https://fategrandorder.fandom.com/wiki/Servant_List_by_ID"
if not os.path.isfile(r):
    wget.download(my_url, r)

fo = open(r)      # simplified for the example (no urllib)
flip_Soup = Soup(fo, "html.parser")
fo.close()
if os.path.isfile("CEs.ssv"):
    os.remove("CEs.csv")

f = open("Servants.csv", "a", encoding='utf8')

table = flip_Soup.findChildren('table')[0]
rows = table.findChildren('tr')
headers = [x.getText() for x in rows[0].findChildren('th')]
# f.write(str(headers).replace("\n", "").replace("[", "").replace("]", ""))

for row in rows:
    cells = row.findChildren('td')
    for cell in cells:
        cell_content = cell.getText()
        ccon = re.sub( '\s+', ' ', cell_content).strip()
        if ccon != "":
            if ccon.__contains__("★"):
                rarity = ccon
                rarv = 1
                if rarity == "★ ★ ★ ★ ★":
                    rarv = 5
                elif rarity == "★ ★ ★ ★":
                    rarv = 4
                elif rarity == "★ ★ ★":
                    rarv = 3
                elif rarity == "★ ★":
                    rarv = 2
                f.write(ccon + "," + str(rarv)+",")
            else:
                f.write(ccon + ",")
    f.write("\n")
f.close()
# print(rowst)