import requests
from bs4 import BeautifulSoup                                       
URL = 'https://magicseaweed.com/St-Andrews-East-Surf-Report/38/'    
response = requests.get(URL)                                        
print(response)                                                     
page = BeautifulSoup(response.text, 'html.parser')
MSWheights = page.find_all('h4')
print(page.title.string)
print(MSWheights)
