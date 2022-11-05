import requests
from bs4 import BeautifulSoup
import pandas as pd
import random

url = "https://www.ettoday.net/news/news-list.htm"

user_agents = [
 "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
 "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    ]

headers = {
    "user-agent":random.choice(user_agents)
}

resp =requests.post(url, headers = headers)

soup = BeautifulSoup(resp.text,"lxml")

# elem = soup.select(".part_list_5")
elem = soup.select(".part_list_2")

title_list = []
date_list = []
cate_list = []
link_list = []

for e in elem:
    title_list = [title.text for title in e.select("a")]
    #print(title_list)
    link_list = [i.get('href') for i in e.select("a")]
    #print(link_list)
    date_list = [date.text for date in e.select(".date")]
    #print(date_list)
    cate_list = [cate.text for cate in e.select("em")]


title_list.reverse()
cate_list.reverse()
date_list.reverse()
pd.set_option("display.max_row", None)
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
# df = pd.DataFrame(data = title_list)

dic = {
    "title":title_list,
    "cate" :cate_list,
    "date" :date_list,    
}

list1 = [i for i in range(100)]
df = pd.DataFrame(dic, index=list1)

print(df)

# df["title"]=title_list
# df["category"]= cate_list
# df["date"]=date_list
