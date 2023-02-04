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
ref = ''
for i in match_results:
        ref=ref+'\n\n'+i

ref = re.sub("<.*?>", "", ref) 

print("\n\nReferance : \n",ref)