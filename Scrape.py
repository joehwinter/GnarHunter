import requests
from bs4 import BeautifulSoup                                      
URL = 'https://magicseaweed.com/St-Andrews-East-Surf-Report/38/'  
response = requests.get(URL)                                       
page = BeautifulSoup(response.content, 'html.parser')
table = page.find(id='msw-js-fc')
text = table.find_all('td', class_='text-center background-gray-lighter')
heights = []
for elem in text:
    if elem.find('h4',class_="nomargin font-sans-serif heavy") != None:
        heights.append(elem.find('h4', class_="nomargin font-sans-serif heavy"))
for elem in heights: 
    print(elem.text, end='\n'*2)

