#importing libraries 
import queue
import os
import urllib
import re
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.robotparser
from urllib.parse import urlparse
from urllib.parse import urljoin
from urllib.parse import urlsplit

#getting the chromedriver 
options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(r'C:\Users\Srujan\chromedriver')
driver.get('http://www.stevens.edu/');

path = os.getcwd()  
print ("The current working directory is %s" % path)   

#Creating Directory
path1 = os.mkdir("MYSTEVENS")                        
path_new= os.chdir("MYSTEVENS")

def is_absolute(url):              
    return bool(urlparse(url).netloc)
rp = urllib.robotparser.RobotFileParser()

email_address = []
q = queue.Queue()
new_list = []
q.put("https://www.stevens.edu/")
for i in range(100):    
    url = q.get()  
       
    driver.get(url)    
    soup = BeautifulSoup(driver.page_source, 'html.parser')    
    
    # Extracting email address   
    email_address += re.findall("\S+@stevens.edu", soup.get_text())    
    email_address = list(set(email_address))    
    links = driver.find_elements_by_xpath('.//a')
    
    links = soup.find_all('a')    
    for link in links:        
        u = link.get('href')        
        if not is_absolute(u):            
            u = urljoin(url, u)        
            if "stevens.edu" in u:            
                q.put(u) 
           
        urlsplit_result = urlsplit(u)
        new_list.append(urlsplit_result.scheme + '://' + urlsplit_result.netloc + urlsplit_result.path)
    
                
        rp.set_url("https://www.stevens.edu/robot.txt")       
        rp.read()                                              
        rp.crawl_delay(8)
        
        directoryofmail = os.path.dirname("Stevens.edu" +urlsplit_result.path)    
        if not os.path.exists(directoryofmail):
                try: 
                    os.makedirs(directoryofmail)
                    #print(urlsplit_result.path)
                except OSError as e:
                     print (e)
        print("Queue size: {}".format(q.qsize()))    
        print("Number of email addresses: {}".format(len(email_address)))
        print(rp.can_fetch("*",urlsplit_result.path))

#Creating text file with emails
with open("mystevens.txt", "w+") as f:    
    for email in email_address:        
        f.write(email + "\n")
