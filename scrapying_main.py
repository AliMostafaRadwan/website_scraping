import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

#######################

proudcts = []
proudct_prices = []
proudct_rates = []
##############################
result = requests.get("THE WEBSITE YOU WANT TO SCRAP")

src = result.content

soup = BeautifulSoup(src, "lxml")
########
proudct = soup.find_all("h6", {"class":"title"})#examples

proudct_price = soup.find_all("span", {"class":"is block sk-clr1"})#examples

proudct_rate = soup.find_all("span", {"class":"rating-reviews"})#examples
########

for i in range(len(proudct)):
    proudcts.append(proudct[i].text)
    proudct_prices.append(proudct_price[i].text)
    proudct_rates.append(proudct_rate[i].text)

file_list = [proudcts, proudct_prices, proudct_rates]
exported = zip_longest(*file_list)
#########
with open("CSV_PATH", "w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["proudct","proudct price","proudct rate"])
    wr.writerows(exported)
