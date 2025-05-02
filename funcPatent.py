# utf-8
""" # funcTxtAnlytcs.py

This library contains multiple functions performing followins:
- Removing Stop wordts from a text
- Removing tags, signs and all non-alphanumeric
- Makes a dictionary of a list of words and returns the frequency
- Parses a PDF into list
- Gets the IP number and downloads the abstract from Google and translates it into English
-
"""

import pandas as pd
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
codec = 'utf-8'

import re
from urllib.request import urlopen
from bs4 import BeautifulSoup


def full_patent_list(patent_ID):
    """
     [text, abstract, claims, description] IS THE LIST IN LIST FORMAT
    """
    try:
        patent_ID = patent_ID.replace(" ", "").replace("/", "")
        url = "https://patents.google.com/patent/" + patent_ID + "/en"
        time.sleep(0.5)
        html = urlopen(url).read()
        # soup = BeautifulSoup(html, features="html.parser")

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")
        # kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()    # rip it out

        # get text
        text = soup.get_text()

        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

        # drop blank lines

        try:
            fulltext = ' '.join(chunk for chunk in chunks if chunk)
        except:
            fulltext = " "

        try:

            """To take the abstract out"""
            abstract = soup.find_all('abstract')
            abstract = str(abstract)
            abstract = abstract[:abstract.find("</div>")]
            abstract = abstract.replace("<b>", "(")
            abstract = abstract.replace("</b>", ")")
            abstract = abstract.replace("<i>", "")
            abstract = abstract.replace("</i>", "")
            abstract = abstract[(abstract.rfind(">") + 1):]

        except:
            try:
                mark0 = """Abstract
                        """
                mark1 = """Description
                """
                start = text.find(mark0) + len(mark0)
                end = text.find(mark1, start)
                abstract = text[start:end]
            except:
                abstract = " "

        try:
            """To take the CLAIMS out"""
            text= fulltext
            mark0 = "Claims ("
            mark1 = "Priority Applications ("
            start = text.find(mark0) + len(mark0)
            end = text.find(mark1, start)
            claims = text[start:end]
        except:
            claims = " "

        """To add the description"""
        try:
            soup = BeautifulSoup(response.text, "lxml")
            soup = soup.find_all('div')
            description = " "
            for tex in soup:
                quotes = re.findall(r'"[^"]*"', str(tex), re.U)
                if "description" in quotes[0]:
                    soup = BeautifulSoup(''.join(str(tex)), "lxml")
                    des = soup.find('div', {'class': quotes[0][1:-1]}).string
                    description += str(des) + "; "
        except:
            try:
                """To take the Description out """
                mark0 = "Description"
                mark1 = "Claims ("
                start = text.find(mark0) + len(mark0)
                end = text.find(mark1, start)
                description = text[start:end]

            except:
                description = " "

    except:
        fulltext, abstract, claims, description = ["It", "has", "failed", "!!!"]

    return [fulltext, abstract, claims, description]

def df_patent_full(df):
    for i in df.index:
        patent_ID = df.loc[i, 'Publication Number']
        list = full_patent_list(patent_ID)

        df.loc[i, "Fulltext"] = list[0]
        df.loc[i, "Abstract"] = list[1]
        df.loc[i, "Claims"] = list[2]
        df.loc[i, "Description"] = list[3]
        time.sleep(0.5)
    print('Fulltext added!')
    return df


IPC_codes = pd.read_csv(r'IPC_table.xlsx').drop(columns=['Unnamed: 0'], axis=1)
def df_patent_ipc(df, N):
    try:
        IPC_codes = pd.read_csv(r'IPC_table_new.csv').drop(columns=['Unnamed: 0'], axis=1)

        columnIPC = pd.DataFrame(df["IPCR Classifications"])
        columnIPC = columnIPC["IPCR Classifications"].str.split(';;', expand=True).add_prefix('code_')


        for i in columnIPC.columns:
            columnIPC[i] = columnIPC[i].astype(str).str[:N]

        for i in columnIPC.index:
            columnIPC.loc[i, :] = columnIPC.loc[i, :].drop_duplicates(keep='first')
        s = IPC_codes.set_index('code')['description']
        columnIPC = columnIPC.replace(s)
        columnIPC = columnIPC.fillna(value='')
        columnIPC['IPC Description'] = columnIPC[columnIPC.columns[0:]].apply(
            lambda x: ';'.join(x.dropna().astype(str)),
            axis=1
        )
        pd.set_option('display.max_colwidth', -1)
        df['IPC Description'] = list(columnIPC['IPC Description'])
        # print('Descriptions added!')
    except:

        # print('Descriptions adding failed!')

        df['IPC Description'] = list(df["IPCR Classifications"])


    return df

patnum= "US6117551A"
pattext = full_patent_list(patnum)
for i in range(4):
    print(pattext[i])



