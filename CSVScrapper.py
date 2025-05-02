"""

This script:
    1 - Downloads CSV file from any link containing CSV format
    2 - Creates an Excel file with all the data from the file
    3 - The Excel file will then be saved

    Hint: The BeautifulSoup request is used in a way to search for CSV & works as long as the link
    contains the CSV file with the specified data

"""

from PyPDF2 import PdfFileReader
import requests
import io
from bs4 import BeautifulSoup
from contextlib import closing
import csv
import pandas as pd

urlList = [
  "https://ark-funds.com/arkk",
  # "https://ark-funds.com/arkq",
  # "https://ark-funds.com/arkw",
  # "https://ark-funds.com/arkg",
  # "https://ark-funds.com/fintech-etf"
    ]

columnNames = [
    "date",
    "fund",
    "company",
    "ticker",
    "cusip",
    "shares",
    "market value($)",
    "weight(%)",
                ]

dfTot = pd.DataFrame(columns = columnNames)

for etf in urlList:
    url = requests.get(etf)
    soup = BeautifulSoup(url.content,"lxml")
    for a in soup.find_all('a', href=True):
        mystr= a['href']
        if(mystr[-4:]=='.csv'):
            print ("url with csv final:", a['href'])
            urlcsv = a['href']
            r = requests.get(urlcsv)

            with closing(requests.get(urlcsv, stream=True)) as r:
                f = (line.decode('utf-8') for line in r.iter_lines())
                reader = csv.reader(f, delimiter=',', quotechar='"')
                df = pd.DataFrame(reader)
                df = df[1:-3]
                df.columns= columnNames
                # print(df)
                dfTot = dfTot.append(df)

dfTot['weight(%)'] = pd.to_numeric(dfTot['weight(%)'], downcast="float")
dfTot['market value($)'] = pd.to_numeric(dfTot['market value($)'], downcast="float")
dfTot['shares'] = pd.to_numeric(dfTot['shares'], downcast="float")
dfTot.sort_values(by=['weight(%)'],ascending=False , inplace=True, kind="heapsort")

date = str(dfTot.iloc[0]["date"]).replace("/","-")
dfTot.to_excel(r"ArkFund" + str(date) + ".xlsx")
print(dfTot)