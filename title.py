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
pattern = "<h1.*?>.*?</h1.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title)

print("Title :\n",title)