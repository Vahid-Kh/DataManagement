import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import pandas as pd

import re



def abstract_scraper(patent_ID):
     patent_ID = patent_ID.replace(" ", "").replace("/", "")

     url = "https://patents.google.com/patent/" + patent_ID

     response = requests.get(url)

     soup = BeautifulSoup(response.text, "html.parser")

     abstract = soup.find_all('abstract')

     abstract = str(abstract)

     abstract = abstract[:abstract.find("</div>")]

     abstract = abstract.replace("<b>", "(")
     abstract = abstract.replace("</b>", ")")

     abstract = abstract.replace("<i>", "")
     abstract = abstract.replace("</i>", "")

     abstract = abstract[(abstract.rfind(">")+1):]

     return (abstract)

def add_abstract(df):

    for i in df.index:
         patent_ID = df.loc[i, 'Publication Number']

         abstract = abstract_scraper(patent_ID)

         df.loc[i, "Abstract"] = abstract

         print(abstract)

         time.sleep(0.5)

    return (df)


# df = pd.read_csv(r"Solenoid Valves/SV inputs/SV_general.csv", encoding="latin-1")
#
# df = df.head(100)
#
# df = add_abstract(df)




