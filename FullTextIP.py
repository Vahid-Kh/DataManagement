
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from funcTxtAnalytics import addAbstract, stringWord, addIPCdescription, stopwords, frequentWords, add_abstract

# from patent_scraping import add_abstract

inPath = r"C:\Users\U375297\Danfoss\RAC Tech Center - Programming Projects - Documents\Python Projects\Data management\Data\Raw Data\\"
wrdCldPath = r"C:\Users\U375297\Danfoss\RAC Tech Center - Programming Projects - Documents\Python Projects\Data management\Data\Word Cloud\\"
outPath = r"C:\Users\U375297\Danfoss\RAC Tech Center - Programming Projects - Documents\Python Projects\Data management\Data\Search Result\\"


fileName ="PatentAbstractGrantedPressureRegulator20102020.csv"
# fileName =".csv"
# fileName =".csv"
# fileName =".csv"
# fileName =".csv"
# fileName =".csv"
# fileName =".csv"
# fileName =".csv"
# fileName =".csv"
# fileName =".csv"
# fileName =".csv"
# fileName =".csv"
# fileName =".csv"
# fileName =".csv"


""" The column to read from """
# colName = "IPC Description"
# colName = "Title"
# colName = "Keywords"
colName = "Abstract"
# colName = "Fulltext"
# colName = "Claims"
# colName = "Description"

"""Number of digits from IPC code"""
#N=3     #first level
#N=4     #second level
N=9      #complete IPC code

"""----------------------------------------------"""
""" SELECT SEARCH WORD :::   %LOWER CASE ONLY % """
""" Can only take lower case """
"""----------------------------------------------"""

""" TO PRINT FULL DATAFRAME   """
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.options.display.max_colwidth = 100
""" Iterate through the csv file  """
df = pd.read_csv(inPath + fileName, encoding="latin-1", low_memory=False)
dftot = pd.DataFrame(columns=df.columns)
print("File name: ", fileName)
print("Column name: ", colName)
for i in range(round(len(df)/100)):

    print("I'm at row # ", i*100)
    dfi = df[i*100:(i+1)*100]

    if colName == "Abstract" and "Abstract" not in dfi.columns.tolist():
        """ Adds abstract to a data frame"""
        dfi = add_abstract(dfi)
    if colName == "IPC Description":
        """ add ipc descriptions """
        dfi = addIPCdescription(dfi, N)
    dftot = dftot.append(dfi, sort=False)

df = dftot
"""Creates an string from a column of a data frame"""
"""Used prior to wordcloud for preparing the string"""
string = stringWord(df, colName)

# # plot the WordCloud image
# print(string)

wordcloud = WordCloud(width=10000, height=6000, background_color='white', stopwords=stopwords,
                      prefer_horizontal=1, min_font_size=10).generate(string)

plt.figure('General wordcloud', figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

if colName == "IPC Description":
    figName = str(wrdCldPath) +  "WordCloud_" + fileName[0:-4] + "_" + str(N) + "_digits_" + colName + ".pdf"
else:
    figName = str(wrdCldPath) +  "WordCloud_" + fileName[0:-4] + "_" + colName + ".pdf"


plt.savefig(figName, dpi=500, format="pdf",)

plt.show()

"""Save the new df with IPC descriptions"""
if colName == "IPC Description":
    df.to_csv( str(outPath) +  fileName[0:-4] + "_" + str(N) + "_digits_" + colName + ".csv")
if colName == "Abstract":
    df.to_csv( str(outPath) +  fileName[0:-4] + "_" + str(N) + colName + ".csv")

most_occur = frequentWords(string)
#
# """Save the new df with frequency words"""
# if colName == "IPC Description":
#     most_occur.to_csv("FrequentWords_" + fileName[0:-4] + "_" + str(N) + "_digits_" + colName + ".csv")
# else:
#     most_occur.to_csv("FrequentWords_" + fileName[0:-4] + colName + ".csv")



