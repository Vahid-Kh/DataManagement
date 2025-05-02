import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud


from funcTxtAnalytics import addAbstract, stringWord, addIPCdescription, my_stopwords, frequentWords, add_abstract

# from patent_scraping import add_abstract


path = r"C:\Users\U375297\Danfoss\RAC Tech Center - Programming Projects - Documents\Python Projects\Data management\Data\Raw Data\\"
fileName= "MineBeaSteppingMotor.csv"
# fileName = r"PatentsAbstractBallValve20142020.csv"

""" The column to read from """
# colName = "IPC Description"
# colName = "Title"
colName = "Abstract"
# colName = "Keywords"

"""Number of digits from IPC code"""
#N=3     #first level
#N=4     #second level
N=9      #complete IPC code


"""----------------------------------------------"""
""" SELECT SEARCH WORD :::   %LOWER CASE ONLY % """
""" Can only take lower case """
"""----------------------------------------------"""
searchWord = 'fuel cell'
# searchWord = 'purger'
"""----------------------------------------------"""




""" TO PRINT FULL DATAFRAME   """
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.options.display.max_colwidth = 100
""" Iterate through the csv file  """
df = pd.read_csv(path + fileName, encoding="latin-1")

if colName == "Abstract":
    """ Adds abstract to a data frame"""
    df = add_abstract(df)

if colName == "IPC Description":
    """ add ipc descriptions """
    df = addIPCdescription(df, N)

"""Creates an string from a column of a data frame"""
"""Used prior to wordcloud for preparing the string"""
string = stringWord(df, colName)

# # plot the WordCloud image
wordcloud = WordCloud(width=5000, height=3000, background_color='white', stopwords=my_stopwords,
                      prefer_horizontal=1, min_font_size=10).generate(string)

plt.figure('General wordcloud', figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

if colName == "IPC Description":
    figName =  "WordCloud_" + fileName[0:-4] + "_" + str(N) + "_digits_" + colName + ".pdf"
else:
    figName =  "WordCloud_" + fileName[0:-4] + "_" + colName + ".pdf"


plt.savefig(figName, dpi=500, format="pdf",)

plt.show()

"""Save the new df with IPC descriptions"""
if colName == "IPC Description":
    df.to_csv( fileName[0:-4] + "_" + str(N) + "_digits_" + colName + ".csv")


# most_occur = frequentWords(string)
#
# """Save the new df with frequency words"""
# if colName == "IPC Description":
#     most_occur.to_csv("FrequentWords_" + fileName[0:-4] + "_" + str(N) + "_digits_" + colName + ".csv")
# else:
#     most_occur.to_csv("FrequentWords_" + fileName[0:-4] + colName + ".csv")

