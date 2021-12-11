import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

#######################

dent_names = []
dent_categorys = []
dent_phons = []
dent_locs = []
##############################
result = requests.get("https://www.yelp.com/search?find_desc=Dentists&find_loc=Texas%20City%2C%20TX&start=0")

src = result.content

soup = BeautifulSoup(src, "lxml")
########
dent_name = soup.find_all("h4", {"class":"css-1l5lt1i"})

dent_category = soup.find_all("p", {"class":"css-1j7sdmt"})

dent_phon = soup.find_all("p", {"class":" css-8jxw1i"})

dent_loc = soup.find_all("span", {"class":" raw__09f24__3Azrj"})
print()
########

for i in range(len(dent_name)):
    dent_names.append(dent_name[i].text)
    dent_categorys.append(dent_category[i].text)
    dent_phons.append(dent_phon[i].text)
    dent_locs.append(dent_loc[i].text)

file_list = [dent_names, dent_categorys, dent_phons, dent_locs]
exported = zip_longest(*file_list)
#########
with open("D:\python\web scrapying\proudcts2.csv", "w") as myfile1:
    wr = csv.writer(myfile1)
    wr.writerow(["dent names","dent categorys","dent phons","dent loc"])
    wr.writerows(exported)