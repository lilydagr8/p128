from bs4 import BeautifulSoup
import pandas as pd
import requests

url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

page = requests.get(url)
print(page)

soup = BeautifulSoup(page.text,'html.parser')

star_table = soup.find('table')

temp_list = []

table_rows = star_table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Star_names = []
Distance = []
Mass = []
Radius = []
Lum = []

df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,Lum)),columns=['Star_Names','Distance','Mass','Radius','Lum'])
print(df2)

df2.to_csv('bright_stars.csv')