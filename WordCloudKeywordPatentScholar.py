import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from funcTxtAnalytics import add_abstract, stringWord, addIPCdescription, stopwords, frequentWords, patent_abstract,df_patent_full,patent_fulltext,add_fulltext
import funcTxtAnalytics as fta
import math

"""You can put in either the original CSV or the OUTPUT.CSV  meaning, the original dataframe or the result of searched data frame"""
# from patent_scraping import add_abstract

inPath =     r"C:\Users\U375297\OneDrive - Danfoss\Desktop\# Programming Projects\Data management\Data\\Raw Data\\"
wrdCldPath = r"C:\Users\U375297\OneDrive - Danfoss\Desktop\# Programming Projects\Data management\Data\\Word Cloud\\"
outPath =    r"C:\Users\U375297\OneDrive - Danfoss\Desktop\# Programming Projects\Data management\Data\\Search Result\\"

# fileName = r"PatentsAbstractBallValve20142020.csv"
fileName = "ArticleWaterValveRefrigeration.csv"
# fileName = "ArticlePressureRegulator.csv"
# fileName ="SCHOLAR2023-2025.csv"
# fileName =".csv"
# fileName =".csv"
# fileName =".csv"
# fileName =".csv"
# fileName =".csv"
# fileName =".csv"
# fileName =".csv"

# fileName ="PatentSafetyValveCO2.csv"
# fileName ="PatentHighTempSeal1.csv"
# fileName =""
# fileName =""
# fileName =""


""" The column to SEARCH KEYWORD from """
# colName = "IPC Description"
# colName = "Title"
colName = "Abstract"
# colName = "Keywords"
# colName = "FullText"

""" The column to MAKE WORD CLOUD from """
# colNameWrdCld = "IPC Description"
# colNameWrdCld = "Title"
# colNameWrdCld = "Abstract"
colNameWrdCld = "Keywords"
# colNameWrdCld = "FullText"

"""----------------------------------------------"""
""" SELECT SEARCH WORD :::   %LOWER CASE ONLY % """
""" Can only take lower case """
# searchWord = "structural"
# searchWord = 'phase change'
# searchWord = "modeling"
# searchWord = "alternative"
# searchWord = "low cost"
# searchWord = "polymer"
# searchWord = "self-assembly"
# searchWord = "3d printing"
# searchWord = "circularity"
# searchWord = "durability"
# searchWord = "bio-based"
# searchWord = "phase change"
# searchWord = "organic framework"
# searchWord = "ceramics"
# searchWord = "waste heat"
# searchWord = "pcm"
# searchWord = "mepcms"
# searchWord = "droplet"
# searchWord = "leak"
# searchWord = "coating"
# searchWord = "refrigerant"
# searchWord = "material"
# searchWord = "perovskite"
searchWord = "cooling"
# searchWord = ""
# searchWord = ""
# searchWord = ""
# searchWord = ""
# searchWord = ""
# searchWord = ""
# searchWord = ""

"""----------------------------------------------"""

"""Number of digits from IPC code"""
#N=3     #first level
#N=4     #second level
N=9      #complete IPC code

"""----------------------------------------------"""
""" SELECT SEARCH WORD :::   %LOWER CASE ONLY % """
""" Can only take lower case """
"""----------------------------------------------"""

""" TO PRINT FULL DATAFRAME   """
# pd.set_option("display.max_rows", None, "display.max_columns", None)
# pd.options.display.max_colwidth = 100

""" Iterate through the csv file  """

if "Output" in fileName:  # If the file is from
    df = pd.read_csv(outPath + fileName, encoding="latin-1", low_memory=False)
else:
    df = pd.read_csv(inPath + fileName, encoding="latin-1", low_memory=False)

dftot = pd.DataFrame(columns=df.columns)
"""START:To sort based on the year published"""
df.sort_values(by='Publication Year', inplace=True)
"""END: To sort based on the year published"""


print("File name: ", fileName)
print("Column name: ", colName)

