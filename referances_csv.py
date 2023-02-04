from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pandas as pd
import csv

ref_index = html.find("References")
start_ref = ref_index + len("References")
end_ref=html.find("Acknowledgements")
end=html[start_ref:end_ref]

pattern = "<p.*?>.*?</p.*?>"
match_results = re.findall(pattern, end, re.IGNORECASE)
reff=[]
for i in match_results:
    reff.append(re.sub("<.*?>", "", i))
    
df=pd.DataFrame({},columns=['Reference','Link'])
li=[]
r=[]
for i in reff:
    r.append(i)
    li.append(re.findall(r'(https?://\S+)', i))
df['Link']=li[0:-1]
df['Reference']=r[0:-1]
df.to_csv(r"D:\Users\Desktop\Intern_test\references.csv")