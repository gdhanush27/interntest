from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pandas as pd
import csv

pattern = "<h1.*?>.*?</h1.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title)

abt_index = html.find("Abstract")
start_abt = abt_index + len("Abstract")
end=html[start_abt:]

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

pattern = "<p.*?>.*?</p.*?>"
match_results = re.search(pattern, end, re.IGNORECASE)
abt = match_results.group()
abt = re.sub("<.*?>", "", abt) 


dic={"Title":title,"Abstract":abt,"number of words in the abstract":len(abt.split()),"Number of words in the body":len(body_1)}
df1=pd.DataFrame(dic,index=[0])
df1.to_csv(r"D:\Users\Desktop\Intern_test\paper_stats.csv")