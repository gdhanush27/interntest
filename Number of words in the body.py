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


body_index = html.find("<div class=\"c-article-body\">")
start_body = abt_index + len("<div class=\"c-article-body\">")
end_body=html.find("References")
end = html[start_body:end_body]

pattern = "<p.*?>.*?</p.*?>"
match_results = re.findall(pattern, end, re.IGNORECASE)

body=''
c=0
for i in match_results:
    if(c!=0):
        body=body+' '+i
    c=1

body = re.sub("<.*?>", "", body) 
body_1=body.split()
print("\n\nNumber of words in the body :\n",len(body_1))