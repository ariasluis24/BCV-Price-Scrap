import requests, urllib3
urllib3.disable_warnings()
from bs4 import BeautifulSoup
page_to_scrape = requests.get('https://www.bcv.org.ve', verify=False)
soup = BeautifulSoup(page_to_scrape.text, 'html.parser')
prices = soup.findAll('div' ,attrs={'class':'col-sm-6 col-xs-6 centrado'})
for price in prices:
    print(price.text)