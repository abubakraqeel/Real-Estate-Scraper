from bs4 import BeautifulSoup
import requests
import pandas as pd

base_url = "https://www.zameen.com/Rentals/Karachi_DHA_Defence-213-1.html?area_min=334.45094400000005&area_max=501.676416&sort=date_desc"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Safari/605.1.15"}
r = requests.get(url= base_url, headers=headers)

soup = BeautifulSoup(r.content, "lxml")
listings = soup.find_all('li', class_= "ef447dde")
listings_links =[]
prefix = "https://www.zameen.com"
for listing in listings:
    listing = str(listing.find('a'))
    listing = listing.split()
    listings_link = listing[4].split('=')[-1]
    listings_links.append(prefix+listings_link)

listings_links= [link.replace('"', '' ) for link in listings_links]


rent = []
name = []
type =[]
size = []
for link in listings_links:
    r_new = requests.get(link, headers= headers)
    soup2 = BeautifulSoup(r_new.content, 'lxml')
    link_rent = soup2.find('span', class_ = '_8eee1bdd')
    link_name = soup2.find('h1', class_='_64bb5b3b')
    link_type = soup2.find('span', class_='_812aa185')
    link_size = soup2.find(attrs={"aria-label": 'Area'})
    link_added = soup2.find(attrs={"aria-label": 'Creation date'})
    type.append(link_type.text)
    size.append(link_size.text)
    name.append(link_name.text)
    rent.append(link_rent.text)

listings_dict = {"Name": name, "Type": type, "Rent": rent, "Size": size}
df = pd.DataFrame(listings_dict)
print(df)









