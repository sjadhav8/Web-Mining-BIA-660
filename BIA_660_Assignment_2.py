import requests
import csv
import re


#STEP 1
r = requests.get("https://en.m.wikipedia.org/wiki/List_of_Internet_top-level_domains")
#status code
print("Status code for wikipedia site: ")
print(r.status_code)


#STEP 2
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

top_level_domain = soup.find("table",{'class' : "wikitable sortable"})
links = top_level_domain.find_all("a")

doc=[]
for link in links:
    doc.append(link.get("title"))
#Modified source code
print(doc)
print("")

#Converting list to string
d = (str(doc).strip('[]'))

#Regular expression
x = re.findall(r'[\.]+[a-z]+', d)
#Unique elements in x
x=set(x)
x=list(x)
print("")
print(x)
print("")


#STEP 3
url=[]
for a in x: 
    final = "https"+":"+"//"+"example" + a
    print(final)
    url.append(final)
print("")

#Creating list to save the result
final_url = []
for v in range(len(url)):
    try:
        response = requests.get(url[v])
        res = response.status_code
        c = (url[v],res)
        final_url.append(c)
        print(c)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        e = (url[v]+" failed to connect")
        print(e)
        final_url.append(e)


#STEP 4
# Save in CSV 
with open("Bia660Assignment2.csv","w")as csvfile:
    bia660 = csv.writer(csvfile)
    bia660.writerow(final_url)
