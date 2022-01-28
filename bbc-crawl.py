import requests
from bs4 import BeautifulSoup
import re


res = requests.get("https://www.bbc.com/")

soup = BeautifulSoup(res.text, 'html.parser')


for tag in soup.find_all(re.compile("^b")):
    print(tag)
