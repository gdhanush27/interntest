from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pandas as pd
import csv

link = "https://www.nature.com/articles/s41598-023-28880-x"
page = urlopen(link)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
paper = urlopen(link)
html_encoded = paper.read()
html = html_encoded.decode("utf-8")


abt_index = html.find("Abstract")
start_abt = abt_index + len("Abstract")
end=html[start_abt:]

pattern = "<p.*?>.*?</p.*?>"
match_results = re.search(pattern, end, re.IGNORECASE)
abt = match_results.group()
abt = re.sub("<.*?>", "", abt) 

print("\n\nAbstract : \n",abt)