for i in range(math.ceil((len(df)/100))):
    print("I'm at row # ", i*100)
    try:
        dfi = df[i*100:(i+1)*100]
    except:
        dfi = df[i * 100:-1]
    if colName == "Abstract" and "Abstract" not in dfi.columns.tolist():
        """ Adds abstract to a data frame"""
        dfi = add_abstract(dfi)
    if colName == "IPC Description":
        """ add ipc descriptions """
        dfi = addIPCdescription(dfi, N)
    if colName == "FullText":
        """ add FullText"""
        dfi = add_fulltext(dfi)
    dftot = pd.concat([dftot, dfi], sort=False)

df = dftot
dfsearch = pd.DataFrame(columns = df.columns)

print(df.columns)
comment_words = ''
stopwords = set(fta.stopwords)
lt = []

for val in df[colName]:
    # typecaste each val to string
    val = str(val)

    if searchWord in val.lower():
        dfsearch = pd.concat([dfsearch, df.loc[df[colName] == val]])


        # split the value
        tokens = val.split()

        # Converts each token into lowercase
        for i in range(len(tokens)):
            tokens[i] = tokens[i].lower()
            lt.append(tokens[i])

        comment_words += " ".join(tokens) + " "




try:
    [print("Pub Date: ", (dfsearch['Date Published'].tolist()[i]), "External: ", dfsearch['External URL'].tolist()[i],
           "Internal: ", dfsearch['Source URLs'].tolist()[i]) for i in range(len(dfsearch['Source URLs']))]

except:
    try:
        # print(dfsearch["DOI"])
        with pd.option_context('display.max_rows', None,
                               'display.max_columns', None,
                               'display.precision', 3,
                               ):
            print(dfsearch["URL"])
    except:
        print("Missing URL!")
# We'll create a new list that contains punctuation we wish to clean.
punctuations = ['(', ')', ';', ':', '[', ']', ',', '™', '/', '.']
# We initialize the stopwords variable, which is a list of words like "The," "I," "and," etc. that don't hold much value as keywords.

# We create a list comprehension that only returns a list of words that are NOT IN stop_words and NOT IN punctuations.
# wanted =['cascade', 'ammonia', 'CO', 'learning']
keywords = [word for word in lt if not word in fta.stopwords and not word in punctuations]
# print(keywords)
# match = [word for word in lt if word in wanted]
# print(match)
dictionary = fta.wordListToFreqDict(keywords)
sorteddict = fta.sortFreqDict(dictionary)

for s in sorteddict:
    if s[0] >= 1:
        print(str(s))


""" WARNING: THE WORDCLOUD IS ONLY BASED ON THE SEARCH DATAFRAME """
"""Creates an string from a column of a data frame"""
"""Used prior to wordcloud for preparing the string"""
string = stringWord(dfsearch, colNameWrdCld)

# # plot the WordCloud image
# print(string)

try:
    wordcloud = WordCloud(width=2400, height=3840, background_color='black', stopwords=stopwords,
                      prefer_horizontal=1, min_font_size=5).generate(string)
except:
    print("The search dataframe is empty")

plt.figure('General wordcloud', figsize=(8, 16), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

if colName == "IPC Description":
    figName = str(wrdCldPath) +  "WordCloud_" + fileName[0:-4] + "_" + str(N) + "_digits_" + colName + ".pdf"
else:
    figName = str(wrdCldPath) +  "WordCloud_" + fileName[0:-4] + "_" + colName + "_"+ searchWord + ".pdf"


plt.savefig(figName, dpi=500, format="pdf",)
# plt.savefig(figName, dpi=500, format="svg",)

"""Save the new df with IPC descriptions"""
if colName == "IPC Description":
    df.to_csv( str(outPath) +  fileName[0:-4] + "_" + str(N) + "_digits_" + colName + ".csv")
if colName == "Abstract":
    df.to_csv( str(outPath) +  fileName[0:-4] + "_" + str(N) + colName + ".csv")

data = pd.DataFrame(dfsearch)
data.to_excel( str(outPath) +   fileName[0:-4] + searchWord + "Output.xlsx")
data.to_csv( str(outPath) +   fileName[0:-4] + searchWord + "Output.csv")

plt.show()



