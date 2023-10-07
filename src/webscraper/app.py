import requests
from bs4 import BeautfulSoup4
import re

url = "" #here is where they 
text = requests.get(url)

r = requests.get(text)
#get the contents in text form
soup = BeautifulSoup(r.text, "html.parser")

