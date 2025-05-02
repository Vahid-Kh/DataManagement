import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from funcTxtAnalytics import stringWord, addIPCdescription, stopwords, frequentWords, patent_abstract,df_patent_full,patent_fulltext,add_fulltext
import math

# from patent_scraping import add_abstract

inPath =        r"C:\Users\U375297\OneDrive - Danfoss\Desktop\# Programming Projects\Data management\Data\Raw Data\\"
wrdCldPath =    r"C:\Users\U375297\OneDrive - Danfoss\Desktop\# Programming Projects\Data management\Data\Word Cloud\\"
outPath =       r"C:\Users\U375297\OneDrive - Danfoss\Desktop\# Programming Projects\Data management\Data\Search Result\\"

# fileName = r"PatentsAbstractBallValve20142020.csv"
fileName = "ArticleWaterValveRefrigeration.csv"
# fileName = "ArticlePressureRegulator.csv"
# fileName ="SCHOLAR2023-2025.csv"
# fileName =""
# fileName =""
# fileName =""
# fileName =""
# fileName =""
# fileName =""
# fileName =""
# fileName =""
# fileName =""
# fileName =""
# fileName =""
# fileName =""
# fileName =""
# fileName =""
# fileName =""
# fileName =""
# fileName =""
# fileName =""

""" The column to read from """
# colName = "IPC Description"
# colName = "Title"
# colName = "Abstract"
colName = "Keywords"
# colName = "FullText"
# colName = "Applicants"

"""Number of digits from IPC code"""
#N=3     #first level
# N=4     #second level
N=9      #complete IPC code

"""----------------------------------------------"""
""" SELECT SEARCH WORD :::   %LOWER CASE ONLY % """
""" Can only take lower case """
"""----------------------------------------------"""

""" TO PRINT FULL DATAFRAME   """
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.options.display.max_colwidth = 100
""" Iterate through the csv file  """

if "Output" in fileName:  # If the file is from
    df = pd.read_csv(outPath + fileName, encoding="latin-1", low_memory=False)
else:
    df = pd.read_csv(inPath + fileName, encoding="latin-1", low_memory=False)

"""START:To sort based on the year published"""
df.sort_values(by='Publication Year', inplace=True)
dftot = pd.DataFrame(columns=df.columns)
print("File name: ", fileName)
# print("Column name: ", colName)



for i in range(math.ceil((len(df)/100))):

    print("I'm at row # ", i*100)
    try:
        dfi = df[i*100:(i+1)*100]
    except:
        dfi = df[i * 100:-1]

    # if colName == "Abstract" and "Abstract" not in dfi.columns.tolist():
    #     """ Adds abstract to a data frame"""
    #     dfi = add_abstract(dfi)
    if colName == "IPC Description":
        """ add ipc descriptions """
        dfi = addIPCdescription(dfi, N)
    if colName == "FullText":
        """ add FullText"""
        dfi = add_fulltext(dfi)
    dftot = pd.concat([dftot, dfi], sort=False)

df = dftot
# print(df.columns)
pd.options.display.max_colwidth =200
# print(df["Abstract"])
"""Creates an string from a column of a data frame"""
"""Used prior to wordcloud for preparing the string"""
string = stringWord(df, colName)

# plot the WordCloud image
# print(string)

# wordcloud = WordCloud(width=2400, height=3840, background_color='black', stopwords=stopwords,
#                       prefer_horizontal=1, min_font_size=5).generate(string)

plt.figure('General wordcloud', figsize=(8, 16), facecolor=None)
# plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

if colName == "IPC Description":
    figName = str(wrdCldPath) +  "WordCloud_" + fileName[0:-4] + "_" + str(N) + "_digits_" + colName + ".pdf"
else:
    figName = str(wrdCldPath) +  "WordCloud_" + fileName[0:-4] + "_" + colName + ".pdf"

plt.savefig(figName, dpi=500, format="pdf",)
# plt.savefig(figName, dpi=500, format="svg",)
plt.show()

"""Save the new df with IPC descriptions"""
if colName == "IPC Description":
    df.to_csv( str(outPath) +  fileName[0:-4] + "_" + str(N) + "_digits_" + colName + ".csv")
if colName == "Abstract":
    df.to_csv( str(outPath) +  fileName[0:-4] + "_" + str(N) + colName + ".csv")
# df = df_patent_full(df)
most_occur = frequentWords(string)
print(most_occur)
print(most_occur[:round(len(most_occur)/10)])
#
"""Save the new df with frequency words"""
if colName == "IPC Description":
    most_occur.to_csv("FrequentWords_" + fileName[0:-4] + "_" + str(N) + "_digits_" + colName + ".csv")
else:
    most_occur.to_csv("FrequentWords_" + fileName[0:-4] + colName + ".csv")
